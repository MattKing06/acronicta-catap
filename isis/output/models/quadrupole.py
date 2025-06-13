
from catapcore.common.machine.pv_utils import ScalarPV, StatePV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class QuadrupolePVMapModel(PVMap):
    
    
    SETI: ScalarPV
    
    """Sets the target current for a magnet power supply"""
    
    
    READI: ScalarPV
    
    """Gets the value of the actual current for a magnet power supply"""
    
    
    READV: ScalarPV
    
    """Gets the value of the actual voltage for a magnet power supply"""
    
    
    SETSTATE: StatePV
    
    """Sets the state of a power supply"""
    
    
    GETSTATE: ScalarPV
    
    """reads the state of a power supple"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        QuadrupolePVMapModel.is_virtual = is_virtual
        QuadrupolePVMapModel.connect_on_creation = connect_on_creation
        super(
            QuadrupolePVMapModel,
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
    def readi(self):
        """Default Getter implementation for READI"""
        
        return self.READI.get()
        

    
    
    @property
    def readv(self):
        """Default Getter implementation for READV"""
        
        return self.READV.get()
        

    
    
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
        

    
    



class QuadrupoleControlsInformationModel(ControlsInformation):
    """
    Class for controlling a quadrupole via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[QuadrupolePVMapModel]

    

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
        QuadrupoleControlsInformationModel.is_virtual = is_virtual
        QuadrupoleControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            QuadrupoleControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> QuadrupolePVMapModel:
        return QuadrupolePVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def seti(self):
        """Default Getter implementation for :attr:`QuadrupolePVMapModel.SETI`."""    
        return self.pv_record_map.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`QuadrupolePVMapModel.SETI`.""" 
        self.pv_record_map.seti = value
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`QuadrupolePVMapModel.READI`."""    
        return self.pv_record_map.readi
    
    
    @property
    def readv(self):
        """Default Getter implementation for :attr:`QuadrupolePVMapModel.READV`."""    
        return self.pv_record_map.readv
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`QuadrupolePVMapModel.SETSTATE`."""    
        return self.pv_record_map.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`QuadrupolePVMapModel.SETSTATE`.""" 
        self.pv_record_map.setstate = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`QuadrupolePVMapModel.GETSTATE`."""    
        return self.pv_record_map.getstate
    
    

    


class QuadrupolePropertiesModel(Properties):
    """
    Class for defining quadrupole-specific properties.

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
            QuadrupolePropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class QuadrupoleModel(Hardware):
    """
    Middle layer class for interacting with a specific quadrupole object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[QuadrupoleControlsInformationModel]
    """Controls information pertaining to this quadrupole
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[QuadrupolePropertiesModel]
    """Properties pertaining to this quadrupole
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            QuadrupoleModel,
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
    def validate_controls_information(cls, v: Any) -> QuadrupoleControlsInformationModel:
        try:
            return QuadrupoleControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> QuadrupolePropertiesModel:
        try:
            return QuadrupolePropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def seti(self):
        """Default Getter implementation for :attr:`QuadrupoleControlsInformationModel.SETI`."""
        return self.controls_information.seti
    
    @seti.setter
    def seti(self, value):
        """Default Setter implementation for :attr:`QuadrupoleControlsInformationModel.SETI`."""
        self.controls_information.seti = value
    
    
    @property
    def readi(self):
        """Default Getter implementation for :attr:`QuadrupoleControlsInformationModel.READI`."""
        return self.controls_information.readi
    
    
    @property
    def readv(self):
        """Default Getter implementation for :attr:`QuadrupoleControlsInformationModel.READV`."""
        return self.controls_information.readv
    
    
    @property
    def setstate(self):
        """Default Getter implementation for :attr:`QuadrupoleControlsInformationModel.SETSTATE`."""
        return self.controls_information.setstate
    
    @setstate.setter
    def setstate(self, value):
        """Default Setter implementation for :attr:`QuadrupoleControlsInformationModel.SETSTATE`."""
        self.controls_information.setstate = value
    
    
    @property
    def getstate(self):
        """Default Getter implementation for :attr:`QuadrupoleControlsInformationModel.GETSTATE`."""
        return self.controls_information.getstate
    
    

class QuadrupoleFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.quadrupole.Quadrupole` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(QuadrupoleFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=QuadrupoleModel,
            lattice_folder="Quadrupole",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_quadrupole(self, name: Union[str, List[str]] = None) -> QuadrupoleModel:
        """
        Returns the quadrupole object for the given name(s).

        :param name: Name(s) of the quadrupole.
        :type name: str or list of str

        :return: Quadrupole object(s).
        :rtype: :class:`quadrupoleModel.Quadrupole`
        or Dict[str: :class:`quadrupole.Quadrupole`]
        """
        return self.get_hardware(name)

    
    def seti(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`QuadrupoleModel.SETI`.

        :param name: Name(s) of the quadrupole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`QuadrupoleModel.SETI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda quadrupole: quadrupole.seti)
    
    def readi(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`QuadrupoleModel.READI`.

        :param name: Name(s) of the quadrupole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`QuadrupoleModel.READI` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda quadrupole: quadrupole.readi)
    
    def readv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`QuadrupoleModel.READV`.

        :param name: Name(s) of the quadrupole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`QuadrupoleModel.READV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda quadrupole: quadrupole.readv)
    
    def setstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`QuadrupoleModel.SETSTATE`.

        :param name: Name(s) of the quadrupole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`QuadrupoleModel.SETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda quadrupole: quadrupole.setstate)
    
    def getstate(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`QuadrupoleModel.GETSTATE`.

        :param name: Name(s) of the quadrupole.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`QuadrupoleModel.GETSTATE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda quadrupole: quadrupole.getstate)
    