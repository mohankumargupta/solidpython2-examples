import subprocess
from pathlib import Path
import sys

openscad_location = "C:\\Users\\Mohan\\scoop\\apps\\openscad-dev\\current\\openscad.exe"

def root_name():
    filename_without_extension = Path(sys.argv[0]).with_suffix('').name
    return filename_without_extension

def save_as_scad(part, name):
    part.save_as_scad(f"{name}.scad")


def save_as_stl(name):
    subprocess.call([openscad_location, "-o", f"{name}.stl", "example001.scad"])

def save_as_scad_and_stl(part):
    root = root_name()
    save_as_scad(part, root)
    save_as_stl(root)
    
