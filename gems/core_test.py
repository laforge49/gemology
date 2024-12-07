import pathlib

from gems import core, base
from pdml import saver


def test(home_path: pathlib.Path) -> None:
    print()
    print("*** core test ***")
    # core.load_types(home_path)
    test_data_path = home_path / pathlib.Path("test data")
    print("test data path:", test_data_path)
    sample1 = core.load(test_data_path / pathlib.Path("sample1.pdml"))
    print()
    print("aggregate:")
    print(base.get_aggregate())
    saver.debug(base.get_aggregate())
    print()
    print("sample1")
    print(sample1)
    saver.debug(sample1)
    core.save_as(sample1, test_data_path / pathlib.Path("sample1a.pdml"))


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    test(home_path)
