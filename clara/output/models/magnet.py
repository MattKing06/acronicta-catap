from catapcore.common.machine.pv_utils import ScalarPV, StatePV, BinaryPV, StatisticalPV
from catapcore.common.machine.hardware import (
    PVMap,
    ControlsInformation,
    Properties,
    Hardware,
)
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict


class MagnetPVMapModel(PVMap):

    GETSETI: ScalarPV

    """Gets the value of the target current for a magnet power supply."""

    SPOWER: StatePV

    """Sets the state of a power supply"""

    RPOWER: StatePV

    """Gets the state of a power supply"""

    ILK_RESET: BinaryPV

    """Resets the magnet interlocks"""

    RILK: StatePV

    """Gets the interlock state for a magnet"""

    ILK_ON: BinaryPV

    """If the interlocks are clear, this enables them"""

    ILK_OFF: BinaryPV

    """If the interlocks are clear, this disables them"""

    ILK_PSU_RESET: BinaryPV = None

    """Reset the magnet power supply interlocks"""

    READI: StatisticalPV

    """Gets the readback current of a magnet power supply."""

    SETI: ScalarPV

    """Sets the target current for a magnet power supply."""

    SETK: ScalarPV

    """Sets the target field strength for a magnet. This ultimately sets a current for the power supply"""

    READK: StatisticalPV

    """Reads the calculated K value for a magnet based on momentum of the section"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        MagnetPVMapModel.is_virtual = is_virtual
        MagnetPVMapModel.connect_on_creation = connect_on_creation
        super(
            MagnetPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @property
    def getseti(self):
        """Default Getter implementation for GETSETI"""

        return self.GETSETI.get()

    @property
    def spower(self):
        """Default Getter implementation for SPOWER"""

        return self.SPOWER.get()

    @spower.setter
    def spower(self, value):
        """Default Setter implementation for SPOWER"""

        return self.SPOWER.put(value)

    @property
    def rpower(self):
        """Default Getter implementation for RPOWER"""

        return self.RPOWER.get()

    @property
    def ilk_reset(self):
        """Default Getter implementation for ILK_RESET"""

        return self.ILK_RESET.get()

    @ilk_reset.setter
    def ilk_reset(self, value):
        """Default Setter implementation for ILK_RESET"""

        return self.ILK_RESET.put(value)

    @property
    def rilk(self):
        """Default Getter implementation for RILK"""

        return self.RILK.get()

    @property
    def ilk_on(self):
        """Default Getter implementation for ILK_ON"""

        return self.ILK_ON.get()

    @ilk_on.setter
    def ilk_on(self, value):
        """Default Setter implementation for ILK_ON"""

        return self.ILK_ON.put(value)

    @property
    def ilk_off(self):
        """Default Getter implementation for ILK_OFF"""

        return self.ILK_OFF.get()

    @ilk_off.setter
    def ilk_off(self, value):
        """Default Setter implementation for ILK_OFF"""

        return self.ILK_OFF.put(value)

    @property
    def ilk_psu_reset(self):
        """Default Getter implementation for ILK_PSU_RESET"""

        if self.ILK_PSU_RESET:
            return self.ILK_PSU_RESET.get()

    @ilk_psu_reset.setter
    def ilk_psu_reset(self, value):
        """Default Setter implementation for ILK_PSU_RESET"""

        if self.ILK_PSU_RESET:
            return self.ILK_PSU_RESET.put(value)

    @property
    def readi(self):
        """Default Getter implementation for READI"""

        return self.READI.get()

    @property
    def seti(self):
        """Default Getter implementation for SETI"""

        return self.SETI.get()

    @seti.setter
    def seti(self, value):
        """Default Setter implementation for SETI"""

        return self.SETI.put(value)

    @property
    def setk(self):
        """Default Getter implementation for SETK"""

        return self.SETK.get()

    @setk.setter
    def setk(self, value):
        """Default Setter implementation for SETK"""

        return self.SETK.put(value)

    @property
    def readk(self):
        """Default Getter implementation for READK"""

        return self.READK.get()


class MagnetControlsInformationModel(ControlsInformation):
    """
    Class for controlling a magnet via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """

    pv_record_map: SerializeAsAny[MagnetPVMapModel]

    """Dictionary of PVs read in from a config file (see :class:`~catapcore.common.machine.hardware.PVMap`)"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
    )

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        MagnetControlsInformationModel.is_virtual = is_virtual
        MagnetControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            MagnetControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> MagnetPVMapModel:
        return MagnetPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    @property
    def getseti(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.GETSETI`."""
        return self.pv_record_map.getseti

    @property
    def spower(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.SPOWER`."""
        return self.pv_record_map.spower

    @spower.setter
    def spower(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.SPOWER`."""
        self.pv_record_map.spower = value

    @property
    def rpower(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.RPOWER`."""
        return self.pv_record_map.rpower

    @property
    def ilk_reset(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.ILK_RESET`."""
        return self.pv_record_map.ilk_reset

    @ilk_reset.setter
    def ilk_reset(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.ILK_RESET`."""
        self.pv_record_map.ilk_reset = value

    @property
    def rilk(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.RILK`."""
        return self.pv_record_map.rilk

    @property
    def ilk_on(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.ILK_ON`."""
        return self.pv_record_map.ilk_on

    @ilk_on.setter
    def ilk_on(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.ILK_ON`."""
        self.pv_record_map.ilk_on = value

    @property
    def ilk_off(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.ILK_OFF`."""
        return self.pv_record_map.ilk_off

    @ilk_off.setter
    def ilk_off(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.ILK_OFF`."""
        self.pv_record_map.ilk_off = value

    @property
    def ilk_psu_reset(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.ILK_PSU_RESET`."""
        return self.pv_record_map.ilk_psu_reset

    @ilk_psu_reset.setter
    def ilk_psu_reset(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.ILK_PSU_RESET`."""
        self.pv_record_map.ilk_psu_reset = value

    @property
    def readi(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.READI`."""
        return self.pv_record_map.readi

    @property
    def seti(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.SETI`."""
        return self.pv_record_map.seti

    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.SETI`."""
        self.pv_record_map.seti = value

    @property
    def setk(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.SETK`."""
        return self.pv_record_map.setk

    @setk.setter
    def setk(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.SETK`."""
        self.pv_record_map.setk = value

    @property
    def readk(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.READK`."""
        return self.pv_record_map.readk


class MagnetPropertiesModel(Properties):
    """
    Class for defining magnet-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """

    subtype: str

    max_i: float

    min_i: float

    manufacturer: str

    mag_set_max_wait_time: float

    magnetic_length: float

    degauss_tolerance: float

    degauss_values: str

    ri_tolerance: float

    field_integral_coefficients: str

    serial_number: int

    virtual_name: str

    def __init__(self, *args, **kwargs):
        super(
            MagnetPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )


class MagnetModel(Hardware):
    """
    Middle layer class for interacting with a specific magnet object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[MagnetControlsInformationModel]
    """Controls information pertaining to this magnet
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[MagnetPropertiesModel]
    """Properties pertaining to this magnet
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            MagnetModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            "GETSETI",
            "SPOWER",
            "RPOWER",
            "ILK_RESET",
            "RILK",
            "ILK_ON",
            "ILK_OFF",
            "ILK_PSU_RESET",
            "READI",
            "SETI",
            "SETK",
            "READK",
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> MagnetControlsInformationModel:
        try:
            return MagnetControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> MagnetPropertiesModel:
        try:
            return MagnetPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    @property
    def getseti(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.GETSETI`."""
        return self.controls_information.getseti

    @property
    def spower(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.SPOWER`."""
        return self.controls_information.spower

    @spower.setter
    def spower(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.SPOWER`."""
        self.controls_information.spower = value

    @property
    def rpower(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.RPOWER`."""
        return self.controls_information.rpower

    @property
    def ilk_reset(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.ILK_RESET`."""
        return self.controls_information.ilk_reset

    @ilk_reset.setter
    def ilk_reset(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.ILK_RESET`."""
        self.controls_information.ilk_reset = value

    @property
    def rilk(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.RILK`."""
        return self.controls_information.rilk

    @property
    def ilk_on(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.ILK_ON`."""
        return self.controls_information.ilk_on

    @ilk_on.setter
    def ilk_on(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.ILK_ON`."""
        self.controls_information.ilk_on = value

    @property
    def ilk_off(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.ILK_OFF`."""
        return self.controls_information.ilk_off

    @ilk_off.setter
    def ilk_off(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.ILK_OFF`."""
        self.controls_information.ilk_off = value

    @property
    def ilk_psu_reset(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.ILK_PSU_RESET`."""
        return self.controls_information.ilk_psu_reset

    @ilk_psu_reset.setter
    def ilk_psu_reset(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.ILK_PSU_RESET`."""
        self.controls_information.ilk_psu_reset = value

    @property
    def readi(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.READI`."""
        return self.controls_information.readi

    @property
    def seti(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.SETI`."""
        return self.controls_information.seti

    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.SETI`."""
        self.controls_information.seti = value

    @property
    def setk(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.SETK`."""
        return self.controls_information.setk

    @setk.setter
    def setk(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.SETK`."""
        self.controls_information.setk = value

    @property
    def readk(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.READK`."""
        return self.controls_information.readk


class MagnetFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.magnet.Magnet` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(MagnetFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=MagnetModel,
            lattice_folder="Magnet",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_magnet(self, name: Union[str, List[str]] = None) -> MagnetModel:
        """
        Returns the magnet object for the given name(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str

        :return: Magnet object(s).
        :rtype: :class:`magnetModel.Magnet`
        or Dict[str: :class:`magnet.Magnet`]
        """
        return self.get_hardware(name)

    def getseti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.GETSETI`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.GETSETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.getseti)

    def spower(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.SPOWER`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.SPOWER` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.spower)

    def rpower(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.RPOWER`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.RPOWER` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.rpower)

    def ilk_reset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.ILK_RESET`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.ILK_RESET` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_reset)

    def rilk(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.RILK`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.RILK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.rilk)

    def ilk_on(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.ILK_ON`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.ILK_ON` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_on)

    def ilk_off(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.ILK_OFF`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.ILK_OFF` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_off)

    def ilk_psu_reset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.ILK_PSU_RESET`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.ILK_PSU_RESET` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_psu_reset)

    def readi(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.READI`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.READI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readi)

    def seti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.SETI`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.SETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.seti)

    def setk(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.SETK`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.SETK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.setk)

    def readk(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.READK`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.READK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readk)
