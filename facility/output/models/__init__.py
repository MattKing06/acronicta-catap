import catapcore.config as cfg
from catapcore.common.machine.area import MachineArea
from typing import Dict, List, Tuple
from collections import namedtuple
import os


if os.path.exists("/home/mattking/acronicta-catap/facility/output/yaml"):
    cfg.LATTICE_LOCATION = "/home/mattking/acronicta-catap/facility/output/yaml"
else:
    raise FileNotFoundError(
        "Lattice location '/home/mattking/acronicta-catap/facility/output/yaml' does not exist. Please check the path."
    )
from catapcore.common.machine.area import MachineArea


_area_names = [
    "BL02",
    "BL01",
]
cfg._machine_areas_tuple = namedtuple("MACHINE_AREAS", _area_names)
cfg.MACHINE_AREAS = cfg._machine_areas_tuple(
    *[MachineArea(name=name) for name in _area_names]
)


_hardware_types = {
    "BPM": [
        "STANDARD",
    ],
}


def _convert_types_to_named_tuple(types: Dict[str, List[str]]) -> Tuple:
    _subtypes = [
        namedtuple(type_name, types[type_name])(*types[type_name])
        for type_name in types
    ]
    _types = namedtuple("TYPES", types.keys())
    return _types(*_subtypes)


cfg.TYPES = _convert_types_to_named_tuple(types=_hardware_types)


cfg.SNAPSHOT_LOCATION = "./snapshots/"
cfg.EPICS_TIMEOUT = 0.5
