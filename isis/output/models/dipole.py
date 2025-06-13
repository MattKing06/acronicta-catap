
from catapcore.common.machine.pv_utils import ScalarPV, StatePV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class DipolePVMapModel(PVMap):
    
    
    SETI: ScalarPV
    
    """Sets the target current for a magnet power supply"""
    
    
    GETSETI: ScalarPV
    
    """Gets the value of the target current for a magnet power supply."""
    
    
    READI: ScalarPV
    
    """Gets the value of the actual current for a magnet power supply"""
    
    
    SETPOL: StatePV
    
    """Sets the value for the polarity of the power supply, used to switch from positive to negative"""
    
    
    READPOL: ScalarPV
    
    """Gets the value of the polarity of the magnet"""
    
    
    SETSTATE: StatePV
    
    """Sets the state of a power supply"""
    
    
    GETSTATE: ScalarPV
    
    """Danfysik 800 PSU Controller Dipole 1 X - Status"""
    
    
    RESET: StatePV
    
    """Forces a reset of a power supply"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        DipolePVMapModel.is_virtual = is_virtual
        DipolePVMapModel.connect_on_creation = connect_on_creation
        super(
            DipolePVMapModel,
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
    def setpol(self):
        """Default Getter implementation for SETPOL"""
        
        return self.SETPOL.get()
        

    
    @setpol.setter
    def setpol(self, value):
        """Default Setter implementation for SETPOL"""
        
        return self.SETPOL.put(value)
        
    
    
    @property
    def readpol(self):
        """Default Getter implementation for READPOL"""
        
        return self.READPOL.get()
        

    
    
    @property
    def setstate(self):
        """Default Getter implementation for SETSTATE"""
        
        return self.SETSTATE.get()
        

    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for SETSTATE"""
        
        return self.SETSTATE.put(value)
        
    
    
    @property
    def getstate(self):
        """Default Getter implementation for GETSTATE"""
        
        return self.GETSTATE.get()
        

    
    
    @property
    def reset(self):
        """Default Getter implementation for RESET"""
        
        return self.RESET.get()
        

    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for RESET"""
        
        return self.RESET.put(value)
        
    
    



class DipoleControlsInformationModel(ControlsInformation):
    """
    Class for controlling a dipole via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[DipolePVMapModel]

    

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
        DipoleControlsInformationModel.is_virtual = is_virtual
        DipoleControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            DipoleControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> DipolePVMapModel:
        return DipolePVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def seti(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.SETI`."""    
        return self.pv_record_map.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`DipolePVMapModel.SETI`.""" 
        self.pv_record_map.seti = value
    
    
    @property
    def getseti(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.GETSETI`."""    
        return self.pv_record_map.getseti
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.READI`."""    
        return self.pv_record_map.readi
    
    
    @property
    def setpol(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.SETPOL`."""    
        return self.pv_record_map.setpol
    
    @setpol.setter
    def setpol(self, value):
        """Default Setter implementation for :attr:`DipolePVMapModel.SETPOL`.""" 
        self.pv_record_map.setpol = value
    
    
    @property
    def readpol(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.READPOL`."""    
        return self.pv_record_map.readpol
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.SETSTATE`."""    
        return self.pv_record_map.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`DipolePVMapModel.SETSTATE`.""" 
        self.pv_record_map.setstate = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.GETSTATE`."""    
        return self.pv_record_map.getstate
    
    
    @property
    def reset(self):
        """Default Getter implementation for :attr:`DipolePVMapModel.RESET`."""    
        return self.pv_record_map.reset
    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for :attr:`DipolePVMapModel.RESET`.""" 
        self.pv_record_map.reset = value
    
    

    


class DipolePropertiesModel(Properties):
    """
    Class for defining dipole-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    magnet_type: str
    
    
    
    max_i: int
    
    
    
    min_i: int
    
    
    
    set_pol_positive: int
    
    
    
    read_pol_positive: int
    
    
    
    set_pol_negative: int
    
    
    
    read_pol_negative: int
    
    
    
    manufacturer: str
    
    
    
    communications: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            DipolePropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class DipoleModel(Hardware):
    """
    Middle layer class for interacting with a specific dipole object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[DipoleControlsInformationModel]
    """Controls information pertaining to this dipole
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[DipolePropertiesModel]
    """Properties pertaining to this dipole
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            DipoleModel,
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
    def validate_controls_information(cls, v: Any) -> DipoleControlsInformationModel:
        try:
            return DipoleControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> DipolePropertiesModel:
        try:
            return DipolePropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def seti(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.SETI`."""
        return self.controls_information.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`DipoleControlsInformationModel.SETI`."""
        self.controls_information.seti = value
    
    
    @property
    def getseti(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.GETSETI`."""
        return self.controls_information.getseti
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.READI`."""
        return self.controls_information.readi
    
    
    @property
    def setpol(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.SETPOL`."""
        return self.controls_information.setpol
    
    @setpol.setter
    def setpol(self, value):
        """Default Setter implementation for :attr:`DipoleControlsInformationModel.SETPOL`."""
        self.controls_information.setpol = value
    
    
    @property
    def readpol(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.READPOL`."""
        return self.controls_information.readpol
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.SETSTATE`."""
        return self.controls_information.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`DipoleControlsInformationModel.SETSTATE`."""
        self.controls_information.setstate = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.GETSTATE`."""
        return self.controls_information.getstate
    
    
    @property
    def reset(self):
        """Default Getter implementation for :attr:`DipoleControlsInformationModel.RESET`."""
        return self.controls_information.reset
    
    @reset.setter
    def reset(self, value):
        """Default Setter implementation for :attr:`DipoleControlsInformationModel.RESET`."""
        self.controls_information.reset = value
    
    

class DipoleFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.dipole.Dipole` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(DipoleFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=DipoleModel,
            lattice_folder="Dipole",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_dipole(self, name: Union[str, List[str]] = None) -> DipoleModel:
        """
        Returns the dipole object for the given name(s).

        :param name: Name(s) of the dipole.
        :type name: str or list of str

        :return: Dipole object(s).
        :rtype: :class:`dipoleModel.Dipole`
        or Dict[str: :class:`dipole.Dipole`]
        """
        return self.get_hardware(name)

    
    def seti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.SETI`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.SETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.seti)
    
    def getseti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.GETSETI`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.GETSETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.getseti)
    
    def readi(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.READI`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.READI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.readi)
    
    def setpol(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.SETPOL`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.SETPOL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.setpol)
    
    def readpol(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.READPOL`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.READPOL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.readpol)
    
    def setstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.SETSTATE`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.SETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.setstate)
    
    def getstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.GETSTATE`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.GETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.getstate)
    
    def reset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`DipoleModel.RESET`.

        :param name: Name(s) of the dipole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`DipoleModel.RESET` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda dipole: dipole.reset)
    