
from CATAP.common.machine.pv_utils import StatePV, BinaryPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ScreenPVMap(PVMap):
    
    POS: StatePV
    
    EN: BinaryPV
    
    MOVING: BinaryPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ScreenPVMap.is_virtual = is_virtual
        ScreenPVMap.connect_on_creation = connect_on_creation
        super(
            ScreenPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def pos(self):
        return self.POS.get()
    
    @pos.setter
    def pos(self, value):
        self.POS.put(value)
    
    
    @property
    def en(self):
        return self.EN.get()
    
    @en.setter
    def en(self, value):
        self.EN.put(value)
    
    
    @property
    def moving(self):
        return self.MOVING.get()
    
    



class ScreenControlsInformation(ControlsInformation):
    """
    Class for controlling a screen via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ScreenPVMap]
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
        ScreenControlsInformation.is_virtual = is_virtual
        ScreenControlsInformation.connect_on_creation = connect_on_creation
        super(
            ScreenControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ScreenPVMap:
        return ScreenPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def pos(self):
        return self.pv_record_map.pos
    
    @pos.setter
    def pos(self, value):
        self.pv_record_map.pos = value
    
    
    @property
    def en(self):
        return self.pv_record_map.en
    
    @en.setter
    def en(self, value):
        self.pv_record_map.en = value
    
    
    @property
    def moving(self):
        return self.pv_record_map.moving
    
    


class ScreenProperties(Properties):
    """
    Class for defining screen-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    camera_name: str
    """"""
    
    has_camera: bool
    """"""
    
    position: float
    """"""
    
    screen_type: str
    """"""
    
    set_max_wait_time: float
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            ScreenProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def camera_name(self):
        return self.camera_name
    
    @property
    def has_camera(self):
        return self.has_camera
    
    @property
    def position(self):
        return self.position
    
    @property
    def screen_type(self):
        return self.screen_type
    
    @property
    def set_max_wait_time(self):
        return self.set_max_wait_time
    

    
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
    
    @property
    def max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.set_max_wait_time

    @max_wait_time.setter
    def max_wait_time(self, value: float) -> None:
        self.set_max_wait_time = value
    

class Screen(Hardware):
    """
    Middle layer class for interacting with a specific screen object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ScreenControlsInformation]
    """Controls information pertaining to this screen
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ScreenProperties]
    """Properties pertaining to this screen
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Screen,
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
    def validate_controls_information(cls, v: Any) -> ScreenControlsInformation:
        try:
            return ScreenControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ScreenProperties:
        try:
            return ScreenProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def pos(self):
        return self.controls_information.pos
    
    @pos.setter
    def pos(self, value):
        self.controls_information.pos = value
    
    
    @property
    def en(self):
        return self.controls_information.en
    
    @en.setter
    def en(self, value):
        self.controls_information.en = value
    
    
    @property
    def moving(self):
        return self.controls_information.moving
    
    

class ScreenFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.screen.Screen` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(ScreenFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Screen,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_screen(self, name: Union[str, List[str]] = None) -> Screen:
        """
        Returns the screen object for the given name(s).

        :param name: Name(s) of the screen.
        :type name: str or list of str

        :return: Screen object(s).
        :rtype: :class:`~CATAP.laser.components.screen.Screen`
        or Dict[str: :class:`~CATAP.laser.components.screen.Screen`]
        """
        return self.get_hardware(name)

    
    def pos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'pos' property of the screen(s).

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the 'POS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.pos)
    
    def en(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'en' property of the screen(s).

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the 'EN' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.en)
    
    def moving(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'moving' property of the screen(s).

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the 'MOVING' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.moving)
    