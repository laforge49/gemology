from typing import *
import pathlib
import tkinter


from gems import core, base
from gems.facets import local_ids_query, global_ids_query, gems_query, attrs_query
from pdml import saver
from tkgems import tkcore
from tkgems.tkfacets import tkattrs, tkglobal_tags


window_gem: base.Gem
selected_listbox_cluster_index: int | None = 0
selected_listbox_gem_index: int | None = 0
selected_gem_names: list = []
selected_gem_full_name = base.GemFullName("Aggregate")
selected_gems_frame = base.GemName(".FrameGemsList")
selected_content_frame = base.GemName(".FramePdml")
selected_facet_names: list = []
selected_facet_name: str | None = None
selected_listbox_facet_index: int | None = None


def get_selected_cluster_name() -> Optional[base.ClusterName]:
    global selected_gem_full_name
    return base.gem_full_name_to_cluster_name(selected_gem_full_name)


def get_selected_gem_name() -> Optional[base.GemName]:
    global selected_gem_full_name
    return base.gem_full_name_to_gem_name(selected_gem_full_name)


def init_listbox_cluster(listbox_cluster_gem: base.Gem) -> None:
    global selected_listbox_cluster_index
    global selected_gem_full_name
    listbox_cluster_object = tkattrs.get_tkobject(listbox_cluster_gem)
    listbox_cluster_object.insert("end", "Aggregate")
    for cluster_name in sorted(global_ids_query.aggregate_get_cluster_names()):
        listbox_cluster_object.insert("end", cluster_name)
    listbox_cluster_object.select_set(0)
    selected_listbox_cluster_index = 0
    selected_gem_full_name = base.GemFullName("Aggregate")
    listbox_cluster_object.see(0)


def listbox_cluster_selection(listbox_cluster_gem: base.Gem, event: any) -> None:
    global selected_listbox_cluster_index
    global selected_gem_full_name
    label_error_gem = global_ids_query.get_gem(base.GemName(".LabelError"), listbox_cluster_gem)
    label_error_object = tkattrs.get_tkobject(label_error_gem)
    label_error_object["text"] = ""
    listbox_cluster_object = tkattrs.get_tkobject(listbox_cluster_gem)
    cluster_indexes = listbox_cluster_object.curselection()
    cluster_index = cluster_indexes[0]
    cluster_name = listbox_cluster_object.get(cluster_index)
    sv_name_gem = global_ids_query.get_gem(base.GemName(".StringVarName"), listbox_cluster_gem)
    sv_name_object = tkattrs.get_tkobject(sv_name_gem)
    sv_name_object.set(cluster_name)
    selected_listbox_cluster_index = cluster_index
    selected_gem_full_name = cluster_name
    init_gems_view(listbox_cluster_gem)
    init_content_view(listbox_cluster_gem)


def init_content_view(tk_gem: base.Gem) -> None:
    global selected_content_frame
    frame_gem = global_ids_query.get_gem(selected_content_frame, tk_gem)
    if frame_gem is None:
        return
    view_gem = tkattrs.get_view_gem(frame_gem)
    tkcore.tkinit_func(view_gem)


def init_gems_view(tk_gem: base.Gem) -> None:
    global selected_gems_frame
    frame_gem = global_ids_query.get_gem(selected_gems_frame, tk_gem)
    if frame_gem is None:
        return
    view_gem = tkattrs.get_view_gem(frame_gem)
    tkcore.tkinit_func(view_gem)


def load_gems(tk_gem: base.Gem, listbox_gem_object: any, prefix: str = "") -> None:
    global selected_gem_names
    gem_name = core.get_gem_name(tk_gem)
    selected_gem_names.append(gem_name)
    listbox_gem_object.insert("end", prefix + gem_name)
    gemsfacet: base.GemsFacet = gems_query.get_gf(tk_gem)
    if gemsfacet is None:
        return
    for gem in gemsfacet:
        load_gems(gem, listbox_gem_object, prefix + "+")


def gems_radiobutton_clicked(gems_radiobutton_gem: base.Gem) -> None:
    global selected_gems_frame
    value = tkattrs.get_options(gems_radiobutton_gem)["value"]
    if value == selected_gems_frame:
        return
    frame_gem = global_ids_query.get_gem(selected_gems_frame, gems_radiobutton_gem)
    tkcore.tk_destroy(frame_gem)
    selected_gems_frame = value
    frame_gem = global_ids_query.get_gem(selected_gems_frame, gems_radiobutton_gem)
    tkcore.tkeval(frame_gem)


def content_radiobutton_clicked(content_radiobutton_gem: base.Gem) -> None:
    global selected_content_frame
    value = tkattrs.get_options(content_radiobutton_gem)["value"]
    if value == selected_content_frame:
        return
    frame_gem = global_ids_query.get_gem(selected_content_frame, content_radiobutton_gem)
    tkcore.tk_destroy(frame_gem)
    selected_content_frame = value
    frame_gem = global_ids_query.get_gem(selected_content_frame, content_radiobutton_gem)
    tkcore.tkeval(frame_gem)


def init_listbox_gem(listbox_gem_gem: base.Gem):
    global selected_listbox_gem_index
    global selected_gem_names
    master_frame_gem = tkglobal_tags.resolve_master_frame_GemName(listbox_gem_gem)
    tkattrs.set_view_gem(master_frame_gem, listbox_gem_gem)
    listbox_gem_object = tkattrs.get_tkobject(listbox_gem_gem)
    listbox_gem_object.delete(0, "end")
    selected_gem_names = [get_selected_cluster_name()]
    cluster_gem = global_ids_query.get_cluster_by_cluster_name(get_selected_cluster_name())
    gem_base_names = local_ids_query.cluster_get_gem_base_names(cluster_gem)
    if gem_base_names is not None:
        for gem_name in sorted(gem_base_names):
            selected_gem_names.append("." + gem_name)
    for gem_name in selected_gem_names:
        listbox_gem_object.insert("end", gem_name)
    gem_index = base.findin(selected_gem_names, get_selected_gem_name())
    if gem_index is None:
        gem_index = 0
    selected_listbox_gem_index = gem_index
    listbox_gem_object.select_set(selected_listbox_gem_index)
    listbox_gem_object.see(selected_listbox_gem_index)


def init_listbox_gem_tree(listbox_gem_gem: base.Gem):
    global selected_listbox_gem_index
    global selected_gem_names
    master_frame_gem = tkglobal_tags.resolve_master_frame_GemName(listbox_gem_gem)
    tkattrs.set_view_gem(master_frame_gem, listbox_gem_gem)
    listbox_gem_object = tkattrs.get_tkobject(listbox_gem_gem)
    listbox_gem_object.delete(0, "end")
    selected_gem_names = []
    cluster_gem = global_ids_query.get_cluster_by_cluster_name(get_selected_cluster_name())
    load_gems(cluster_gem, listbox_gem_object, "")
    gem_index = base.findin(selected_gem_names, get_selected_gem_name())
    if gem_index is None:
        gem_index = 0
    selected_listbox_gem_index = gem_index
    listbox_gem_object.select_set(selected_listbox_gem_index)
    listbox_gem_object.see(selected_listbox_gem_index)


def listbox_gem_selection(listbox_gem_gem: base.Gem, event: any) -> None:
    global selected_listbox_gem_index
    global selected_gem_full_name
    global selected_gem_names
    label_error_gem = global_ids_query.get_gem(base.GemName(".LabelError"), listbox_gem_gem)
    label_error_object = tkattrs.get_tkobject(label_error_gem)
    label_error_object["text"] = ""
    listbox_gem_object = tkattrs.get_tkobject(listbox_gem_gem)
    gem_indexes = listbox_gem_object.curselection()
    gem_index = gem_indexes[0]
    gem_name = base.GemName(selected_gem_names[gem_index])
    sv_name_gem = global_ids_query.get_gem(base.GemName(".StringVarName"), listbox_gem_gem)
    sv_name_object = tkattrs.get_tkobject(sv_name_gem)
    if get_selected_cluster_name() == gem_name:
        selected_gem_full_name = base.GemFullName(get_selected_cluster_name())
        sv_name_object.set(selected_gem_full_name)
    else:
        selected_gem_full_name = get_selected_cluster_name() + gem_name
        sv_name_object.set(selected_gem_full_name)
    selected_listbox_gem_index = gem_index
    init_content_view(listbox_gem_gem)


def listbox_facet_selection(listbox_facet_gem: base.Gem, event: any) -> None:
    global selected_facet_names
    global selected_facet_name
    global selected_listbox_facet_index
    listbox_facet_object = tkattrs.get_tkobject(listbox_facet_gem)
    facet_indexes = listbox_facet_object.curselection()
    facet_index = facet_indexes[0]
    facet_name = selected_facet_names[facet_index]
    selected_listbox_facet_index = facet_index
    selected_facet_name = facet_name
    facet_state_gem = global_ids_query.get_gem(base.GemName(".FacetState"), listbox_facet_gem)
    facet_state_object = tkattrs.get_tkobject(facet_state_gem)
    facet_state_object.config(text="")
    facet_text_gem = global_ids_query.get_gem(base.GemName(".TextFacet"), listbox_facet_gem)
    init_facet_text(facet_text_gem)


def entry_name_return(entry_name_gem: base.Gem, event: any) -> None:
    button_name_function(entry_name_gem)


def button_name_function(entry_name_gem: base.Gem) -> None:
    sv_name_gem = global_ids_query.get_gem(base.GemName(".StringVarName"), entry_name_gem)
    sv_name_object = tkattrs.get_tkobject(sv_name_gem)
    gem_full_name = sv_name_object.get()
    select_gem(gem_full_name)


def select_gem(gem_full_name: base.GemFullName, event: Optional[any] = None) -> None:
    global selected_listbox_cluster_index
    global selected_gem_names
    global selected_listbox_gem_index
    global selected_gem_full_name
    label_error_gem = global_ids_query.get_gem(base.GemName(".LabelError"), window_gem)
    label_error_object = tkattrs.get_tkobject(label_error_gem)
    if gem_full_name.endswith("."):
        label_error_object["text"] = "Improper name."
        return
    dot_index = base.findin(gem_full_name, ".")
    if dot_index is None:
        cluster_name = gem_full_name
        gem_name = gem_full_name
    else:
        cluster_name = gem_full_name[:dot_index]
        gem_name = gem_full_name[dot_index:]
    listbox_cluster_gem = global_ids_query.get_gem(base.GemName(".ListBoxCluster"), window_gem)
    listbox_cluster_object = tkattrs.get_tkobject(listbox_cluster_gem)
    cluster_names = listbox_cluster_object.get(0, "end")
    cluster_index = base.findin(cluster_names, cluster_name)
    if cluster_index is None:
        label_error_object["text"] = "Unknown cluster."
        return
    label_error_object["text"] = ""
    listbox_cluster_object.selection_clear(0, "end")
    listbox_cluster_object.selection_set(cluster_index)
    if get_selected_cluster_name() != cluster_name:
        selected_gem_full_name = gem_full_name
        selected_listbox_cluster_index = cluster_index
        print(444, cluster_index)
        init_gems_view(window_gem)
        selected_listbox_gem_index = 0
    else:
        selected_gem_full_name = gem_full_name
    gem_index = base.findin(selected_gem_names, gem_name)
    if gem_index is None:
        print(gem_name)
        print(selected_gem_names)
        label_error_object["text"] = "Unknown gem name."
        return
    selected_listbox_gem_index = gem_index
    listbox_view_gem = get_listbox_view_gem(window_gem)
    listbox_view_object = tkattrs.get_tkobject(listbox_view_gem)
    listbox_view_object.selection_clear(0, "end")
    listbox_view_object.select_set(selected_listbox_gem_index)
    listbox_view_object.see(selected_listbox_gem_index)
    init_content_view(window_gem)


def get_listbox_view_gem(tk_gem: base.Gem) -> Optional[base.Gem]:
    frame_gem = global_ids_query.get_gem(selected_gems_frame, tk_gem)
    if frame_gem is None:
        return None
    view_gem = tkattrs.get_view_gem(frame_gem)
    return view_gem


def init_pdml_text(text_gem: base.Gem) -> None:
    global selected_gem_full_name
    cluster = attrs_query.get_cluster(text_gem)
    if cluster is None:
        return
    facet_state_gem = local_ids_query.cluster_get_gem_by_gem_base_name(cluster, base.GemBaseName("FacetState"))
    tkcore.tk_destroy(facet_state_gem)
    parent_gem = attrs_query.get_gem_parent(text_gem)
    tkattrs.set_view_gem(parent_gem, text_gem)
    gem = global_ids_query.get_gem(selected_gem_full_name)
    if gem is None:
        return
    text_object = tkattrs.get_tkobject(text_gem)
    text_object.delete("1.0", "end")
    s = saver.data_to_string(0, gem, False)
    text_object.insert("1.0", s)
    text_object.see("1.0")


def init_listbox_facet(listbox_facet_gem: base.Gem) -> None:
    global selected_gem_full_name
    global selected_facet_names
    global selected_facet_name
    global selected_listbox_facet_index

    facet_state_gem = global_ids_query.get_gem(base.GemName(".FacetState"), listbox_facet_gem)
    facet_state_object = tkattrs.get_tkobject(facet_state_gem)
    if facet_state_object is None:
        tkcore.tkeval(facet_state_gem)
        facet_state_object = tkattrs.get_tkobject(facet_state_gem)
    master_frame_gem = tkglobal_tags.resolve_master_frame_GemName(listbox_facet_gem)
    tkattrs.set_view_gem(master_frame_gem, listbox_facet_gem)
    listbox_facet_gem_object = tkattrs.get_tkobject(listbox_facet_gem)
    listbox_facet_gem_object.delete(0, "end")
    gem_gem = global_ids_query.get_gem(selected_gem_full_name)
    selected_facet_names = []
    if gem_gem is not None:
        for facet_name in sorted(gem_gem):
            selected_facet_names.append(facet_name)
            listbox_facet_gem_object.insert("end", facet_name)
    if selected_facet_name is None:
        facet_state_object.config(text="No Facet Selected")
        facet_index = None
    else:
        facet_index = base.findin(selected_facet_names, selected_facet_name)
        if facet_index is None:
            facet_state_object.config(text="No matching Facet: " + selected_facet_name)
        else:
            facet_state_object.config(text="")
    selected_listbox_facet_index = facet_index
    if facet_index is None:
        listbox_facet_gem_object.see(0)
    else:
        listbox_facet_gem_object.select_set(selected_listbox_facet_index)
        listbox_facet_gem_object.see(selected_listbox_facet_index)
    facet_text_gem = global_ids_query.get_gem(base.GemName(".TextFacet"), listbox_facet_gem)
    init_facet_text(facet_text_gem)


def reset_text_object(text_object) -> None:
    if text_object is None:
        return
    text_object.delete("1.0", "end")
    tags = text_object.tag_names()
    for tag in tags:
        text_object.tag_remove(tag, "1.0", "end")
    text_object.mark_set("insert", "1.0")


def default_facet_display(facet, text_object) -> None:
    s = saver.data_to_string(0, facet, False)
    text_object.insert("1.0", s)
    text_object.see("1.0")


def change_cursor(gems: list, event) -> None:
    index = event.widget.index(tkinter.CURRENT)
    line, column = map(int, index.split('.'))
    if line > len(gems):
        event.widget.config(cursor="arrow")
    else:
        event.widget.config(cursor="hand2")


def gems_facet_display(gems: list, text_object) -> None:
    text_object.bind("<Motion>", lambda event: change_cursor(gems, event))
    for gem in gems:
        gem_base_name = local_ids_query.get_gem_base_name(gem)
        gem_name = base.GemName("." + gem_base_name)
        gem_full_name = global_ids_query.expand_gem_name(gem, gem_name)
        text_object.tag_config(gem_base_name, foreground="blue", underline=True)
        text_object.insert("end", gem_full_name + "\n", gem_base_name)
        text_object.tag_bind(gem_base_name, "<Button-1>",
                             lambda event: select_gem(base.GemFullName(gem_full_name), event))


def init_facet_text(facet_text_gem: base.Gem) -> None:
    global selected_gem_full_name
    global selected_facet_name
    gem = global_ids_query.get_gem(selected_gem_full_name, facet_text_gem)
    text_object = tkattrs.get_tkobject(facet_text_gem)
    reset_text_object(text_object)
    if selected_facet_name is None:
        return
    facet = gem.get(selected_facet_name)
    if facet is None:
        return
    match selected_facet_name:
        case "GemsFacet":
            gems_facet_display(facet, text_object)
        case _:
            default_facet_display(facet, text_object)


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
    global window_gem
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
    window_gem = local_ids_query.cluster_get_gem_by_gem_base_name(viewer_cluster, base.GemBaseName("RootWindow"))
    if window_gem is None:
        print("window_gem is None")
        return
    window = tkcore.tkeval(window_gem)
    window.mainloop()


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    initialize(home_path)
