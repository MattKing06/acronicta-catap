
from CATAP.common.machine.pv_utils import BinaryPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ValvePVMap(PVMap):
    
    Close: BinaryPV
    
    Open: BinaryPV
    
    Sta: StatePV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ValvePVMap.is_virtual = is_virtual
        ValvePVMap.connect_on_creation = connect_on_creation
        super(
            ValvePVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def close(self):
        return self.Close.get()
    
    @close.setter
    def close(self, value):
        self.Close.put(value)
    
    
    @property
    def open(self):
        return self.Open.get()
    
    @open.setter
    def open(self, value):
        self.Open.put(value)
    
    
    @property
    def sta(self):
        return self.Sta.get()
    
    



class ValveControlsInformation(ControlsInformation):
    """
    Class for controlling a valve via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ValvePVMap]
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
        ValveControlsInformation.is_virtual = is_virtual
        ValveControlsInformation.connect_on_creation = connect_on_creation
        super(
            ValveControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ValvePVMap:
        return ValvePVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def close(self):
        return self.pv_record_map.close
    
    @close.setter
    def close(self, value):
        self.pv_record_map.close = value
    
    
    @property
    def open(self):
        return self.pv_record_map.open
    
    @open.setter
    def open(self, value):
        self.pv_record_map.open = value
    
    
    @property
    def sta(self):
        return self.pv_record_map.sta
    
    


class ValveProperties(Properties):
    """
    Class for defining valve-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    valve_set_max_wait_time: float
    """"""
    
    valve_type: str
    """"""
    
    virtual_name: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            ValveProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def valve_set_max_wait_time(self):
        return self.valve_set_max_wait_time
    
    @property
    def valve_type(self):
        return self.valve_type
    
    @property
    def virtual_name(self):
        return self.virtual_name
    

    
    @property
    def valve_max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.valve_set_max_wait_time

    @valve_max_wait_time.setter
    def valve_max_wait_time(self, value: float) -> None:
        self.valve_set_max_wait_time = value
    

class Valve(Hardware):
    """
    Middle layer class for interacting with a specific valve object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ValveControlsInformation]
    """Controls information pertaining to this valve
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ValveProperties]
    """Properties pertaining to this valve
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Valve,
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
    def validate_controls_information(cls, v: Any) -> ValveControlsInformation:
        try:
            return ValveControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ValveProperties:
        try:
            return ValveProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def close(self):
        return self.controls_information.close
    
    @close.setter
    def close(self, value):
        self.controls_information.close = value
    
    
    @property
    def open(self):
        return self.controls_information.open
    
    @open.setter
    def open(self, value):
        self.controls_information.open = value
    
    
    @property
    def sta(self):
        return self.controls_information.sta
    
    

class ValveFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.valve.Valve` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(ValveFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Valve,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_valve(self, name: Union[str, List[str]] = None) -> Valve:
        """
        Returns the valve object for the given name(s).

        :param name: Name(s) of the valve.
        :type name: str or list of str

        :return: Valve object(s).
        :rtype: :class:`~CATAP.laser.components.valve.Valve`
        or Dict[str: :class:`~CATAP.laser.components.valve.Valve`]
        """
        return self.get_hardware(name)

    
    def close(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'close' property of the valve(s).

        :param name: Name(s) of the valve.
        :type name: str or list of str or None

        :return: Value(s) of the 'Close' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda valve: valve.close)
    
    def open(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'open' property of the valve(s).

        :param name: Name(s) of the valve.
        :type name: str or list of str or None

        :return: Value(s) of the 'Open' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda valve: valve.open)
    
    def sta(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'sta' property of the valve(s).

        :param name: Name(s) of the valve.
        :type name: str or list of str or None

        :return: Value(s) of the 'Sta' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda valve: valve.sta)
    