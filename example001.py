#from pathlib import Path
from solid2 import cube
#from jupyterscad import view
import subprocess

def save_as_stl():
    subprocess.call(["C:\\Users\\Mohan\\scoop\\apps\\openscad-dev\\current\\openscad.exe", "-o", "example001.stl", "example001.scad"])
    
part = cube(3)
part.save_as_scad()
save_as_stl()



