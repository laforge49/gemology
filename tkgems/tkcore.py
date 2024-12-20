import copy
import pathlib
import typing
import tkinter as tk
from tkinter import ttk

from gems import base, core
from gems.core import make_gem
from gems.facets import attrs_query, global_ids_query, gems_query
from pdml import saver
from tkgems.tkfacets import tkattrs, tkglobal_tags


def make_tkdescriptor_gem(descriptor_name: str, tkcomposer: typing.Callable, is_widget: bool, packable: bool)\
        -> dict:
    aggregate = base.get_aggregate()
    resources = make_gem(aggregate, aggregate, "Resources")
    tkdescriptors_gem = make_gem(aggregate, resources, descriptor_name.split(".")[0])
    tkdescriptor_gem = make_gem(aggregate, tkdescriptors_gem, descriptor_name)
    tkattrs.set_tkcomposer(tkdescriptor_gem, tkcomposer)
    tkattrs.set_is_widget(tkdescriptor_gem, is_widget)
    tkattrs.set_packable(tkdescriptor_gem, packable)
    return tkdescriptor_gem


def initialize_tkdescriptors() -> None:
    make_tkdescriptor_gem("TkDescriptor.tklistbox", tk.Listbox, True, True)
    make_tkdescriptor_gem("TkDescriptor.tkradiobutton", tk.Radiobutton, True, True)
    make_tkdescriptor_gem("TkDescriptor.tkstringvar", tk.StringVar, False, False)
    make_tkdescriptor_gem("TkDescriptor.tktext", tk.Text, True, True)
    make_tkdescriptor_gem("TkDescriptor.tkwindow", tk.Tk, True, False)
    make_tkdescriptor_gem("TkDescriptor.ttkbutton", ttk.Button, True, True)
    make_tkdescriptor_gem("TkDescriptor.ttkentry", ttk.Entry, True, True)
    make_tkdescriptor_gem("TkDescriptor.ttkframe", ttk.Frame, True, True)
    make_tkdescriptor_gem("TkDescriptor.ttklabel", ttk.Label, True, True)
    make_tkdescriptor_gem("TkDescriptor.ttkscrollbar", ttk.Scrollbar, True, True)


def get_tkdescriptor_gem(tkgem: dict) -> dict | None:
    tktype = tkglobal_tags.get_tktype(tkgem)
    if tktype is None:
        return None
    return core.get_resource_gem(tktype)


def persist_value(tk_gem: dict) -> None:
    pass


def center_window(window, width, height):
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def create_window(widget_gem: dict) -> None:
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


def listbox_up_down(listbox_gem: dict, event: any) -> None:
    pass

def create_tkresource_gems() -> None:
    core.create_resource_gem("tkcore.persist_value", persist_value)
    core.create_resource_gem("tkcore.create_window", create_window)
    core.create_resource_gem("tkcore.listbox_up_down", listbox_up_down)


def initialize(home_path: pathlib.Path) -> None:
    initialize_tkdescriptors()
    create_tkresource_gems()


def do_tkoptions(tkgem: dict) -> dict:
    options = tkattrs.get_options(tkgem)
    if options is None:
        options = {}
    else:
        options = copy.deepcopy(options)
    # todo variable options
    return options


def tklayout(packable: bool, tkgem: dict, tkobject: any) -> None:
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


def tkinit_func(tkgem: dict) -> None:
    func_name = tkglobal_tags.get_init_tkgem(tkgem)
    if func_name is not None:
        func = core.get_resource_function(func_name)
        func(tkgem)


def tkevents(tkgem: dict, tkobject: any) -> None:
    # todo tklayout
    pass


def tkscroll(scrollbar_gem: dict, scrollbar_object: any) -> None:
    # todo tklayout
    pass


def tkeval(tkgem: dict) -> any:
    if tkgem is None:
        return None
    parent_gem = attrs_query.get_gem_parent(tkgem)
    parent_tkobject = tkattrs.get_tkobject(parent_gem)
    tkdescriptor_gem = get_tkdescriptor_gem(tkgem)
    if tkdescriptor_gem is None:
       return None
    tkcomposer = tkattrs.get_tkcomposer(tkdescriptor_gem)
    tkoptions = do_tkoptions(tkgem)
    tkobject = tkcomposer(parent_tkobject, **tkoptions)
    tkattrs.set_tkobject(tkgem, tkobject)
    packable = tkattrs.get_packable(tkdescriptor_gem)
    tklayout(packable, tkgem, tkobject)
    tkinit_func(tkgem)
    tkevents(tkgem, tkobject)
    tkscroll(tkgem, tkobject)
    gf = gems_query.get_gf(tkgem)
    if gf is not None:
        for child_gem in gf:
            manual = tkattrs.get_manual(child_gem)
            if not manual:
                tkeval(child_gem)
    return tkobject
