from catapcore.common.machine.pv_utils import StatisticalPV, StatePV, BinaryPV
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
from enum import EnumMeta
from pydantic import field_validator, SerializeAsAny, ConfigDict


class BPMPVMapModel(PVMap):

    X: StatisticalPV

    """X position reading"""

    Y: StatisticalPV

    """X position reading"""

    ACQUIRE: StatePV = None

    """Trigger acquisition of BPM data"""

    IS_ACQUIRING: BinaryPV = None

    """Indicates if BPM is currently acquiring data"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        BPMPVMapModel.is_virtual = is_virtual
        BPMPVMapModel.connect_on_creation = connect_on_creation
        super(
            BPMPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @property
    def x(self):
        """Default Getter implementation for X"""

        return self.X.get()

    @property
    def y(self):
        """Default Getter implementation for Y"""

        return self.Y.get()

    @property
    def acquire(self):
        """Default Getter implementation for ACQUIRE"""

        if self.ACQUIRE:
            return self.ACQUIRE.get()

    @acquire.setter
    def acquire(self, value):
        """Default Setter implementation for ACQUIRE"""

        if self.ACQUIRE:
            return self.ACQUIRE.put(value)

    @property
    def is_acquiring(self):
        """Default Getter implementation for IS_ACQUIRING"""

        if self.IS_ACQUIRING:
            return self.IS_ACQUIRING.get()

    @property
    def acquire_states(self) -> EnumMeta:
        """Default Getter implementation for :attr:`BPMPVMapModel.ACQUIRE.states`."""
        if self.ACQUIRE:
            return self.ACQUIRE.states


class BPMControlsInformationModel(ControlsInformation):
    """
    Class for controlling a bpm via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """

    pv_record_map: SerializeAsAny[BPMPVMapModel]

    x_calibration_factor: float

    y_calibration_factor: float

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
        BPMControlsInformationModel.is_virtual = is_virtual
        BPMControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            BPMControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> BPMPVMapModel:
        return BPMPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    @property
    def x(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.X`."""
        return self.pv_record_map.x

    @property
    def y(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.Y`."""
        return self.pv_record_map.y

    @property
    def acquire(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.ACQUIRE`."""
        return self.pv_record_map.acquire

    @acquire.setter
    def acquire(self, value):
        """Default Setter implementation for :attr:`BPMPVMapModel.ACQUIRE`."""
        self.pv_record_map.acquire = value

    @property
    def is_acquiring(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.IS_ACQUIRING`."""
        return self.pv_record_map.is_acquiring

    @property
    def x_calibration_factor(self) -> float:
        """Default Getter implementation for x_calibration_factor."""

        return self.x_calibration_factor

    @property
    def y_calibration_factor(self) -> float:
        """Default Getter implementation for y_calibration_factor."""

        return self.y_calibration_factor

    @property
    def acquire_states(self) -> EnumMeta:
        """Default Getter implementation for :attr:`BPMPVMapModel.acquire_states`."""
        return self.pv_record_map.acquire_states


class BPMPropertiesModel(Properties):
    """
    Class for defining bpm-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """

    manufacturer: str

    model: str

    serial_number: str

    installation_date: str

    last_calibration_date: str

    next_calibration_due: str

    def __init__(self, *args, **kwargs):
        super(
            BPMPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )


class BPMModel(Hardware):
    """
    Middle layer class for interacting with a specific bpm object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[BPMControlsInformationModel]
    """Controls information pertaining to this bpm
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[BPMPropertiesModel]
    """Properties pertaining to this bpm
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            BPMModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            "X",
            "Y",
            "ACQUIRE",
            "IS_ACQUIRING",
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> BPMControlsInformationModel:
        try:
            return BPMControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> BPMPropertiesModel:
        try:
            return BPMPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    @property
    def x(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.X`."""
        return self.controls_information.x

    @property
    def y(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.Y`."""
        return self.controls_information.y

    @property
    def acquire(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.ACQUIRE`."""
        return self.controls_information.acquire

    @acquire.setter
    def acquire(self, value):
        """Default Setter implementation for :attr:`BPMControlsInformationModel.ACQUIRE`."""
        self.controls_information.acquire = value

    @property
    def is_acquiring(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.IS_ACQUIRING`."""
        return self.controls_information.is_acquiring


class BPMFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.bpm.BPM` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
        hardware_type: Hardware = BPMModel,
    ):
        super(BPMFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=hardware_type,
            lattice_folder="BPM",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_bpm(self, name: Union[str, List[str]] = None) -> BPMModel:
        """
        Returns the bpm object for the given name(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str

        :return: Bpm object(s).
        :rtype: :class:`bpmModel.BPM`
        or Dict[str: :class:`bpm.BPM`]
        """
        return self.get_hardware(name)

    def x(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.X`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.X` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.x)

    def y(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.Y`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.Y` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.y)

    def acquire(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.ACQUIRE`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.ACQUIRE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.acquire)

    def is_acquiring(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.IS_ACQUIRING`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.IS_ACQUIRING` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.is_acquiring)
