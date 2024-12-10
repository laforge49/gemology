import pathlib

from gems import core
from tkgems import tkcore


def initialize(home_path: pathlib.Path) -> None:
    print()
    print("*** start viewer ***")
    print("home path:", home_path)
    viewer_pdml_path = home_path / "viewer.pdml"
    print("viewer.pdml path:", viewer_pdml_path)
    core.initialize(home_path)
    tkcore.initialize(home_path)
    viewer_cluster = core.load(viewer_pdml_path)
    print()


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    initialize(home_path)
