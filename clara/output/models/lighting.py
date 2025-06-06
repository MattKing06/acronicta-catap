
from CATAP.common.machine.pv_utils import PV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class LightingPVMapModel(PVMap):
    
    
    ACCELERATOR_HALL_LIGHT_Off: PV
    
    """"""
    
    
    ACCELERATOR_HALL_LIGHT_On: PV
    
    """"""
    
    
    ACCELERATOR_HALL_LIGHT_Sta: PV
    
    """"""
    
    
    CLARA_LED_Off: PV
    
    """"""
    
    
    CLARA_LED_On: PV
    
    """"""
    
    
    CLARA_LED_Sta: PV
    
    """"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        LightingPVMapModel.is_virtual = is_virtual
        LightingPVMapModel.connect_on_creation = connect_on_creation
        super(
            LightingPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def accelerator_hall_light_off(self):
        """Default Getter implementation for ACCELERATOR_HALL_LIGHT_Off"""
        
        return self.ACCELERATOR_HALL_LIGHT_Off.get()
        

    
    
    @property
    def accelerator_hall_light_on(self):
        """Default Getter implementation for ACCELERATOR_HALL_LIGHT_On"""
        
        return self.ACCELERATOR_HALL_LIGHT_On.get()
        

    
    
    @property
    def accelerator_hall_light_sta(self):
        """Default Getter implementation for ACCELERATOR_HALL_LIGHT_Sta"""
        
        return self.ACCELERATOR_HALL_LIGHT_Sta.get()
        

    
    
    @property
    def clara_led_off(self):
        """Default Getter implementation for CLARA_LED_Off"""
        
        return self.CLARA_LED_Off.get()
        

    
    
    @property
    def clara_led_on(self):
        """Default Getter implementation for CLARA_LED_On"""
        
        return self.CLARA_LED_On.get()
        

    
    
    @property
    def clara_led_sta(self):
        """Default Getter implementation for CLARA_LED_Sta"""
        
        return self.CLARA_LED_Sta.get()
        

    
    



class LightingControlsInformationModel(ControlsInformation):
    """
    Class for controlling a lighting via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[LightingPVMapModel]

    
    
    PV: bool
    
    

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
        LightingControlsInformationModel.is_virtual = is_virtual
        LightingControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            LightingControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> LightingPVMapModel:
        return LightingPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def accelerator_hall_light_off(self):
        """Default Getter implementation for :attr:`LightingPVMapModel.ACCELERATOR_HALL_LIGHT_Off`."""    
        return self.pv_record_map.accelerator_hall_light_off
    
    
    @property
    def accelerator_hall_light_on(self):
        """Default Getter implementation for :attr:`LightingPVMapModel.ACCELERATOR_HALL_LIGHT_On`."""    
        return self.pv_record_map.accelerator_hall_light_on
    
    
    @property
    def accelerator_hall_light_sta(self):
        """Default Getter implementation for :attr:`LightingPVMapModel.ACCELERATOR_HALL_LIGHT_Sta`."""    
        return self.pv_record_map.accelerator_hall_light_sta
    
    
    @property
    def clara_led_off(self):
        """Default Getter implementation for :attr:`LightingPVMapModel.CLARA_LED_Off`."""    
        return self.pv_record_map.clara_led_off
    
    
    @property
    def clara_led_on(self):
        """Default Getter implementation for :attr:`LightingPVMapModel.CLARA_LED_On`."""    
        return self.pv_record_map.clara_led_on
    
    
    @property
    def clara_led_sta(self):
        """Default Getter implementation for :attr:`LightingPVMapModel.CLARA_LED_Sta`."""    
        return self.pv_record_map.clara_led_sta
    
    

    
    @property
    def pv(self) -> bool:
        """Default Getter implementation for PV."""
        
        return self.PV
        
    


class LightingPropertiesModel(Properties):
    """
    Class for defining lighting-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    

    def __init__(self, *args, **kwargs):
        super(
            LightingPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class LightingModel(Hardware):
    """
    Middle layer class for interacting with a specific lighting object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[LightingControlsInformationModel]
    """Controls information pertaining to this lighting
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[LightingPropertiesModel]
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
            LightingModel,
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
    def validate_controls_information(cls, v: Any) -> LightingControlsInformationModel:
        try:
            return LightingControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> LightingPropertiesModel:
        try:
            return LightingPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def accelerator_hall_light_off(self):
        """Default Getter implementation for :attr:`LightingControlsInformationModel.ACCELERATOR_HALL_LIGHT_Off`."""
        return self.controls_information.accelerator_hall_light_off
    
    
    @property
    def accelerator_hall_light_on(self):
        """Default Getter implementation for :attr:`LightingControlsInformationModel.ACCELERATOR_HALL_LIGHT_On`."""
        return self.controls_information.accelerator_hall_light_on
    
    
    @property
    def accelerator_hall_light_sta(self):
        """Default Getter implementation for :attr:`LightingControlsInformationModel.ACCELERATOR_HALL_LIGHT_Sta`."""
        return self.controls_information.accelerator_hall_light_sta
    
    
    @property
    def clara_led_off(self):
        """Default Getter implementation for :attr:`LightingControlsInformationModel.CLARA_LED_Off`."""
        return self.controls_information.clara_led_off
    
    
    @property
    def clara_led_on(self):
        """Default Getter implementation for :attr:`LightingControlsInformationModel.CLARA_LED_On`."""
        return self.controls_information.clara_led_on
    
    
    @property
    def clara_led_sta(self):
        """Default Getter implementation for :attr:`LightingControlsInformationModel.CLARA_LED_Sta`."""
        return self.controls_information.clara_led_sta
    
    

class LightingFactoryModel(Factory):
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
        super(LightingFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=LightingModel,
            lattice_folder="Lighting",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_lighting(self, name: Union[str, List[str]] = None) -> LightingModel:
        """
        Returns the lighting object for the given name(s).

        :param name: Name(s) of the lighting.
        :type name: str or list of str

        :return: Lighting object(s).
        :rtype: :class:`lightingModel.Lighting`
        or Dict[str: :class:`lighting.Lighting`]
        """
        return self.get_hardware(name)

    
    def accelerator_hall_light_off(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LightingModel.ACCELERATOR_HALL_LIGHT_Off`.

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LightingModel.ACCELERATOR_HALL_LIGHT_Off` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.accelerator_hall_light_off)
    
    def accelerator_hall_light_on(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LightingModel.ACCELERATOR_HALL_LIGHT_On`.

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LightingModel.ACCELERATOR_HALL_LIGHT_On` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.accelerator_hall_light_on)
    
    def accelerator_hall_light_sta(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LightingModel.ACCELERATOR_HALL_LIGHT_Sta`.

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LightingModel.ACCELERATOR_HALL_LIGHT_Sta` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.accelerator_hall_light_sta)
    
    def clara_led_off(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LightingModel.CLARA_LED_Off`.

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LightingModel.CLARA_LED_Off` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.clara_led_off)
    
    def clara_led_on(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LightingModel.CLARA_LED_On`.

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LightingModel.CLARA_LED_On` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.clara_led_on)
    
    def clara_led_sta(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LightingModel.CLARA_LED_Sta`.

        :param name: Name(s) of the lighting.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LightingModel.CLARA_LED_Sta` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lighting: lighting.clara_led_sta)
    