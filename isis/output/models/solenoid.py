
from catapcore.common.machine.pv_utils import ScalarPV, StatePV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class SolenoidPVMapModel(PVMap):
    
    
    SETI: ScalarPV
    
    """Sets the target current for a magnet power supply"""
    
    
    GETSETI: ScalarPV
    
    """Gets the value of the target current for a magnet power supply."""
    
    
    READI: ScalarPV
    
    """Gets the value of the actual current for a magnet power supply"""
    
    
    SETSTATE: StatePV
    
    """Sets the state of a power supply"""
    
    
    RESET: StatePV
    
    """Forces a reset of a power supply"""
    
    
    GETSTATE: ScalarPV
    
    """Danfysik 800 PSU Controller Solenoid 1 - Status"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        SolenoidPVMapModel.is_virtual = is_virtual
        SolenoidPVMapModel.connect_on_creation = connect_on_creation
        super(
            SolenoidPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def seti(self):
        """Default Getter implementation for SETI"""
        
        return self.SETI.get()
        

    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for SETI"""
        
        return self.SETI.put(value)
        
    
    
    @property
    def getseti(self):
        """Default Getter implementation for GETSETI"""
        
        return self.GETSETI.get()
        

    
    
    @property
    def readi(self):
        """Default Getter implementation for READI"""
        
        return self.READI.get()
        

    
    
    @property
    def setstate(self):
        """Default Getter implementation for SETSTATE"""
        
        return self.SETSTATE.get()
        

    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for SETSTATE"""
        
        return self.SETSTATE.put(value)
        
    
    
    @property
    def reset(self):
        """Default Getter implementation for RESET"""
        
        return self.RESET.get()
        

    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for RESET"""
        
        return self.RESET.put(value)
        
    
    
    @property
    def getstate(self):
        """Default Getter implementation for GETSTATE"""
        
        return self.GETSTATE.get()
        

    
    



class SolenoidControlsInformationModel(ControlsInformation):
    """
    Class for controlling a solenoid via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[SolenoidPVMapModel]

    

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
        SolenoidControlsInformationModel.is_virtual = is_virtual
        SolenoidControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            SolenoidControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> SolenoidPVMapModel:
        return SolenoidPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def seti(self):
        """Default Getter implementation for :attr:`SolenoidPVMapModel.SETI`."""    
        return self.pv_record_map.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`SolenoidPVMapModel.SETI`.""" 
        self.pv_record_map.seti = value
    
    
    @property
    def getseti(self):
        """Default Getter implementation for :attr:`SolenoidPVMapModel.GETSETI`."""    
        return self.pv_record_map.getseti
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`SolenoidPVMapModel.READI`."""    
        return self.pv_record_map.readi
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`SolenoidPVMapModel.SETSTATE`."""    
        return self.pv_record_map.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`SolenoidPVMapModel.SETSTATE`.""" 
        self.pv_record_map.setstate = value
    
    
    @property
    def reset(self):
        """Default Getter implementation for :attr:`SolenoidPVMapModel.RESET`."""    
        return self.pv_record_map.reset
    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for :attr:`SolenoidPVMapModel.RESET`.""" 
        self.pv_record_map.reset = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`SolenoidPVMapModel.GETSTATE`."""    
        return self.pv_record_map.getstate
    
    

    


class SolenoidPropertiesModel(Properties):
    """
    Class for defining solenoid-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    magnet_type: str
    
    
    
    max_i: int
    
    
    
    min_i: int
    
    
    
    manufacturer: str
    
    
    
    communications: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            SolenoidPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class SolenoidModel(Hardware):
    """
    Middle layer class for interacting with a specific solenoid object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[SolenoidControlsInformationModel]
    """Controls information pertaining to this solenoid
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[SolenoidPropertiesModel]
    """Properties pertaining to this solenoid
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""
    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            SolenoidModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            
            "SETI",
            
            "GETSETI",
            
            "READI",
            
            "SETSTATE",
            
            "RESET",
            
            "GETSTATE",
            
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> SolenoidControlsInformationModel:
        try:
            return SolenoidControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> SolenoidPropertiesModel:
        try:
            return SolenoidPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def seti(self):
        """Default Getter implementation for :attr:`SolenoidControlsInformationModel.SETI`."""
        return self.controls_information.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`SolenoidControlsInformationModel.SETI`."""
        self.controls_information.seti = value
    
    
    @property
    def getseti(self):
        """Default Getter implementation for :attr:`SolenoidControlsInformationModel.GETSETI`."""
        return self.controls_information.getseti
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`SolenoidControlsInformationModel.READI`."""
        return self.controls_information.readi
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`SolenoidControlsInformationModel.SETSTATE`."""
        return self.controls_information.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`SolenoidControlsInformationModel.SETSTATE`."""
        self.controls_information.setstate = value
    
    
    @property
    def reset(self):
        """Default Getter implementation for :attr:`SolenoidControlsInformationModel.RESET`."""
        return self.controls_information.reset
    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for :attr:`SolenoidControlsInformationModel.RESET`."""
        self.controls_information.reset = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`SolenoidControlsInformationModel.GETSTATE`."""
        return self.controls_information.getstate
    
    

class SolenoidFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.solenoid.Solenoid` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(SolenoidFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=SolenoidModel,
            lattice_folder="Solenoid",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_solenoid(self, name: Union[str, List[str]] = None) -> SolenoidModel:
        """
        Returns the solenoid object for the given name(s).

        :param name: Name(s) of the solenoid.
        :type name: str or list of str

        :return: Solenoid object(s).
        :rtype: :class:`solenoidModel.Solenoid`
        or Dict[str: :class:`solenoid.Solenoid`]
        """
        return self.get_hardware(name)

    
    def seti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`SolenoidModel.SETI`.

        :param name: Name(s) of the solenoid.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`SolenoidModel.SETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda solenoid: solenoid.seti)
    
    def getseti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`SolenoidModel.GETSETI`.

        :param name: Name(s) of the solenoid.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`SolenoidModel.GETSETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda solenoid: solenoid.getseti)
    
    def readi(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`SolenoidModel.READI`.

        :param name: Name(s) of the solenoid.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`SolenoidModel.READI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda solenoid: solenoid.readi)
    
    def setstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`SolenoidModel.SETSTATE`.

        :param name: Name(s) of the solenoid.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`SolenoidModel.SETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda solenoid: solenoid.setstate)
    
    def reset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`SolenoidModel.RESET`.

        :param name: Name(s) of the solenoid.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`SolenoidModel.RESET` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda solenoid: solenoid.reset)
    
    def getstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`SolenoidModel.GETSTATE`.

        :param name: Name(s) of the solenoid.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`SolenoidModel.GETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda solenoid: solenoid.getstate)
    