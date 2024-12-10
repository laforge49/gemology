import pathlib
import typing
import tkinter as tk
from tkinter import ttk

from gems import base
from gems.core import make_gem
from tkgems.tkfacets import tkattrs


def make_tkdescriptor_gem(descriptor_name: str, tkcomposer: typing.Callable, is_widget: bool, packable: bool)\
        -> dict:
    aggregate = base.get_aggregate()
    resources = make_gem(aggregate, aggregate, "Resources")
    tkdescriptors_gem = make_gem(aggregate, resources, "TkDescriptors")
    tkdescriptor_gem = make_gem(aggregate, tkdescriptors_gem, descriptor_name)
    tkattrs.set_tkcomposer(tkdescriptor_gem, tkcomposer)
    tkattrs.set_is_widget(tkdescriptor_gem, is_widget)
    tkattrs.set_packable(tkdescriptor_gem, packable)


def initialize_tkdescriptors() -> None:
    make_tkdescriptor_gem("tklistbox", tk.Listbox, True, True)
    make_tkdescriptor_gem("tkradiobutton", tk.Radiobutton, True, True)
    make_tkdescriptor_gem("tkstringvar", tk.StringVar, False, False)
    make_tkdescriptor_gem("tktext", tk.Text, True, True)
    make_tkdescriptor_gem("tkwindow", tk.Tk, True, False)
    make_tkdescriptor_gem("ttkbutton", ttk.Button, True, True)
    make_tkdescriptor_gem("ttkentry", ttk.Entry, True, True)
    make_tkdescriptor_gem("ttkframe", ttk.Frame, True, True)
    make_tkdescriptor_gem("ttklabel", ttk.Label, True, True)
    make_tkdescriptor_gem("ttkscrollbar", ttk.Scrollbar, True, True)


def create_window(widget_gem: dict) -> None:
    pass


def initialize(home_path: pathlib.Path) -> None:
    initialize_tkdescriptors()
