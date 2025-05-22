
from CATAP.common.machine.pv_utils import BinaryPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ShutterPVMap(PVMap):
    
    SetPos: BinaryPV
    
    State: StatePV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ShutterPVMap.is_virtual = is_virtual
        ShutterPVMap.connect_on_creation = connect_on_creation
        super(
            ShutterPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def setpos(self):
        return self.SetPos.get()
    
    @setpos.setter
    def setpos(self, value):
        self.SetPos.put(value)
    
    
    @property
    def state(self):
        return self.State.get()
    
    



class ShutterControlsInformation(ControlsInformation):
    """
    Class for controlling a shutter via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ShutterPVMap]
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
        ShutterControlsInformation.is_virtual = is_virtual
        ShutterControlsInformation.connect_on_creation = connect_on_creation
        super(
            ShutterControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ShutterPVMap:
        return ShutterPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def setpos(self):
        return self.pv_record_map.setpos
    
    @setpos.setter
    def setpos(self, value):
        self.pv_record_map.setpos = value
    
    
    @property
    def state(self):
        return self.pv_record_map.state
    
    


class ShutterProperties(Properties):
    """
    Class for defining shutter-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    shutter_set_max_wait_time: float
    """"""
    
    shutter_type: str
    """"""
    
    virtual_name: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            ShutterProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def shutter_set_max_wait_time(self):
        return self.shutter_set_max_wait_time
    
    @property
    def shutter_type(self):
        return self.shutter_type
    
    @property
    def virtual_name(self):
        return self.virtual_name
    

    
    @property
    def shutter_max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.shutter_set_max_wait_time

    @shutter_max_wait_time.setter
    def shutter_max_wait_time(self, value: float) -> None:
        self.shutter_set_max_wait_time = value
    

class Shutter(Hardware):
    """
    Middle layer class for interacting with a specific shutter object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ShutterControlsInformation]
    """Controls information pertaining to this shutter
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ShutterProperties]
    """Properties pertaining to this shutter
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Shutter,
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
    def validate_controls_information(cls, v: Any) -> ShutterControlsInformation:
        try:
            return ShutterControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ShutterProperties:
        try:
            return ShutterProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def setpos(self):
        return self.controls_information.setpos
    
    @setpos.setter
    def setpos(self, value):
        self.controls_information.setpos = value
    
    
    @property
    def state(self):
        return self.controls_information.state
    
    

class ShutterFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.shutter.Shutter` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(ShutterFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Shutter,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_shutter(self, name: Union[str, List[str]] = None) -> Shutter:
        """
        Returns the shutter object for the given name(s).

        :param name: Name(s) of the shutter.
        :type name: str or list of str

        :return: Shutter object(s).
        :rtype: :class:`~CATAP.laser.components.shutter.Shutter`
        or Dict[str: :class:`~CATAP.laser.components.shutter.Shutter`]
        """
        return self.get_hardware(name)

    
    def setpos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'setpos' property of the shutter(s).

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the 'SetPos' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.setpos)
    
    def state(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'state' property of the shutter(s).

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the 'State' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.state)
    