
from CATAP.common.machine.pv_utils import PV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class LightingPVMap(PVMap):
    
    ACCELERATOR_HALL_LIGHT_Off: PV
    
    ACCELERATOR_HALL_LIGHT_On: PV
    
    ACCELERATOR_HALL_LIGHT_Sta: PV
    
    CLARA_LED_Off: PV
    
    CLARA_LED_On: PV
    
    CLARA_LED_Sta: PV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        LightingPVMap.is_virtual = is_virtual
        LightingPVMap.connect_on_creation = connect_on_creation
        super(
            LightingPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def accelerator_hall_light_off(self):
        return self.ACCELERATOR_HALL_LIGHT_Off.get()
    
    
    @property
    def accelerator_hall_light_on(self):
        return self.ACCELERATOR_HALL_LIGHT_On.get()
    
    
    @property
    def accelerator_hall_light_sta(self):
        return self.ACCELERATOR_HALL_LIGHT_Sta.get()
    
    
    @property
    def clara_led_off(self):
        return self.CLARA_LED_Off.get()
    
    
    @property
    def clara_led_on(self):
        return self.CLARA_LED_On.get()
    
    
    @property
    def clara_led_sta(self):
        return self.CLARA_LED_Sta.get()
    
    



class LightingControlsInformation(ControlsInformation):
    """
    Class for controlling a lighting via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[LightingPVMap]
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
        LightingControlsInformation.is_virtual = is_virtual
        LightingControlsInformation.connect_on_creation = connect_on_creation
        super(
            LightingControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> LightingPVMap:
        return LightingPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def accelerator_hall_light_off(self):
        return self.pv_record_map.accelerator_hall_light_off
    
    
    @property
    def accelerator_hall_light_on(self):
        return self.pv_record_map.accelerator_hall_light_on
    
    
    @property
    def accelerator_hall_light_sta(self):
        return self.pv_record_map.accelerator_hall_light_sta
    
    
    @property
    def clara_led_off(self):
        return self.pv_record_map.clara_led_off
    
    
    @property
    def clara_led_on(self):
        return self.pv_record_map.clara_led_on
    
    
    @property
    def clara_led_sta(self):
        return self.pv_record_map.clara_led_sta
    
    


class LightingProperties(Properties):
    """
    Class for defining lighting-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    

    def __init__(self, *args, **kwargs):
        super(
            LightingProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    

    

class Lighting(Hardware):
    """
    Middle layer class for interacting with a specific lighting object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[LightingControlsInformation]
    """Controls information pertaining to this lighting
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[LightingProperties]
    """Properties pertaining to this lighting
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Lighting,
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
    def validate_controls_information(cls, v: Any) -> LightingControlsInformation:
        try:
            return LightingControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> LightingProperties:
        try:
            return LightingProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def accelerator_hall_light_off(self):
        return self.controls_information.accelerator_hall_light_off
    
    
    @property
    def accelerator_hall_light_on(self):
        return self.controls_information.accelerator_hall_light_on
    
    
    @property
    def accelerator_hall_light_sta(self):
        return self.controls_information.accelerator_hall_light_sta
    
    
    @property
    def clara_led_off(self):
        return self.controls_information.clara_led_off
    
    
    @property
    def clara_led_on(self):
        return self.controls_information.clara_led_on
    
    
    @property
    def clara_led_sta(self):
        return self.controls_information.clara_led_sta
    
    

class LightingFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.lighting.Lighting` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(LightingFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Lighting,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_lighting(self, name: Union[str, List[str]] = None) -> Lighting:
        """
        Returns the lighting object for the given name(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str

        :return: Lighting object(s).
        :rtype: :class:`~CATAP.laser.components.lighting.Lighting`
        or Dict[str: :class:`~CATAP.laser.components.lighting.Lighting`]
        """
        return self.get_hardware(name)

    
    def accelerator_hall_light_off(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'accelerator_hall_light_off' property of the lighting(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the 'ACCELERATOR_HALL_LIGHT_Off' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.accelerator_hall_light_off)
    
    def accelerator_hall_light_on(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'accelerator_hall_light_on' property of the lighting(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the 'ACCELERATOR_HALL_LIGHT_On' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.accelerator_hall_light_on)
    
    def accelerator_hall_light_sta(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'accelerator_hall_light_sta' property of the lighting(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the 'ACCELERATOR_HALL_LIGHT_Sta' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.accelerator_hall_light_sta)
    
    def clara_led_off(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'clara_led_off' property of the lighting(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the 'CLARA_LED_Off' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.clara_led_off)
    
    def clara_led_on(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'clara_led_on' property of the lighting(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the 'CLARA_LED_On' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.clara_led_on)
    
    def clara_led_sta(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'clara_led_sta' property of the lighting(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the 'CLARA_LED_Sta' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.clara_led_sta)
    