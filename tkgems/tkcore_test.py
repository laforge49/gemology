import pathlib

from gems import core
from tkgems import tkcore


def test(home_path: pathlib.Path) -> None:
    print()
    print("*** tkcore test ***")
    test_data_path = home_path / pathlib.Path("test data")
    print("test data path:", test_data_path)
    core.initialize(home_path)
    tkcore.initialize(home_path)
    print()


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    test(home_path)
