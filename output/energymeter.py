
from CATAP.common.machine.pv_utils import StatisticalPV, BinaryPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class EnergyMeterPVMap(PVMap):
    
    ENERGYREADBACK: StatisticalPV
    
    OVERRANGE: BinaryPV
    
    RANGESP: StatePV
    
    RUNSP: BinaryPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        EnergyMeterPVMap.is_virtual = is_virtual
        EnergyMeterPVMap.connect_on_creation = connect_on_creation
        super(
            EnergyMeterPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def energyreadback(self):
        return self.ENERGYREADBACK.get()
    
    
    @property
    def overrange(self):
        return self.OVERRANGE.get()
    
    
    @property
    def rangesp(self):
        return self.RANGESP.get()
    
    @rangesp.setter
    def rangesp(self, value):
        self.RANGESP.put(value)
    
    
    @property
    def runsp(self):
        return self.RUNSP.get()
    
    @runsp.setter
    def runsp(self, value):
        self.RUNSP.put(value)
    
    



class EnergyMeterControlsInformation(ControlsInformation):
    """
    Class for controlling a energymeter via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[EnergyMeterPVMap]
    """Dictionary of PVs read in from a config file (see :class:`~CATAP.common.machine.hardware.PVMap`)"""
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
        EnergyMeterControlsInformation.is_virtual = is_virtual
        EnergyMeterControlsInformation.connect_on_creation = connect_on_creation
        super(
            EnergyMeterControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> EnergyMeterPVMap:
        return EnergyMeterPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def energyreadback(self):
        return self.pv_record_map.energyreadback
    
    
    @property
    def overrange(self):
        return self.pv_record_map.overrange
    
    
    @property
    def rangesp(self):
        return self.pv_record_map.rangesp
    
    @rangesp.setter
    def rangesp(self, value):
        self.pv_record_map.rangesp = value
    
    
    @property
    def runsp(self):
        return self.pv_record_map.runsp
    
    @runsp.setter
    def runsp(self, value):
        self.pv_record_map.runsp = value
    
    


class EnergyMeterProperties(Properties):
    """
    Class for defining energymeter-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    calibration_factor: float
    """"""
    
    position: float
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            EnergyMeterProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def calibration_factor(self):
        return self.calibration_factor
    
    @property
    def position(self):
        return self.position
    

    
    @property
    def calibration_factor(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.calibration_factor

    @calibration_factor.setter
    def calibration_factor(self, value: float) -> None:
        self.calibration_factor = value
    
    @property
    def position(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.position

    @position.setter
    def position(self, value: float) -> None:
        self.position = value
    

class EnergyMeter(Hardware):
    """
    Middle layer class for interacting with a specific energymeter object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[EnergyMeterControlsInformation]
    """Controls information pertaining to this energymeter
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[EnergyMeterProperties]
    """Properties pertaining to this energymeter
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            EnergyMeter,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> EnergyMeterControlsInformation:
        try:
            return EnergyMeterControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> EnergyMeterProperties:
        try:
            return EnergyMeterProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def energyreadback(self):
        return self.controls_information.energyreadback
    
    
    @property
    def overrange(self):
        return self.controls_information.overrange
    
    
    @property
    def rangesp(self):
        return self.controls_information.rangesp
    
    @rangesp.setter
    def rangesp(self, value):
        self.controls_information.rangesp = value
    
    
    @property
    def runsp(self):
        return self.controls_information.runsp
    
    @runsp.setter
    def runsp(self, value):
        self.controls_information.runsp = value
    
    

class EnergyMeterFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.energymeter.EnergyMeter` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(EnergyMeterFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=EnergyMeter,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_energymeter(self, name: Union[str, List[str]] = None) -> EnergyMeter:
        """
        Returns the energymeter object for the given name(s).

        :param name: Name(s) of the energymeter.
        :type name: str or list of str

        :return: Energymeter object(s).
        :rtype: :class:`~CATAP.laser.components.energymeter.EnergyMeter`
        or Dict[str: :class:`~CATAP.laser.components.energymeter.EnergyMeter`]
        """
        return self.get_hardware(name)

    
    def energyreadback(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'energyreadback' property of the energymeter(s).

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the 'ENERGYREADBACK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.energyreadback)
    
    def overrange(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'overrange' property of the energymeter(s).

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the 'OVERRANGE' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.overrange)
    
    def rangesp(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rangesp' property of the energymeter(s).

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the 'RANGESP' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.rangesp)
    
    def runsp(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'runsp' property of the energymeter(s).

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the 'RUNSP' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.runsp)
    