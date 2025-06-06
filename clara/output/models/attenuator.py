
from CATAP.common.machine.pv_utils import BinaryPV, ScalarPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class AttenuatorPVMapModel(PVMap):
    
    
    ENABLE: BinaryPV
    
    """Send a move command to the attenuator"""
    
    
    ROT_MABS: ScalarPV
    
    """Sets the step-size to move the attenuator"""
    
    
    ROT_RPOS: ScalarPV
    
    """The readback of the attenuator position"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        AttenuatorPVMapModel.is_virtual = is_virtual
        AttenuatorPVMapModel.connect_on_creation = connect_on_creation
        super(
            AttenuatorPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def enable(self):
        """Default Getter implementation for ENABLE"""
        
        return self.ENABLE.get()
        

    
    @enable.setter
    def enable(self, value):
        """Default Setter implementation for ENABLE"""
        
        return self.ENABLE.put(value)
        
    
    
    @property
    def rot_mabs(self):
        """Default Getter implementation for ROT_MABS"""
        
        return self.ROT_MABS.get()
        

    
    @rot_mabs.setter
    def rot_mabs(self, value):
        """Default Setter implementation for ROT_MABS"""
        
        return self.ROT_MABS.put(value)
        
    
    
    @property
    def rot_rpos(self):
        """Default Getter implementation for ROT_RPOS"""
        
        return self.ROT_RPOS.get()
        

    
    



class AttenuatorControlsInformationModel(ControlsInformation):
    """
    Class for controlling a attenuator via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[AttenuatorPVMapModel]

    

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
        AttenuatorControlsInformationModel.is_virtual = is_virtual
        AttenuatorControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            AttenuatorControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> AttenuatorPVMapModel:
        return AttenuatorPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def enable(self):
        """Default Getter implementation for :attr:`AttenuatorPVMapModel.ENABLE`."""    
        return self.pv_record_map.enable
    
    @enable.setter
    def enable(self, value):
        """Default Setter implementation for :attr:`AttenuatorPVMapModel.ENABLE`.""" 
        self.pv_record_map.enable = value
    
    
    @property
    def rot_mabs(self):
        """Default Getter implementation for :attr:`AttenuatorPVMapModel.ROT_MABS`."""    
        return self.pv_record_map.rot_mabs
    
    @rot_mabs.setter
    def rot_mabs(self, value):
        """Default Setter implementation for :attr:`AttenuatorPVMapModel.ROT_MABS`.""" 
        self.pv_record_map.rot_mabs = value
    
    
    @property
    def rot_rpos(self):
        """Default Getter implementation for :attr:`AttenuatorPVMapModel.ROT_RPOS`."""    
        return self.pv_record_map.rot_rpos
    
    

    


class AttenuatorPropertiesModel(Properties):
    """
    Class for defining attenuator-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    attenuator_set_max_wait_time: float
    
    
    
    subtype: str
    
    
    
    maximum: int
    
    
    
    minimum: int
    
    
    
    tolerance: float
    
    
    
    virtual_name: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            AttenuatorPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class AttenuatorModel(Hardware):
    """
    Middle layer class for interacting with a specific attenuator object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[AttenuatorControlsInformationModel]
    """Controls information pertaining to this attenuator
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[AttenuatorPropertiesModel]
    """Properties pertaining to this attenuator
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            AttenuatorModel,
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
    def validate_controls_information(cls, v: Any) -> AttenuatorControlsInformationModel:
        try:
            return AttenuatorControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> AttenuatorPropertiesModel:
        try:
            return AttenuatorPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def enable(self):
        """Default Getter implementation for :attr:`AttenuatorControlsInformationModel.ENABLE`."""
        return self.controls_information.enable
    
    @enable.setter
    def enable(self, value):
        """Default Setter implementation for :attr:`AttenuatorControlsInformationModel.ENABLE`."""
        self.controls_information.enable = value
    
    
    @property
    def rot_mabs(self):
        """Default Getter implementation for :attr:`AttenuatorControlsInformationModel.ROT_MABS`."""
        return self.controls_information.rot_mabs
    
    @rot_mabs.setter
    def rot_mabs(self, value):
        """Default Setter implementation for :attr:`AttenuatorControlsInformationModel.ROT_MABS`."""
        self.controls_information.rot_mabs = value
    
    
    @property
    def rot_rpos(self):
        """Default Getter implementation for :attr:`AttenuatorControlsInformationModel.ROT_RPOS`."""
        return self.controls_information.rot_rpos
    
    

class AttenuatorFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.attenuator.Attenuator` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(AttenuatorFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=AttenuatorModel,
            lattice_folder="Attenuator",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_attenuator(self, name: Union[str, List[str]] = None) -> AttenuatorModel:
        """
        Returns the attenuator object for the given name(s).

        :param name: Name(s) of the attenuator.
        :type name: str or list of str

        :return: Attenuator object(s).
        :rtype: :class:`attenuatorModel.Attenuator`
        or Dict[str: :class:`attenuator.Attenuator`]
        """
        return self.get_hardware(name)

    
    def enable(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`AttenuatorModel.ENABLE`.

        :param name: Name(s) of the attenuator.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`AttenuatorModel.ENABLE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda attenuator: attenuator.enable)
    
    def rot_mabs(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`AttenuatorModel.ROT_MABS`.

        :param name: Name(s) of the attenuator.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`AttenuatorModel.ROT_MABS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda attenuator: attenuator.rot_mabs)
    
    def rot_rpos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`AttenuatorModel.ROT_RPOS`.

        :param name: Name(s) of the attenuator.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`AttenuatorModel.ROT_RPOS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda attenuator: attenuator.rot_rpos)
    