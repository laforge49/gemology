import pathlib

from pdml import textin
import ast
import enum


class Delim(enum.Enum):
    EOL = "end of line (new line)"
    EOT = "end of token (space)"
    EOK = "end of key (colon)"
    EOF = "end of file"
    EOG = "end of group(dedent)"
    NOT = "not applicable"


class PDmlException(Exception):
    """Invalid Python Data markup language syntax"""
    def __init__(self, msg: str, cursor: textin.Cursor | None):
        line = textin.line(cursor)
        super().__init__(msg + "\n  line " + str(line))


def get_list(ind: int, cursor: textin.Cursor) -> list:
    ls = []
    first = True
    while True:
        (ind, t) = get_data(cursor, ind, first=first)
        first = False
        if t is None:
            return ls
        ls.append(t)


def get_dict(ind: int, cursor: textin.Cursor) -> dict:
    di = {}
    first = True
    while True:
        (ind, k) = get_data(cursor, ind, first=first, right=False)
        first = False
        if k is None:
            return di
        if isinstance(k, str) and k.startswith("#"):
            raise PDmlException("key may not start with #", cursor)
        if textin.peek_char(cursor) != " ":
            raise PDmlException("one or more spaces must follow : at end of key", cursor)
        while not textin.is_empty(cursor) and textin.peek_char(cursor) == " ":
            textin.skip(cursor)
        (_, v) = get_data(cursor, ind, left=False)
        di[k] = v


def get_set(ind: int, cursor: textin.Cursor) -> set:
    ls = set()
    first = True
    while True:
        (ind, t) = get_data(cursor, ind, first=first)
        first = False
        if t is None:
            return ls
        ls.add(t)


def evaler(ind: int, t: str, cursor: textin.Cursor) -> any:
    if t == "list":
        return get_list(ind, cursor)
    if t == "dict":
        return get_dict(ind, cursor)
    if t == "set":
        return get_set(ind, cursor)
    try:
        return ast.literal_eval(t)
    except Exception as exc:
        raise PDmlException("Eval error", cursor) from exc


def get_string_token(cursor: textin.Cursor) -> tuple[str | None, Delim]:
    if textin.peek_char(cursor) != "\"":
        return tuple((None, Delim.NOT))
    v_lst = []
    i = 1
    while not textin.is_empty(cursor):
        c = textin.peek_char(cursor, i)
        if c == "\"":
            i += 1
            textin.skip(cursor, i)
            c = textin.peek_char(cursor)
            if c is None:
                return tuple(("".join(v_lst), Delim.EOF))
            if c == " ":
                return tuple(("".join(v_lst), Delim.EOT))  # end of token
            if c == ":":
                return tuple(("".join(v_lst), Delim.EOK))  # end of key
            if c == "\n":
                return tuple(("".join(v_lst), Delim.EOL))  # end of line
            raise PDmlException("invalid syntax after trailing \"", cursor)
        elif c == "\\":
            i += 1
            c = textin.peek_char(cursor, i)
            if c is None:
                raise PDmlException("\\ found at end of file", cursor)
            i += 1
            if c == "n":
                v_lst.append("\n")
            else:
                v_lst.append(c)
        else:
            i += 1
            v_lst.append(c)
    raise PDmlException("string missing trailing \"", cursor)


def pre_token(cursor: textin.Cursor, ind: int, first: bool, left: bool) -> int | None:
    if left:
        textin.skip_empty_lines(cursor)
    if textin.is_empty(cursor):
        return None
    iw = textin.spaces_count(cursor)
    if left:
        if iw < ind:
            return None
        if first:
            if iw == ind:
                return None
        elif iw > ind:
            raise PDmlException("indented too far", cursor)
    textin.skip(cursor, iw)
    return iw


def get_token(cursor: textin.Cursor) -> (str, Delim):
    i = 0
    while True:
        c = textin.peek_char(cursor, i)
        if c is None:
            w = Delim.EOF
            break
        if c == " ":
            w = Delim.EOT
            break
        if c == ":":
            w = Delim.EOK
            break
        if c == "\n":
            w = Delim.EOL
            break
        if c == "#":
            raise PDmlException("space missing between token and comment", cursor)
        i += 1
    if i == 0:
        raise PDmlException("missing value", cursor)
    t = textin.fetch(cursor, i)
    return tuple((t, w))


def post_token(cursor: textin.Cursor, right: bool, w: Delim) -> None:
    if right:
        if w == Delim.EOT:
            textin.trim_right(cursor)
        elif w == Delim.EOL:
            textin.skip(cursor)
        elif w != Delim.EOF:
            raise PDmlException("unexpected termination of single token", cursor)
    else:
        if w != Delim.EOK:
            raise PDmlException("missing : after key", cursor)
        textin.skip(cursor)


def get_data(cursor: textin.Cursor, ind: int = -1, first: bool = True, left: bool = True, right: bool = True) \
        -> (int, any):
    iw = pre_token(cursor, ind, first, left)
    if iw is None:
        return tuple((None, None))
    (t, w) = get_string_token(cursor)
    is_str = isinstance(t, str)
    if not is_str:
        (t, w) = get_token(cursor)
    post_token(cursor, right, w)
    if is_str:
        return tuple((iw, t))
    else:
        return tuple((iw, evaler(ind, t, cursor)))


def process_input(cursor: textin.Cursor) -> any:
    (_, data) = get_data(cursor)
    textin.skip_empty_lines(cursor)
    if not textin.is_empty(cursor):
        raise PDmlException("more than one top-level token?", cursor)
    return data


def reader(from_path: pathlib.Path) -> any:
    cursor: textin.Cursor = textin.cursor_from_file(from_path)
    return process_input(cursor)


def load_files_test(directory_path: pathlib.Path) -> None:
    for pdml_path in directory_path.glob("*.pdml"):
        print(pdml_path)
        try:
            da: any = reader(pdml_path)
            print(da)
        except PDmlException as exc:
            print(exc)
        except Exception as exc:
            print(type(exc))
        else:
            raise Exception("No error found")


def test_loader(home_path: pathlib.Path) -> None:
    test_data_path = home_path / pathlib.Path("test data")
    erroneous_path = test_data_path / "erroneous"
    print("\nerroneous strings:\n")
    load_files_test(erroneous_path)


if __name__ == "__main__":
    test_loader(pathlib.Path("."))
