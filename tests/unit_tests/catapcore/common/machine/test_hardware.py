import os
import unittest
from ruamel.yaml import YAML
from catapcore.common.machine.hardware import Hardware, PVMap
from catapcore.common.machine.pv_utils import StatisticalPV, StatePV, BinaryPV
from catapcore.common.machine.area import MachineArea
from catapcore.common.exceptions import UnexpectedPVEntry
import catapcore.config as cfg

cfg.LATTICE_LOCATION = "./tests/lattice"


class DummyPVMap(PVMap):
    """
    Mock PVMap for testing purposes.
    """

    X: StatisticalPV
    Y: StatisticalPV
    ACQUIRE: StatePV | None = None
    IS_ACQUIRING: BinaryPV | None = None

    def __init__(
        self,
        is_virtual: bool = False,
        connect_on_creation: bool = False,
        **kwargs,
    ):
        super().__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            **kwargs,
        )


class TestPVMap(unittest.TestCase):
    def setUp(self) -> None:
        self.yaml_file = os.path.join(
            cfg.LATTICE_LOCATION,
            "BPM",
            "BPM-02.yaml",
        )
        self.pv_config = None
        with open(self.yaml_file, "r") as file:
            yaml = YAML(typ="safe")
            config = dict(yaml.load(file))
            self.pv_config = config["controls_information"]["pv_record_map"]
        self.test_pv_map: DummyPVMap = DummyPVMap(
            is_virtual=True,
            connect_on_creation=False,
            **self.pv_config,
        )
        return super().setUp()

    def test_map_initialization(self):
        """
        Test that the PVMap initializes correctly
        with the provided configuration.
        """
        self.assertIsInstance(self.test_pv_map, DummyPVMap)
        self.assertTrue(self.test_pv_map.is_virtual)
        self.assertFalse(self.test_pv_map.connect_on_creation)

    def test_map_types_are_correct(self):
        self.assertIsInstance(self.test_pv_map.X, StatisticalPV)
        self.assertIsInstance(self.test_pv_map.Y, StatisticalPV)
        self.assertIsInstance(self.test_pv_map.ACQUIRE, StatePV)
        self.assertIsInstance(self.test_pv_map.IS_ACQUIRING, BinaryPV)

    def test_map_statistics_dictionary(self):
        """
        Check that the statistics dictionary is correctly set up
        for the PVs in the map.
        """
        self.assertIn("X", self.test_pv_map.statistics)
        self.assertIn("Y", self.test_pv_map.statistics)
        self.assertNotIn("ACQUIRE", self.test_pv_map.statistics)
        self.assertNotIn("IS_ACQUIRING", self.test_pv_map.statistics)
        # Check that the statistics are instances of StatisticalPV
        self.assertIsInstance(self.test_pv_map.statistics["X"], StatisticalPV)
        self.assertIsInstance(self.test_pv_map.statistics["Y"], StatisticalPV)

    def test_map_pv_dictionary(self):
        """
        Check that the PV dictionary is correctly set up
        for the PVs in the map.
        """
        self.assertIn("X", self.test_pv_map._pvs)
        self.assertIn("Y", self.test_pv_map._pvs)
        self.assertIn("ACQUIRE", self.test_pv_map._pvs)
        self.assertIn("IS_ACQUIRING", self.test_pv_map._pvs)

    def test_map_has_correct_pv_virtual_names(self):
        """
        Check that the PV names are set correctly for the virtual PVs.
        This involves checking the default VIRTUAL_PREFIX when no virtual_pv
        is provided, as well as ensuring that the virtual_pv
        is set correctly when provided.
        """
        self.pv_config["X"].update({"virtual_pv": "SIM:BPM-02:X"})
        pv_map: DummyPVMap = DummyPVMap(
            is_virtual=True,
            connect_on_creation=False,
            **self.pv_config,
        )
        self.assertEqual(pv_map.X.pv.pvname, "SIM:BPM-02:X")
        self.assertEqual(pv_map.Y.pv.pvname, "VM-BPM-02:Y_READBACK")


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.yaml_file = os.path.join(
            cfg.LATTICE_LOCATION,
            "BPM",
            "BPM-01.yaml",
        )
        self.hardware_config = None
        with open(self.yaml_file, "r") as file:
            yaml = YAML(typ="safe")
            self.hardware_config = dict(yaml.load(file))
        cfg.MACHINE_AREAS = [
            MachineArea(name="BL01"),
            MachineArea(name="BL02"),
        ]
        return super().setUp()

    def test_load_hardware(self):
        with self.assertWarns(
            UnexpectedPVEntry,
            msg="Expected warning about all the BPM PVs",
        ):
            hardware = Hardware(
                is_virtual=True,
                connect_on_creation=False,
                **self.hardware_config,
            )
        self.assertEqual(hardware.name, "BPM-01")
        self.assertIsInstance(hardware.aliases, list)
        self.assertIsInstance(hardware.machine_area, MachineArea)
        self.assertEqual(hardware.machine_area.name, "BL01")

    def test_load_bad_machine_area(self):
        self.hardware_config["properties"]["machine_area"] = "UNKNOWN"
        with self.assertRaises(ValueError):
            with self.assertWarns(
                UnexpectedPVEntry,
                msg="Expected warning about all the camera PVs",
            ):
                Hardware(
                    is_virtual=True,
                    connect_on_creation=False,
                    **self.hardware_config,
                )
