import pathlib


from gems import core, base
from gems.facets import local_ids_query, global_ids_query, gems_query, attrs_query
from pdml import saver
from tkgems import tkcore
from tkgems.tkfacets import tkattrs, tkglobal_tags


selected_listbox_cluster_index: int | None = 0
selected_listbox_gem_index: int | None = 0
selected_cluster_name: str = "Aggregate"
Selected_cluster_gems: list = ["Aggregate"]
selected_gem_base_name: str = "Aggregate"
selected_gem_base_names: list = []
selected_gem_name: str = "Aggregate"
selected_gems_radiobutton: str = ".FrameGemsList"
selected_content_radiobutton: str = ".FramePdml"
selected_facet_names: list = []
selected_facet_name: str | None = None
selected_listbox_facet_index: int | None = None


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


def load_gems(tk_gem: base.Gem, listbox_gem_object: any, prefix: str = "") -> None:
    global selected_gem_base_names
    gem_name = core.get_gem_name(tk_gem)
    selected_gem_base_names.append(gem_name)
    listbox_gem_object.insert("end", prefix + gem_name)
    gemsfacet: base.GemsFacet = gems_query.get_gf(tk_gem)
    if gemsfacet is None:
        return
    for gem in gemsfacet:
        load_gems(gem, listbox_gem_object, prefix + "+")


def gems_radiobutton_clicked(gems_radiobutton_gem: base.Gem) -> None:
    global selected_gems_radiobutton
    value = tkattrs.get_options(gems_radiobutton_gem)["value"]
    if value == selected_gems_radiobutton:
        return
    frame_gem = global_ids_query.get_gem(selected_gems_radiobutton, gems_radiobutton_gem)
    tkcore.tk_destroy(frame_gem)
    selected_gems_radiobutton = value
    frame_gem = global_ids_query.get_gem(selected_gems_radiobutton, gems_radiobutton_gem)
    tkcore.tkeval(frame_gem)


def content_radiobutton_clicked(content_radiobutton_gem: base.Gem) -> None:
    global selected_content_radiobutton
    value = tkattrs.get_options(content_radiobutton_gem)["value"]
    if value == selected_content_radiobutton:
        return
    frame_gem = global_ids_query.get_gem(selected_content_radiobutton, content_radiobutton_gem)
    tkcore.tk_destroy(frame_gem)
    selected_content_radiobutton = value
    frame_gem = global_ids_query.get_gem(selected_content_radiobutton, content_radiobutton_gem)
    tkcore.tkeval(frame_gem)


def init_listbox_gem(listbox_gem_gem: base.Gem):
    global selected_listbox_gem_index
    global selected_cluster_name
    global selected_gem_base_name
    global selected_gem_base_names
    master_frame_gem = tkglobal_tags.resolve_master_frame_GemName(listbox_gem_gem)
    tkattrs.set_view_gem(master_frame_gem, listbox_gem_gem)
    listbox_gem_object = tkattrs.get_tkobject(listbox_gem_gem)
    listbox_gem_object.delete(0, "end")
    selected_gem_base_names = [selected_cluster_name]
    cluster_gem = global_ids_query.get_cluster_by_cluster_name(selected_cluster_name)
    gem_base_names = local_ids_query.cluster_get_gem_base_names(cluster_gem)
    if gem_base_names is not None:
        for gem_name in sorted(gem_base_names):
            selected_gem_base_names.append(gem_name)
    for gem_name in selected_gem_base_names:
        listbox_gem_object.insert("end", gem_name)
    gem_index = base.findin(selected_gem_base_names, selected_gem_base_name)
    if gem_index is None:
        gem_index = 0
    selected_listbox_gem_index = gem_index
    listbox_gem_object.select_set(selected_listbox_gem_index)
    listbox_gem_object.see(selected_listbox_gem_index)


def init_listbox_gem_tree(listbox_gem_gem: base.Gem):
    global selected_listbox_gem_index
    global selected_cluster_name
    global selected_gem_base_name
    global selected_gem_base_names
    master_frame_gem = tkglobal_tags.resolve_master_frame_GemName(listbox_gem_gem)
    tkattrs.set_view_gem(master_frame_gem, listbox_gem_gem)
    listbox_gem_object = tkattrs.get_tkobject(listbox_gem_gem)
    listbox_gem_object.delete(0, "end")
    selected_gem_base_names = []
    cluster_gem = global_ids_query.get_cluster_by_cluster_name(selected_cluster_name)
    load_gems(cluster_gem, listbox_gem_object, "")
    gem_index = base.findin(selected_gem_base_names, selected_gem_base_name)
    if gem_index is None:
        gem_index = 0
    selected_listbox_gem_index = gem_index
    listbox_gem_object.select_set(selected_listbox_gem_index)
    listbox_gem_object.see(selected_listbox_gem_index)


def listbox_gem_selection(listbox_gem_gem: base.Gem, event: any) -> None:
    print(125, "todo")


def listbox_facet_selection(listbox_facet_gem: base.Gem, event: any) -> None:
    print(129, "todo")


def entry_name_return(entry_name_gem: base.Gem, event: any) -> None:
    button_name_function(entry_name_gem)


def button_name_function(entry_name_gem: base.Gem) -> None:
    print(124, "todo")


def init_pdml_text(text_gem: base.Gem) -> None:
    global selected_gem_base_name
    cluster = attrs_query.get_cluster(text_gem)
    if cluster is None:
        return
    facet_state_gem = local_ids_query.cluster_get_gem_by_gem_base_name(cluster, "FacetState")
    tkcore.tk_destroy(facet_state_gem)
    parent_gem = attrs_query.get_gem_parent(text_gem)
    tkattrs.set_view_gem(parent_gem, text_gem)
    gem = global_ids_query.get_gem(selected_gem_base_name, text_gem)
    if gem is None:
        return
    text_object = tkattrs.get_tkobject(text_gem)
    text_object.delete("1.0", "end")
    s = saver.data_to_string(0, gem, False)
    text_object.insert("1.0", s)
    text_object.see("1.0")


def init_listbox_facet(listbox_facet_gem: base.Gem) -> None:
    global selected_gem_name
    global selected_facet_names
    global selected_facet_name
    global selected_listbox_facet_index

    facet_state_gem = global_ids_query.get_gem(".FacetState", listbox_facet_gem)
#    facet_state_object = build.get_attr(facet_state_gem, "#tk_object")
#    if facet_state_object is None:
#        tkgems.tk_eval(facet_state_gem)
#        facet_state_object = build.get_attr(facet_state_gem, "#tk_object")
#    master_frame_name = build.get_aggregate_tag(listbox_facet_gem, "master_frame")
#    master_frame_gem = build.get_gem(master_frame_name, listbox_facet_gem)
#    build.set_attr(master_frame_gem, "#view_gem", listbox_facet_gem)
#    listbox_facet_gem_object = build.get_attr(listbox_facet_gem, "#tk_object")
#    listbox_facet_gem_object.delete(0, "end")
#    gem_gem = build.get_gem(selected_gem_name)
#    selected_facet_names = []
#    if gem_gem is not None:
#        for facet_name in sorted(gem_gem):
#            selected_facet_names.append(facet_name)
#            listbox_facet_gem_object.insert("end", facet_name)
#    if selected_facet_name is None:
#        facet_state_object.config(text="No Facet Selected")
#        facet_index = None
#    else:
#        facet_index = build.findin(selected_facet_names, selected_facet_name)
#        if facet_index is None:
#            facet_state_object.config(text="No matching Facet: " + selected_facet_name)
#        else:
#            facet_state_object.config(text="")
#    selected_listbox_facet_index = facet_index
#    if facet_index is None:
#        listbox_facet_gem_object.see(0)
#    else:
#        listbox_facet_gem_object.select_set(selected_listbox_facet_index)
#        listbox_facet_gem_object.see(selected_listbox_facet_index)
#    facet_text_gem = build.get_gem(".TextFacet", listbox_facet_gem)
#    init_facet_text(facet_text_gem)
    print(120, "todo")


def init_facet_text(facet_text_gem: base.Gem) -> None:
    print(130, "todo")


def create_viewer_resource_gems() -> None:
    core.make_resource_function_gem("viewer-init_listbox_cluster", init_listbox_cluster)
    core.make_resource_function_gem("viewer-listbox_cluster_selection", listbox_cluster_selection)
    core.make_resource_function_gem("viewer-gems_radiobutton_clicked", gems_radiobutton_clicked)
    core.make_resource_function_gem("viewer-content_radiobutton_clicked", content_radiobutton_clicked)
    core.make_resource_function_gem("viewer-init_listbox_gem", init_listbox_gem)
    core.make_resource_function_gem("viewer-init_listbox_gem_tree", init_listbox_gem_tree)
    core.make_resource_function_gem("viewer-listbox_gem_selection", listbox_gem_selection)
    core.make_resource_function_gem("viewer-entry_name_return", entry_name_return)
    core.make_resource_function_gem("viewer-button_name_function", button_name_function)
    core.make_resource_function_gem("viewer-init_pdml_text", init_pdml_text)
    core.make_resource_function_gem("viewer-init_listbox_facet", init_listbox_facet)
    core.make_resource_function_gem("viewer-listbox_facet_selection", listbox_facet_selection)
    core.make_resource_function_gem("viewer-init_facet_text", init_facet_text)


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
    if viewer_cluster is None:
        print("viewer_cluster is None")
        return
    window_gem = local_ids_query.cluster_get_gem_by_gem_base_name(viewer_cluster, "RootWindow")
    if window_gem is None:
        print("window_gem is None")
        return
    window = tkcore.tkeval(window_gem)
    window.mainloop()


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    initialize(home_path)
