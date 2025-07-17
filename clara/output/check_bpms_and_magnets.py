from hardware.magnet import MagnetFactory
from hardware.bpm import BPMFactory

""" Create Factories """
mf = MagnetFactory()
bpmf = BPMFactory()

""" Save a snapshot of magnet settings and bpm readings """
mf.create_snapshot()
mf.save_snapshot("17_06_2025_magnets")
bpmf.create_snapshot()
bpmf.save_snapshot("17_06_2025_bpms")

""" Set some new magnet currents """
new_optics = {"S02-QUAD-01": 1.0, "S03-QUAD-01": 2.0}
for name, value in new_optics.items():
    mf.get_magnet(name).spower = 1
    mf.get_magnet(name).seti = value

""" Get all BPM X and Y values as dict """
x_values = bpmf.x()
y_values = bpmf.y()

""" Save out a snapshot of BPM values """
bpmf.create_snapshot()
bpmf.save_snapshot("17_06_2025_bpms_after_adjustment")

""" Load older magnet settings """
mf.load_snapshot("17_06_2025_magnets.yaml", apply=True)
