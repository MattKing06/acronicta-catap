
from catapcore.common.machine.pv_utils import StatePV, BinaryPV, ScalarPV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ScreenPVMapModel(PVMap):
    
    
    POS: StatePV = None
    
    """Vertical Device state"""
    
    
    MOVING: BinaryPV = None
    
    """Screen moving flag"""
    
    
    EN: BinaryPV = None
    
    """Screen enable flag"""
    
    
    V_POS: StatePV = None
    
    """Vertical Device state"""
    
    
    V_ACTPOS: ScalarPV = None
    
    """Screen actuator position"""
    
    
    V_MOVING: BinaryPV = None
    
    """Screen moving flag"""
    
    
    V_EN: BinaryPV = None
    
    """Screen enable flag"""
    
    
    H_POS: StatePV = None
    
    """Horizontal Device state"""
    
    
    H_ACTPOS: ScalarPV = None
    
    """Screen actuator position"""
    
    
    H_MOVING: BinaryPV = None
    
    """Screen moving flag"""
    
    
    H_EN: BinaryPV = None
    
    """Screen enable flag"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ScreenPVMapModel.is_virtual = is_virtual
        ScreenPVMapModel.connect_on_creation = connect_on_creation
        super(
            ScreenPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def pos(self):
        """Default Getter implementation for POS"""
        
        if self.POS:
            return self.POS.get()
        

    
    @pos.setter
    def pos(self, value):
        """Default Setter implementation for POS"""
        
        if self.POS:
            return self.POS.put(value)
        
    
    
    @property
    def moving(self):
        """Default Getter implementation for MOVING"""
        
        if self.MOVING:
            return self.MOVING.get()
        

    
    
    @property
    def en(self):
        """Default Getter implementation for EN"""
        
        if self.EN:
            return self.EN.get()
        

    
    @en.setter
    def en(self, value):
        """Default Setter implementation for EN"""
        
        if self.EN:
            return self.EN.put(value)
        
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for V_POS"""
        
        if self.V_POS:
            return self.V_POS.get()
        

    
    @v_pos.setter
    def v_pos(self, value):
        """Default Setter implementation for V_POS"""
        
        if self.V_POS:
            return self.V_POS.put(value)
        
    
    
    @property
    def v_actpos(self):
        """Default Getter implementation for V_ACTPOS"""
        
        if self.V_ACTPOS:
            return self.V_ACTPOS.get()
        

    
    
    @property
    def v_moving(self):
        """Default Getter implementation for V_MOVING"""
        
        if self.V_MOVING:
            return self.V_MOVING.get()
        

    
    
    @property
    def v_en(self):
        """Default Getter implementation for V_EN"""
        
        if self.V_EN:
            return self.V_EN.get()
        

    
    @v_en.setter
    def v_en(self, value):
        """Default Setter implementation for V_EN"""
        
        if self.V_EN:
            return self.V_EN.put(value)
        
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for H_POS"""
        
        if self.H_POS:
            return self.H_POS.get()
        

    
    @h_pos.setter
    def h_pos(self, value):
        """Default Setter implementation for H_POS"""
        
        if self.H_POS:
            return self.H_POS.put(value)
        
    
    
    @property
    def h_actpos(self):
        """Default Getter implementation for H_ACTPOS"""
        
        if self.H_ACTPOS:
            return self.H_ACTPOS.get()
        

    
    
    @property
    def h_moving(self):
        """Default Getter implementation for H_MOVING"""
        
        if self.H_MOVING:
            return self.H_MOVING.get()
        

    
    
    @property
    def h_en(self):
        """Default Getter implementation for H_EN"""
        
        if self.H_EN:
            return self.H_EN.get()
        

    
    @h_en.setter
    def h_en(self, value):
        """Default Setter implementation for H_EN"""
        
        if self.H_EN:
            return self.H_EN.put(value)
        
    
    



class ScreenControlsInformationModel(ControlsInformation):
    """
    Class for controlling a screen via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ScreenPVMapModel]

    
    
    movement_type: str
    
    
    
    vertical_devices: dict
    
    
    
    horizontal_devices: dict | None = None
    
    

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
        ScreenControlsInformationModel.is_virtual = is_virtual
        ScreenControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            ScreenControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ScreenPVMapModel:
        return ScreenPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def pos(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.POS`."""    
        return self.pv_record_map.pos
    
    @pos.setter
    def pos(self, value):
        """Default Setter implementation for :attr:`ScreenPVMapModel.POS`.""" 
        self.pv_record_map.pos = value
    
    
    @property
    def moving(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.MOVING`."""    
        return self.pv_record_map.moving
    
    
    @property
    def en(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.EN`."""    
        return self.pv_record_map.en
    
    @en.setter
    def en(self, value):
        """Default Setter implementation for :attr:`ScreenPVMapModel.EN`.""" 
        self.pv_record_map.en = value
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.V_POS`."""    
        return self.pv_record_map.v_pos
    
    @v_pos.setter
    def v_pos(self, value):
        """Default Setter implementation for :attr:`ScreenPVMapModel.V_POS`.""" 
        self.pv_record_map.v_pos = value
    
    
    @property
    def v_actpos(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.V_ACTPOS`."""    
        return self.pv_record_map.v_actpos
    
    
    @property
    def v_moving(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.V_MOVING`."""    
        return self.pv_record_map.v_moving
    
    
    @property
    def v_en(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.V_EN`."""    
        return self.pv_record_map.v_en
    
    @v_en.setter
    def v_en(self, value):
        """Default Setter implementation for :attr:`ScreenPVMapModel.V_EN`.""" 
        self.pv_record_map.v_en = value
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.H_POS`."""    
        return self.pv_record_map.h_pos
    
    @h_pos.setter
    def h_pos(self, value):
        """Default Setter implementation for :attr:`ScreenPVMapModel.H_POS`.""" 
        self.pv_record_map.h_pos = value
    
    
    @property
    def h_actpos(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.H_ACTPOS`."""    
        return self.pv_record_map.h_actpos
    
    
    @property
    def h_moving(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.H_MOVING`."""    
        return self.pv_record_map.h_moving
    
    
    @property
    def h_en(self):
        """Default Getter implementation for :attr:`ScreenPVMapModel.H_EN`."""    
        return self.pv_record_map.h_en
    
    @h_en.setter
    def h_en(self, value):
        """Default Setter implementation for :attr:`ScreenPVMapModel.H_EN`.""" 
        self.pv_record_map.h_en = value
    
    

    
    @property
    def movement_type(self) -> str:
        """Default Getter implementation for movement_type."""
        
        return self.movement_type
        
    
    @property
    def vertical_devices(self) -> dict:
        """Default Getter implementation for vertical_devices."""
        
        return self.vertical_devices
        
    
    @property
    def horizontal_devices(self) -> dict:
        """Default Getter implementation for horizontal_devices."""
        
        if self.horizontal_devices:
            return self.horizontal_devices.get()
        
    


class ScreenPropertiesModel(Properties):
    """
    Class for defining screen-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    camera_name: str
    
    
    
    has_camera: bool
    
    
    
    set_max_wait_time: float
    
    

    def __init__(self, *args, **kwargs):
        super(
            ScreenPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class ScreenModel(Hardware):
    """
    Middle layer class for interacting with a specific screen object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ScreenControlsInformationModel]
    """Controls information pertaining to this screen
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ScreenPropertiesModel]
    """Properties pertaining to this screen
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""
    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            ScreenModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            
            "POS",
            
            "MOVING",
            
            "EN",
            
            "V_POS",
            
            "V_ACTPOS",
            
            "V_MOVING",
            
            "V_EN",
            
            "H_POS",
            
            "H_ACTPOS",
            
            "H_MOVING",
            
            "H_EN",
            
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> ScreenControlsInformationModel:
        try:
            return ScreenControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ScreenPropertiesModel:
        try:
            return ScreenPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def pos(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.POS`."""
        return self.controls_information.pos
    
    @pos.setter
    def pos(self, value):
        """Default Setter implementation for :attr:`ScreenControlsInformationModel.POS`."""
        self.controls_information.pos = value
    
    
    @property
    def moving(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.MOVING`."""
        return self.controls_information.moving
    
    
    @property
    def en(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.EN`."""
        return self.controls_information.en
    
    @en.setter
    def en(self, value):
        """Default Setter implementation for :attr:`ScreenControlsInformationModel.EN`."""
        self.controls_information.en = value
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.V_POS`."""
        return self.controls_information.v_pos
    
    @v_pos.setter
    def v_pos(self, value):
        """Default Setter implementation for :attr:`ScreenControlsInformationModel.V_POS`."""
        self.controls_information.v_pos = value
    
    
    @property
    def v_actpos(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.V_ACTPOS`."""
        return self.controls_information.v_actpos
    
    
    @property
    def v_moving(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.V_MOVING`."""
        return self.controls_information.v_moving
    
    
    @property
    def v_en(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.V_EN`."""
        return self.controls_information.v_en
    
    @v_en.setter
    def v_en(self, value):
        """Default Setter implementation for :attr:`ScreenControlsInformationModel.V_EN`."""
        self.controls_information.v_en = value
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.H_POS`."""
        return self.controls_information.h_pos
    
    @h_pos.setter
    def h_pos(self, value):
        """Default Setter implementation for :attr:`ScreenControlsInformationModel.H_POS`."""
        self.controls_information.h_pos = value
    
    
    @property
    def h_actpos(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.H_ACTPOS`."""
        return self.controls_information.h_actpos
    
    
    @property
    def h_moving(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.H_MOVING`."""
        return self.controls_information.h_moving
    
    
    @property
    def h_en(self):
        """Default Getter implementation for :attr:`ScreenControlsInformationModel.H_EN`."""
        return self.controls_information.h_en
    
    @h_en.setter
    def h_en(self, value):
        """Default Setter implementation for :attr:`ScreenControlsInformationModel.H_EN`."""
        self.controls_information.h_en = value
    
    

class ScreenFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.screen.Screen` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(ScreenFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=ScreenModel,
            lattice_folder="Screen",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_screen(self, name: Union[str, List[str]] = None) -> ScreenModel:
        """
        Returns the screen object for the given name(s).

        :param name: Name(s) of the screen.
        :type name: str or list of str

        :return: Screen object(s).
        :rtype: :class:`screenModel.Screen`
        or Dict[str: :class:`screen.Screen`]
        """
        return self.get_hardware(name)

    
    def pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.POS`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.pos)
    
    def moving(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.MOVING`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.MOVING` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.moving)
    
    def en(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.EN`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.EN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.en)
    
    def v_pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.V_POS`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.V_POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.v_pos)
    
    def v_actpos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.V_ACTPOS`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.V_ACTPOS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.v_actpos)
    
    def v_moving(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.V_MOVING`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.V_MOVING` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.v_moving)
    
    def v_en(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.V_EN`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.V_EN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.v_en)
    
    def h_pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.H_POS`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.H_POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.h_pos)
    
    def h_actpos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.H_ACTPOS`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.H_ACTPOS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.h_actpos)
    
    def h_moving(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.H_MOVING`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.H_MOVING` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.h_moving)
    
    def h_en(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ScreenModel.H_EN`.

        :param name: Name(s) of the screen.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ScreenModel.H_EN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda screen: screen.h_en)
    