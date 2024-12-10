import pathlib


def test(home_path: pathlib.Path) -> None:
    print()
    print("*** tkcore test ***")
    test_data_path = home_path / pathlib.Path("test data")
    print("test data path:", test_data_path)
    print()
