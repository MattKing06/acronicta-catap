
from CATAP.common.machine.pv_utils import BinaryPV, StatePV, ScalarPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ShutterPVMapModel(PVMap):
    
    
    SetPos: BinaryPV = None
    
    """Command to open the shutter"""
    
    
    State: StatePV
    
    """Current state of the shutter"""
    
    
    Close: BinaryPV = None
    
    """Command to close the shutter"""
    
    
    Cmi: ScalarPV = None
    
    """Integer that is converted into bits to represent interlock statuses
"""
    
    
    Open: BinaryPV = None
    
    """Command to open the shutter"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ShutterPVMapModel.is_virtual = is_virtual
        ShutterPVMapModel.connect_on_creation = connect_on_creation
        super(
            ShutterPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def setpos(self):
        """Default Getter implementation for SetPos"""
        
        if self.SetPos:
            return self.SetPos.get()
        

    
    @setpos.setter
    def setpos(self, value):
        """Default Setter implementation for SetPos"""
        
        if self.SetPos:
            return self.SetPos.put(value)
        
    
    
    @property
    def state(self):
        """Default Getter implementation for State"""
        
        return self.State.get()
        

    
    
    @property
    def close(self):
        """Default Getter implementation for Close"""
        
        if self.Close:
            return self.Close.get()
        

    
    @close.setter
    def close(self, value):
        """Default Setter implementation for Close"""
        
        if self.Close:
            return self.Close.put(value)
        
    
    
    @property
    def cmi(self):
        """Default Getter implementation for Cmi"""
        
        if self.Cmi:
            return self.Cmi.get()
        

    
    
    @property
    def open(self):
        """Default Getter implementation for Open"""
        
        if self.Open:
            return self.Open.get()
        

    
    @open.setter
    def open(self, value):
        """Default Setter implementation for Open"""
        
        if self.Open:
            return self.Open.put(value)
        
    
    



class ShutterControlsInformationModel(ControlsInformation):
    """
    Class for controlling a shutter via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ShutterPVMapModel]

    
    
    shutter_type: str
    
    

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
        ShutterControlsInformationModel.is_virtual = is_virtual
        ShutterControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            ShutterControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ShutterPVMapModel:
        return ShutterPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def setpos(self):
        """Default Getter implementation for :attr:`ShutterPVMapModel.SetPos`."""    
        return self.pv_record_map.setpos
    
    @setpos.setter
    def setpos(self, value):
        """Default Setter implementation for :attr:`ShutterPVMapModel.SetPos`.""" 
        self.pv_record_map.setpos = value
    
    
    @property
    def state(self):
        """Default Getter implementation for :attr:`ShutterPVMapModel.State`."""    
        return self.pv_record_map.state
    
    
    @property
    def close(self):
        """Default Getter implementation for :attr:`ShutterPVMapModel.Close`."""    
        return self.pv_record_map.close
    
    @close.setter
    def close(self, value):
        """Default Setter implementation for :attr:`ShutterPVMapModel.Close`.""" 
        self.pv_record_map.close = value
    
    
    @property
    def cmi(self):
        """Default Getter implementation for :attr:`ShutterPVMapModel.Cmi`."""    
        return self.pv_record_map.cmi
    
    
    @property
    def open(self):
        """Default Getter implementation for :attr:`ShutterPVMapModel.Open`."""    
        return self.pv_record_map.open
    
    @open.setter
    def open(self, value):
        """Default Setter implementation for :attr:`ShutterPVMapModel.Open`.""" 
        self.pv_record_map.open = value
    
    

    
    @property
    def shutter_type(self) -> str:
        """Default Getter implementation for shutter_type."""
        
        return self.shutter_type
        
    


class ShutterPropertiesModel(Properties):
    """
    Class for defining shutter-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    shutter_set_max_wait_time: float
    
    
    
    subtype: str
    
    
    
    virtual_name: str
    
    
    
    shutter_interlock_names: str = None
    
    

    def __init__(self, *args, **kwargs):
        super(
            ShutterPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class ShutterModel(Hardware):
    """
    Middle layer class for interacting with a specific shutter object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ShutterControlsInformationModel]
    """Controls information pertaining to this shutter
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ShutterPropertiesModel]
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
            ShutterModel,
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
    def validate_controls_information(cls, v: Any) -> ShutterControlsInformationModel:
        try:
            return ShutterControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ShutterPropertiesModel:
        try:
            return ShutterPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def setpos(self):
        """Default Getter implementation for :attr:`ShutterControlsInformationModel.SetPos`."""
        return self.controls_information.setpos
    
    @setpos.setter
    def setpos(self, value):
        """Default Setter implementation for :attr:`ShutterControlsInformationModel.SetPos`."""
        self.controls_information.setpos = value
    
    
    @property
    def state(self):
        """Default Getter implementation for :attr:`ShutterControlsInformationModel.State`."""
        return self.controls_information.state
    
    
    @property
    def close(self):
        """Default Getter implementation for :attr:`ShutterControlsInformationModel.Close`."""
        return self.controls_information.close
    
    @close.setter
    def close(self, value):
        """Default Setter implementation for :attr:`ShutterControlsInformationModel.Close`."""
        self.controls_information.close = value
    
    
    @property
    def cmi(self):
        """Default Getter implementation for :attr:`ShutterControlsInformationModel.Cmi`."""
        return self.controls_information.cmi
    
    
    @property
    def open(self):
        """Default Getter implementation for :attr:`ShutterControlsInformationModel.Open`."""
        return self.controls_information.open
    
    @open.setter
    def open(self, value):
        """Default Setter implementation for :attr:`ShutterControlsInformationModel.Open`."""
        self.controls_information.open = value
    
    

class ShutterFactoryModel(Factory):
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
        super(ShutterFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=ShutterModel,
            lattice_folder="Shutter",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_shutter(self, name: Union[str, List[str]] = None) -> ShutterModel:
        """
        Returns the shutter object for the given name(s).

        :param name: Name(s) of the shutter.
        :type name: str or list of str

        :return: Shutter object(s).
        :rtype: :class:`shutterModel.Shutter`
        or Dict[str: :class:`shutter.Shutter`]
        """
        return self.get_hardware(name)

    
    def setpos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ShutterModel.SetPos`.

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ShutterModel.SetPos` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.setpos)
    
    def state(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ShutterModel.State`.

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ShutterModel.State` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.state)
    
    def close(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ShutterModel.Close`.

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ShutterModel.Close` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.close)
    
    def cmi(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ShutterModel.Cmi`.

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ShutterModel.Cmi` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.cmi)
    
    def open(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ShutterModel.Open`.

        :param name: Name(s) of the shutter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ShutterModel.Open` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda shutter: shutter.open)
    