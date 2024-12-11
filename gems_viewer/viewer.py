import pathlib

from gems import core
from gems.facets import local_ids_query
from pdml import saver
from tkgems import tkcore


def initialize(home_path: pathlib.Path) -> None:
    print()
    print("*** start viewer ***")
    print("home path:", home_path)
    if home_path is None:
        return
    viewer_pdml_path = home_path / "viewer.pdml"
    print("viewer.pdml path:", viewer_pdml_path)
    if viewer_pdml_path is None:
        return
    core.initialize(home_path)
    tkcore.initialize(home_path)
    viewer_cluster = core.load(viewer_pdml_path)
    print()
    print("viewer_cluster is None:", viewer_cluster is None)
    if viewer_cluster is None:
        return
    saver.debug(viewer_cluster)
    window_gem = local_ids_query.get_gem_by_gem_base_name(viewer_cluster, "RootWindow")
    if window_gem is None:
        print("window_gem is None")
        return


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    initialize(home_path)
