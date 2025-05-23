import CATAP.config as cfg
cfg.LATTICE_LOCATION = "./yaml"
from magnet import MagnetFactory
from bpm import BPMFactory
from camera import CameraFactory
from cavity import CavityFactory
from charge import ChargeFactory
from energymeter import EnergyMeterFactory
# Test the generated classes
mag = MagnetFactory(is_virtual=True)
bpm = BPMFactory(is_virtual=True)
cam = CameraFactory(is_virtual=True)
cav = CavityFactory(is_virtual=True)
em = EnergyMeterFactory(is_virtual=True)
qf = ChargeFactory(is_virtual=True)
print(qf.q())
print(em.energyreadback())
print(cav.powermwread())
print(cam.ana_x_rbv())
print(bpm.x())
print(mag.readi())
