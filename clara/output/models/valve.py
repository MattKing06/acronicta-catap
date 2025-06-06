
from CATAP.common.machine.pv_utils import BinaryPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ValvePVMapModel(PVMap):
    
    
    Close: BinaryPV
    
    """Command PV to close the vacuum valve, activate signal must be sent after setting this PV."""
    
    
    Open: BinaryPV
    
    """Command PV to open the vacuum valve, activate signal must be sent after setting this PV."""
    
    
    Sta: StatePV
    
    """Reports back the current state of the vacuum valve."""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ValvePVMapModel.is_virtual = is_virtual
        ValvePVMapModel.connect_on_creation = connect_on_creation
        super(
            ValvePVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def close(self):
        """Default Getter implementation for Close"""
        
        return self.Close.get()
        

    
    @close.setter
    def close(self, value):
        """Default Setter implementation for Close"""
        
        return self.Close.put(value)
        
    
    
    @property
    def open(self):
        """Default Getter implementation for Open"""
        
        return self.Open.get()
        

    
    @open.setter
    def open(self, value):
        """Default Setter implementation for Open"""
        
        return self.Open.put(value)
        
    
    
    @property
    def sta(self):
        """Default Getter implementation for Sta"""
        
        return self.Sta.get()
        

    
    



class ValveControlsInformationModel(ControlsInformation):
    """
    Class for controlling a valve via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ValvePVMapModel]

    

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
        ValveControlsInformationModel.is_virtual = is_virtual
        ValveControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            ValveControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ValvePVMapModel:
        return ValvePVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def close(self):
        """Default Getter implementation for :attr:`ValvePVMapModel.Close`."""    
        return self.pv_record_map.close
    
    @close.setter
    def close(self, value):
        """Default Setter implementation for :attr:`ValvePVMapModel.Close`.""" 
        self.pv_record_map.close = value
    
    
    @property
    def open(self):
        """Default Getter implementation for :attr:`ValvePVMapModel.Open`."""    
        return self.pv_record_map.open
    
    @open.setter
    def open(self, value):
        """Default Setter implementation for :attr:`ValvePVMapModel.Open`.""" 
        self.pv_record_map.open = value
    
    
    @property
    def sta(self):
        """Default Getter implementation for :attr:`ValvePVMapModel.Sta`."""    
        return self.pv_record_map.sta
    
    

    


class ValvePropertiesModel(Properties):
    """
    Class for defining valve-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    valve_set_max_wait_time: float
    
    
    
    subtype: str
    
    
    
    virtual_name: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            ValvePropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class ValveModel(Hardware):
    """
    Middle layer class for interacting with a specific valve object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ValveControlsInformationModel]
    """Controls information pertaining to this valve
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ValvePropertiesModel]
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
            ValveModel,
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
    def validate_controls_information(cls, v: Any) -> ValveControlsInformationModel:
        try:
            return ValveControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ValvePropertiesModel:
        try:
            return ValvePropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def close(self):
        """Default Getter implementation for :attr:`ValveControlsInformationModel.Close`."""
        return self.controls_information.close
    
    @close.setter
    def close(self, value):
        """Default Setter implementation for :attr:`ValveControlsInformationModel.Close`."""
        self.controls_information.close = value
    
    
    @property
    def open(self):
        """Default Getter implementation for :attr:`ValveControlsInformationModel.Open`."""
        return self.controls_information.open
    
    @open.setter
    def open(self, value):
        """Default Setter implementation for :attr:`ValveControlsInformationModel.Open`."""
        self.controls_information.open = value
    
    
    @property
    def sta(self):
        """Default Getter implementation for :attr:`ValveControlsInformationModel.Sta`."""
        return self.controls_information.sta
    
    

class ValveFactoryModel(Factory):
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
        super(ValveFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=ValveModel,
            lattice_folder="Valve",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_valve(self, name: Union[str, List[str]] = None) -> ValveModel:
        """
        Returns the valve object for the given name(s).

        :param name: Name(s) of the valve.
        :type name: str or list of str

        :return: Valve object(s).
        :rtype: :class:`valveModel.Valve`
        or Dict[str: :class:`valve.Valve`]
        """
        return self.get_hardware(name)

    
    def close(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ValveModel.Close`.

        :param name: Name(s) of the valve.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ValveModel.Close` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda valve: valve.close)
    
    def open(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ValveModel.Open`.

        :param name: Name(s) of the valve.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ValveModel.Open` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda valve: valve.open)
    
    def sta(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ValveModel.Sta`.

        :param name: Name(s) of the valve.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ValveModel.Sta` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda valve: valve.sta)
    