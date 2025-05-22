import CATAP.config as cfg
cfg.LATTICE_LOCATION = "../lattice"
from magnet import MagnetFactory
mag = MagnetFactory(is_virtual=True)

print(mag.readi())