import pathlib

from gems import core, base
from gems.facets import local_ids_update, global_tags_update
from pdml import saver


def hi_there():
    print("Hello World!")


def test(home_path: pathlib.Path) -> None:
    print()
    print("*** core test ***")
    test_data_path = home_path / pathlib.Path("test data")
    print("test data path:", test_data_path)
    print()
    print("function resource test:")
    core.initialize(home_path)
    hi_there_function = core.add_function("hi_there", hi_there)
    global_tags_update.set_description(hi_there_function, "Hello World!")
    core.get_function("hi_there")()
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
