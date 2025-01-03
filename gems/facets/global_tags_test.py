import pathlib

from gems import core, base
from gems.facets import global_tags_query
from pdml import saver


def test(home_path: pathlib.Path) -> None:
    print()
    print("*** global tags test ***")
    test_data_path = home_path / pathlib.Path("test data")
    print("test data path:", test_data_path)
    core.initialize(home_path)
    global_tags_test = core.load(test_data_path / pathlib.Path("global_tags_test.pdml"))
    print()
    print("aggregate tag names:")
    print(global_tags_query.aggregate_get_tag_names())
    print()
    print("aggregate get tag values:")
    print("simpleGlobalTag:", global_tags_query.aggregate_get_tag_values("simpleGlobalTag"))
    print("aGemName:", global_tags_query.aggregate_get_tag_values("aGemName"))
    print("bGemName:", global_tags_query.aggregate_get_tag_values("bGemName"))
    saver.debug(global_tags_query.aggregate_get_gems_by_tag("bGemName", "Aggregate.unknown"))


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    test(home_path)
