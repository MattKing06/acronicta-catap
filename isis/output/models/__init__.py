import CATAP.config as cfg
from CATAP.common.machine.area import MachineArea
from collections import namedtuple
import os


if os.path.exists("/home/mattking/jinja-catap/isis/output/yaml"):
    cfg.LATTICE_LOCATION = "/home/mattking/jinja-catap/isis/output/yaml"
else:
    raise FileNotFoundError("Lattice location '/home/mattking/jinja-catap/isis/output/yaml' does not exist. Please check the path.")
from CATAP.common.machine.area import MachineArea


_area_names = [
    
    "MEBT",
    
    "LEBT",
    
]



cfg._machine_areas_tuple = namedtuple("MACHINE_AREAS", _area_names)
cfg.MACHINE_AREAS = cfg._machine_areas_tuple(*[MachineArea(name=name) for name in _area_names])
cfg.SNAPSHOT_LOCATION = "./snapshots/"
cfg.EPICS_TIMEOUT = 0.5
