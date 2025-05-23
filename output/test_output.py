import CATAP.config as cfg
cfg.LATTICE_LOCATION = "./yaml"
from magnet import MagnetFactory
mag = MagnetFactory(is_virtual=True)

print(mag.readi())
