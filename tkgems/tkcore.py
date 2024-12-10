import pathlib

from gems import base
from gems.core import make_gem


def make_tkdescriptor_gem(descriptor_name: str) -> dict:
    aggregate = base.get_aggregate()
    resources = make_gem(aggregate, aggregate, "Resources")
    tkdescriptors_gem = make_gem(aggregate, resources, "TkDescriptors")
    tkdescriptor_gem = make_gem(aggregate, tkdescriptors_gem, descriptor_name)


def initialize(home_path: pathlib.Path) -> None:
    pass
