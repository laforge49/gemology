import pathlib
import typing
import tkinter as tk
from tkinter import ttk

from gems import base, core
from gems.core import make_gem
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


def get_tkdescriptor_gem(tkgem: dict)-> dict:
    tktype = tkglobal_tags.get_tktype(tkgem)
    if tktype is None:
        return None
    return core.get_resource_gem(tktype)


def persist_value(tk_gem: dict) -> None:
    pass


def create_window(widget_gem: dict) -> None:
    pass


def listbox_up_down(listbox_gem: dict, event: any) -> None:
    pass

def create_tkresource_gems() -> None:
    core.create_resource_gem("tkcore.persist_value", persist_value)
    core.create_resource_gem("tkcore.create_window", create_window)
    core.create_resource_gem("tkcore.listbox_up_down", listbox_up_down)


def initialize(home_path: pathlib.Path) -> None:
    initialize_tkdescriptors()
