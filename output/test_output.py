import CATAP.config as cfg
cfg.LATTICE_LOCATION = "./yaml"
from models.magnet import MagnetFactoryModel
from models.bpm import BPMFactoryModel
from models.camera import CameraFactoryModel
from models.cavity import CavityFactoryModel
from models.charge import ChargeFactoryModel
from models.energymeter import EnergyMeterFactoryModel
from models.mirror import MirrorFactoryModel
# Test the generated classes
mag = MagnetFactoryModel(is_virtual=True)
bpm = BPMFactoryModel(is_virtual=True)
cam = CameraFactoryModel(is_virtual=True)
cav = CavityFactoryModel(is_virtual=True)
em = EnergyMeterFactoryModel(is_virtual=True)
qf = ChargeFactoryModel(is_virtual=True)
mirr = MirrorFactoryModel(is_virtual=True)
print(mirr.v_pos())
print(qf.q())
print(em.energyreadback())
print(cav.powermwread())
print(cam.ana_x_rbv())
print(bpm.x())
print(mag.readi())
