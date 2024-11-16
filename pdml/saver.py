import pathlib
from collections import abc


def dict_to_strings(ind: int, d: dict, nested: bool) -> abc.Iterator[str]:
    if nested:
        yield ""
    else:
        yield " " * ind
    yield "dict"
    ind += 4
    for k, v in sorted(d.items()):
        yield "\n"
        yield " " * ind
        if isinstance(k, str) and k.startswith("#"):
            yield "# "
            for s in base_data_to_strings(k):
                yield s
            if isinstance(v, str):
                yield ' "' + v + '"'
            else:
                yield " ..."
        else:
            for s in base_data_to_strings(k):
                yield s
            yield ": "
            for s in data_to_strings(ind, v, True):
                yield s


def list_to_strings(ind: int, ls: list, nested: bool) -> abc.Iterator[str]:
    if nested:
        yield ""
    else:
        yield " " * ind
    yield "list"
    ind += 4
    for i in ls:
        yield "\n"
        yield " " * ind
        for s in data_to_strings(ind, i, True):
            yield s


def set_to_strings(ind: int, ls: set, nested: bool) -> abc.Iterator[str]:
    if nested:
        yield ""
    else:
        yield " " * ind
    yield "set"
    ind += 4
    for i in ls:
        yield "\n"
        yield " " * ind
        for s in data_to_strings(ind, i, True):
            yield s


def encode_char(c: str) -> str:
    if c == "\\":
        return "\\\\"
    if c == '"':
        return '\\"'
    if c == "\n":
        return "\\n"
    return c


def encode_str(s: str) -> str:
    s = "".join(encode_char(i) for i in s)
    return '"' + s + '"'


def base_data_to_strings(data) -> str:
    if isinstance(data, str):
        yield encode_str(data)
    else:
        yield str(data)


def data_to_strings(ind: int, data, nested: bool) -> abc.Iterator[str]:
    if isinstance(data, list):
        for s in list_to_strings(ind, data, nested):
            yield s
    elif isinstance(data, dict):
        for s in dict_to_strings(ind, data, nested):
            yield s
    elif isinstance(data, set):
        for s in set_to_strings(ind, data, nested):
            yield s
    else:
        for s in base_data_to_strings(data):
            yield s


def data_to_string(ind: int, data: any, nested: bool) -> str:
    return "".join(data_to_strings(ind, data, nested))

def debug(data: any) -> None:
    if data is None:
        print(None)
    else:
        print(data_to_string(0, data, False))


def writer(to_path: pathlib.Path, data:any) -> str:
    with to_path.open("w") as toFile:
        s = data_to_string(0, data, False)
        toFile.write(s)
        return s


def write_files_test(write_path: pathlib.Path) -> None:
    data_samples = [{"1": "a", "#2": "b", "3": "c"}]
    i = 0
    for da in data_samples:
        i += 1
        ri = str(i).rjust(3, "0")
        to_file_name = "w" + ri + ".pdml"
        to_path = write_path / to_file_name
        print(to_path)
        st = writer(to_path, da)


def test_write(home_path: pathlib.Path) -> None:
    print("write strings")
    test_data_path = home_path / pathlib.Path("test data")
    write_path = test_data_path / "write"
    write_files_test(write_path)


if __name__ == "__main__":
    test_write(pathlib.Path("."))
