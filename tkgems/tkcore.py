import copy
import pathlib
from typing import *
import tkinter as tk
from tkinter import ttk

from gems import base, core
from gems.facets import attrs_query, global_ids_query, gems_query
from tkgems.tkfacets import tkattrs, tkglobal_tags


def make_tkdescriptor_gem(descriptor_name: str, tkcomposer: type, is_widget: bool, packable: bool)\
        -> dict:
    resource_gem = core.make_resource_type_gem(descriptor_name, tkcomposer)
    assert isinstance(resource_gem, base.Resource)
    tkattrs.set_is_widget(resource_gem, is_widget)
    tkattrs.set_packable(resource_gem, packable)
    return resource_gem


def initialize_tkdescriptors() -> None:
    make_tkdescriptor_gem("TkDescriptor-tklistbox", tk.Listbox, True, True)
    make_tkdescriptor_gem("TkDescriptor-tkradiobutton", tk.Radiobutton, True, True)
    make_tkdescriptor_gem("TkDescriptor-tkstringvar", tk.StringVar, False, False)
    make_tkdescriptor_gem("TkDescriptor-tktext", tk.Text, True, True)
    make_tkdescriptor_gem("TkDescriptor-tkwindow", tk.Tk, True, False)
    make_tkdescriptor_gem("TkDescriptor-ttkbutton", ttk.Button, True, True)
    make_tkdescriptor_gem("TkDescriptor-ttkentry", ttk.Entry, True, True)
    make_tkdescriptor_gem("TkDescriptor-ttkframe", ttk.Frame, True, True)
    make_tkdescriptor_gem("TkDescriptor-ttklabel", ttk.Label, True, True)
    make_tkdescriptor_gem("TkDescriptor-ttkscrollbar", ttk.Scrollbar, True, True)


def get_tkdescriptor_gem(tkgem: base.Gem) -> Optional[base.Gem]:
    tktype = tkglobal_tags.get_tktype(tkgem)
    if tktype is None:
        return None
    return core.get_resource_gem(tktype)


def center_window(window, width, height):
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def create_window(widget_gem: base.Gem) -> None:
    window = tkattrs.get_tkobject(widget_gem)
    root_window_title = tkattrs.get_title(widget_gem)
    if root_window_title is None:
        cluster = attrs_query.get_cluster(widget_gem)
        root_window_title = global_ids_query.get_cluster_name(cluster)
    window.title(root_window_title)
    root_window_geometry = tkattrs.get_geometry(widget_gem)
    width = tkattrs.get_tkwidth(widget_gem)
    height = tkattrs.get_tkheight(widget_gem)
    if root_window_geometry is None:
        center_window(window, width, height)
    window.geometry(root_window_geometry)


def listbox_up_down(listbox_gem: base.Gem, event: any) -> None:
    listbox_object = tkattrs.get_tkobject(listbox_gem)
    index = listbox_object.curselection()[0]
    if event.keysym == 'Up':
        index -= 1
    elif event.keysym == 'Down':
        index += 1
    if 0 <= index < listbox_object.size():
        listbox_object.selection_clear(0, tk.END)
        listbox_object.select_set(index)
        listbox_object.see(index)
    tkevent(listbox_gem, None, "<<ListboxSelect>>")

def create_tkresource_gems() -> None:
    core.make_resource_function_gem("tkcore-create_window", create_window)
    core.make_resource_function_gem("tkcore-listbox_up_down", listbox_up_down)


def initialize(home_path: pathlib.Path) -> None:
    initialize_tkdescriptors()
    create_tkresource_gems()


def tk_destroy(tk_gem: base.Gem) -> None:
    if tk_gem is None:
        return
    tk_object = tkattrs.del_tkobject(tk_gem)
    if tk_object is None:
        return
    tk_object.destroy()
    gems_facet = gems_query.get_gf(tk_gem)
    if gems_facet is None:
        return
    for gem in gems_facet:
        tk_destroy(gem)


def do_tkoptions(tkgem: base.Gem) -> dict:
    options = tkattrs.get_options(tkgem)
    if options is None:
        options = {}
    else:
        options = copy.deepcopy(options)
    var_object = tkattrs.get_tkobject(tkglobal_tags.resolve_VariableGemName(tkgem))
    if var_object is not None:
        options["variable"] = var_object
    textvar_object = tkattrs.get_tkobject(tkglobal_tags.resolve_TextVariableGemName(tkgem))
    if textvar_object is not None:
        options["textvariable"] = textvar_object
    listvar_object = tkattrs.get_tkobject(tkglobal_tags.resolve_ListVariableGemName(tkgem))
    if listvar_object is not None:
        options["listvariable"] = listvar_object
    command_name = tkglobal_tags.get_command(tkgem)
    if command_name is not None:
        func = core.get_resource_function(command_name)
        if func is None:
            print(222, command_name)
        options["command"] = lambda: func(tkgem)
    return options


def tklayout(packable: bool, tkgem: base.Gem, tkobject: any) -> None:
    columns = tkattrs.get_columns(tkgem)
    if columns is not None:
        for column in columns:
            tkobject.columnconfigure(**column)
    rows = tkattrs.get_rows(tkgem)
    if rows is not None:
        for row in rows:
            tkobject.rowconfigure(**row)
    if packable:
        grid = tkattrs.get_grid(tkgem)
        if grid is not None:
            tkobject.grid(**grid)
        else:
            pack = tkattrs.get_pack(tkgem)
            if pack is None:
                pack = {}
            tkobject.pack(**pack)


def tkinit_func(tkgem: base.Gem) -> None:
    func_name = tkglobal_tags.get_init_tkgem(tkgem)
    if func_name is not None:
        func = core.get_resource_function(func_name)
        func(tkgem)


def tkevent(tkgem: base.Gem, event: any, tag_name: str) -> None:
    events = tkattrs.get_events(tkgem)
    if events is None:
        event_function_name = None
    else:
        event_function_name = events.get(tag_name)
    if event_function_name is not None:
        func = core.get_resource_function(event_function_name)
        if func:
            func(tkgem, event)


def tkevents(tkgem: base.Gem, tkobject: any) -> None:
    events = tkattrs.get_events(tkgem)
    if events is not None:
        for event_name, event_function_name in events.items():
            func = core.get_resource_function(event_function_name)
            if func is None:
                print(987, event_function_name)
            tkobject.bind(event_name, lambda event: func(tkgem, event))


def tkscroll(scrollbar_gem: base.Gem, scrollbar_object: any, tkoptions: dict) -> None:
    orient = tkoptions.get("orient")
    scrolling_object = tkattrs.get_tkobject(tkglobal_tags.resolve_ScrollingGemName(scrollbar_gem))
    if scrolling_object is None:
        return
    # scrollbar_object["command"] = scrolling_object
    if orient == "vertical":
        scrollbar_object["command"] = scrolling_object.yview
        scrolling_object["yscrollcommand"] = scrollbar_object.set
    elif orient == "horizontal":
        scrollbar_object["command"] = scrolling_object.xview
        scrolling_object["xscrollcommand"] = scrollbar_object.set


def tkeval(tkgem: base.Gem) -> any:
    if tkgem is None:
        return None
    parent_gem = attrs_query.get_gem_parent(tkgem)
    parent_tkobject = tkattrs.get_tkobject(parent_gem)
    tkdescriptor_gem = get_tkdescriptor_gem(tkgem)
    if tkdescriptor_gem is None:
       return None
    tkcomposer = attrs_query.get_type(tkdescriptor_gem)
    tkoptions = do_tkoptions(tkgem)
    tkobject = tkcomposer(parent_tkobject, **tkoptions)
    tkattrs.set_tkobject(tkgem, tkobject)
    packable = tkattrs.get_packable(tkdescriptor_gem)
    tklayout(packable, tkgem, tkobject)
    tkinit_func(tkgem)
    tkevents(tkgem, tkobject)
    tkscroll(tkgem, tkobject, tkoptions)
    gf = gems_query.get_gf(tkgem)
    if gf is not None:
        for child_gem in gf:
            manual = tkattrs.get_manual(child_gem)
            if not manual:
                tkeval(child_gem)
    return tkobject
