import CATAP.config as cfg
cfg.LATTICE_LOCATION = "./yaml"
from magnet import MagnetFactory
from bpm import BPMFactory
from camera import CameraFactory
# Test the generated classes
mag = MagnetFactory(is_virtual=True)
bpm = BPMFactory(is_virtual=True)
cam = CameraFactory(is_virtual=True)
print(cam.ana_x_rbv())
print(bpm.x())
print(mag.readi())
