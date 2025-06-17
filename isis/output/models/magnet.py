
from catapcore.common.machine.pv_utils import ScalarPV, StatePV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class MagnetPVMapModel(PVMap):
    
    
    SETI: ScalarPV
    
    """Sets the target current for a magnet power supply"""
    
    
    GETSETI: ScalarPV = None
    
    """Gets the value of the target current for a magnet power supply."""
    
    
    READI: ScalarPV
    
    """Gets the value of the actual current for a magnet power supply"""
    
    
    SETSTATE: StatePV
    
    """Sets the state of a power supply"""
    
    
    RESET: StatePV = None
    
    """Forces a reset of a power supply"""
    
    
    GETSTATE: ScalarPV
    
    """Danfysik 800 PSU Controller Dipole 1 X - Status"""
    
    
    SETPOL: StatePV = None
    
    """Sets the value for the polarity of the power supply, used to switch from positive to negative"""
    
    
    READPOL: ScalarPV = None
    
    """Gets the value of the polarity of the magnet"""
    
    
    READV: ScalarPV = None
    
    """Gets the value of the actual voltage for a magnet power supply"""
    

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
        
        if self.GETSETI:
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
        
        if self.RESET:
            return self.RESET.get()
        

    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for RESET"""
        
        if self.RESET:
            return self.RESET.put(value)
        
    
    
    @property
    def getstate(self):
        """Default Getter implementation for GETSTATE"""
        
        return self.GETSTATE.get()
        

    
    
    @property
    def setpol(self):
        """Default Getter implementation for SETPOL"""
        
        if self.SETPOL:
            return self.SETPOL.get()
        

    
    @setpol.setter
    def setpol(self, value):
        """Default Setter implementation for SETPOL"""
        
        if self.SETPOL:
            return self.SETPOL.put(value)
        
    
    
    @property
    def readpol(self):
        """Default Getter implementation for READPOL"""
        
        if self.READPOL:
            return self.READPOL.get()
        

    
    
    @property
    def readv(self):
        """Default Getter implementation for READV"""
        
        if self.READV:
            return self.READV.get()
        

    
    



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
    def seti(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.SETI`."""    
        return self.pv_record_map.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.SETI`.""" 
        self.pv_record_map.seti = value
    
    
    @property
    def getseti(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.GETSETI`."""    
        return self.pv_record_map.getseti
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.READI`."""    
        return self.pv_record_map.readi
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.SETSTATE`."""    
        return self.pv_record_map.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.SETSTATE`.""" 
        self.pv_record_map.setstate = value
    
    
    @property
    def reset(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.RESET`."""    
        return self.pv_record_map.reset
    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.RESET`.""" 
        self.pv_record_map.reset = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.GETSTATE`."""    
        return self.pv_record_map.getstate
    
    
    @property
    def setpol(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.SETPOL`."""    
        return self.pv_record_map.setpol
    
    @setpol.setter
    def setpol(self, value):
        """Default Setter implementation for :attr:`MagnetPVMapModel.SETPOL`.""" 
        self.pv_record_map.setpol = value
    
    
    @property
    def readpol(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.READPOL`."""    
        return self.pv_record_map.readpol
    
    
    @property
    def readv(self):
        """Default Getter implementation for :attr:`MagnetPVMapModel.READV`."""    
        return self.pv_record_map.readv
    
    

    


class MagnetPropertiesModel(Properties):
    """
    Class for defining magnet-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    subtype: str
    
    
    
    max_i: int
    
    
    
    min_i: int
    
    
    
    manufacturer: str
    
    
    
    communications: str
    
    
    
    set_pol_positive: int = None
    
    
    
    read_pol_positive: int = None
    
    
    
    set_pol_negative: int = None
    
    
    
    read_pol_negative: int = None
    
    

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
            
            "SETI",
            
            "GETSETI",
            
            "READI",
            
            "SETSTATE",
            
            "RESET",
            
            "GETSTATE",
            
            "SETPOL",
            
            "READPOL",
            
            "READV",
            
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
    def seti(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.SETI`."""
        return self.controls_information.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.SETI`."""
        self.controls_information.seti = value
    
    
    @property
    def getseti(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.GETSETI`."""
        return self.controls_information.getseti
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.READI`."""
        return self.controls_information.readi
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.SETSTATE`."""
        return self.controls_information.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.SETSTATE`."""
        self.controls_information.setstate = value
    
    
    @property
    def reset(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.RESET`."""
        return self.controls_information.reset
    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.RESET`."""
        self.controls_information.reset = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.GETSTATE`."""
        return self.controls_information.getstate
    
    
    @property
    def setpol(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.SETPOL`."""
        return self.controls_information.setpol
    
    @setpol.setter
    def setpol(self, value):
        """Default Setter implementation for :attr:`MagnetControlsInformationModel.SETPOL`."""
        self.controls_information.setpol = value
    
    
    @property
    def readpol(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.READPOL`."""
        return self.controls_information.readpol
    
    
    @property
    def readv(self):
        """Default Getter implementation for :attr:`MagnetControlsInformationModel.READV`."""
        return self.controls_information.readv
    
    

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

    
    def seti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.SETI`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.SETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.seti)
    
    def getseti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.GETSETI`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.GETSETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.getseti)
    
    def readi(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.READI`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.READI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readi)
    
    def setstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.SETSTATE`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.SETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.setstate)
    
    def reset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.RESET`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.RESET` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.reset)
    
    def getstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.GETSTATE`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.GETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.getstate)
    
    def setpol(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.SETPOL`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.SETPOL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.setpol)
    
    def readpol(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.READPOL`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.READPOL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readpol)
    
    def readv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MagnetModel.READV`.

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MagnetModel.READV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readv)
    