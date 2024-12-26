import pathlib
import typing
from collections import abc


class Cursor(typing.TypedDict):
    buf: str
    line: int
    more: abc.Iterator[str] | None
    from_path: pathlib.Path | None


def buf(cursor: Cursor) -> str:
    return cursor["buf"]


def line(cursor: Cursor) -> int:
    return cursor["line"]


def more(cursor: Cursor) -> abc.Iterator | None:
    return cursor["more"]


def buf_count(cursor: Cursor) -> int:
    return len(buf(cursor))


def echo(line: int, buf: str):
    print(str(line) + ":", buf)


def create_cursor(more: abc.Iterator[str], file_path: pathlib.Path = None) -> Cursor:
    buf: str = next(more, None)
    line: int = 1
    from_path: pathlib.Path = file_path
    return {"buf": buf, "line": line, "more": more, "from_path": from_path}


def get_lines(from_path: pathlib.Path) -> abc.Iterator[str]:
    def it() -> abc.Iterator[str]:
        with from_path.open("r") as from_file:
            s = True
            while s:
                s = from_file.readline()
                if s:
                    yield s
                else:
                    return
    return it()


def cursor_from_file(from_path: pathlib.Path) -> Cursor:
    return create_cursor(get_lines(from_path), file_path=from_path)


def cursor_from_string(full: str) -> Cursor:
    lines = full.split("\n")

    def it() -> abc.Iterator[str]:
        for ln in lines:
            yield ln + "\n"
    return create_cursor(it())


def check(cursor: Cursor, width: int) -> bool:
    b = buf(cursor)
    while more(cursor) is not None and len(b) < width:
        try:
            n = next(more(cursor))
            line = cursor["line"] + 1
            b += n
            cursor["buf"] = b
            # echo(line, n)
            cursor["line"] = line
        except StopIteration:
            cursor["more"] = None
            break
    return len(b) >= width


def is_empty(cursor: Cursor) -> bool:
    return not check(cursor, 1)


def ensure(cursor: Cursor, width: int = 1) -> None:
    if not check(cursor, width):
        raise Exception("input is short")


def skip(cursor: Cursor, iw: int = 1) -> None:
    ensure(cursor, iw)
    cursor["buf"] = buf(cursor)[iw:]


def fetch(cursor: Cursor, width: int = 1) -> str:
    if width == 0:
        return ""
    ensure(cursor, width)
    b = buf(cursor)
    v = b[:width]
    cursor["buf"] = b[width:]
    return v


def peek_char(cursor: Cursor, skip: int = 0) -> str | None:
    if not check(cursor, skip + 1):
        return None
    return buf(cursor)[skip]


def is_not_space(c: str) -> bool:
    return c != " "


def is_nl(c: str) -> bool:
    return c == "\n"


def spaces_count(cursor: Cursor) -> int:
    i = 0
    while True:
        c = peek_char(cursor, i)
        if c is None or is_not_space(c):
            return i
        i += 1


def empty(cursor: Cursor) -> None:
    cursor["buf"] = ""
    cursor["more"] = None


def count_whitespace(cursor: Cursor) -> (int, str):
    is_significant = is_not_space
    i = 0
    while True:
        c = peek_char(cursor, i)
        if c is None:
            return tuple((i, c))
        elif c == "#":
            is_significant = is_nl
        elif is_significant(c):
            return tuple((i, c))
        i += 1


def trim_right(cursor: Cursor) -> None:
    (i, c) = count_whitespace(cursor)
    if c is None:
        empty(cursor)
    elif c == "\n":
        skip(cursor, i + 1)
    else:
        raise Exception("unexpected token")


def skip_empty_lines(cursor) -> None:
    while True:
        (i, c) = count_whitespace(cursor)
        if c is None:
            empty(cursor)
            break
        if c == "\n":
            skip(cursor, i + 1)
        else:
            break


def trim_skip(cursor) -> None:
    trim_right(cursor)
    skip_empty_lines(cursor)


def test_textin(home_path: pathlib.Path):
    print("\ntextin tests\n")

    cu = cursor_from_string("ab c\nd")
    print(cu)
    ensure(cu, 5)
    ensure(cu, 5)
    print(check(cu, 5))
    print(check(cu, 6))
    print(peek_char(cu, 3))
    print(peek_char(cu, 5))
    print(fetch(cu, 1))
    print(fetch(cu, 6))
    print(is_empty(cu))

    test_data_path = home_path / pathlib.Path("test data")
    manual_path = test_data_path / "manual"
    from_path = manual_path / "m006.pdml"
    print(from_path)
    cursor: Cursor = cursor_from_file(from_path)
    print(cursor)


if __name__ == "__main__":
    test_textin(pathlib.Path("."))
