import pathlib
import typing

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


def initialize(home_path: pathlib.Path) -> None:
    pass
