import pathlib

from gems import core, base
from gems.facets import local_ids_query, global_ids_query
from pdml import saver
from tkgems import tkcore
from tkgems.tkfacets import tkattrs

selected_listbox_cluster_index: int | None = 0
selected_cluster_name: str = "Aggregate"


def init_listbox_cluster(listbox_cluster_gem: base.Gem) -> None:
    global selected_listbox_cluster_index
    global selected_cluster_name
    listbox_cluster_object = tkattrs.get_tkobject(listbox_cluster_gem)
    listbox_cluster_object.insert("end", "Aggregate")
    for cluster_name in sorted(global_ids_query.aggregate_get_cluster_names()):
        listbox_cluster_object.insert("end", cluster_name)
    listbox_cluster_object.select_set(0)
    selected_listbox_cluster_index = 0
    selected_cluster_name = "Aggregate"
    listbox_cluster_object.see(0)


def listbox_cluster_selection(listbox_cluster_gem: base.Gem, event: any) -> None:
    print(123, "todo")


def create_viewer_resource_gems() -> None:
    core.create_resource_gem("viewer.init_listbox_cluster", init_listbox_cluster)
    core.create_resource_gem("viewer.listbox_cluster_selection", listbox_cluster_selection)


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
    create_viewer_resource_gems()
    viewer_cluster = core.load(viewer_pdml_path)
    print()
    print("viewer_cluster is None:", viewer_cluster is None)
    if viewer_cluster is None:
        return
    print()
    print("aggregate:")
    saver.debug(base.get_aggregate())
    print()
    print("viewer_cluster:")
    saver.debug(viewer_cluster)
    window_gem = local_ids_query.get_gem_by_gem_base_name(viewer_cluster, "RootWindow")
    if window_gem is None:
        print("window_gem is None")
        return
    window = tkcore.tkeval(window_gem)
    window.mainloop()


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    initialize(home_path)
