
from CATAP.common.machine.pv_utils import BinaryPV, ScalarPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class StagePVMapModel(PVMap):
    
    
    EX: BinaryPV
    
    """Execute move"""
    
    
    EN: BinaryPV
    
    """Enable movement"""
    
    
    TGTPOS: ScalarPV
    
    """Absolute target position"""
    
    
    MOVING: BinaryPV
    
    """Moving state"""
    
    
    ACTPOS: ScalarPV
    
    """Absolute actuator position"""
    
    
    READY: BinaryPV
    
    """Ready to move"""
    
    
    JOGINC: ScalarPV
    
    """Jog increment"""
    
    
    JOGUP: BinaryPV
    
    """Execute job upwards (away from straight-on)"""
    
    
    JOGDOWN: BinaryPV
    
    """Execute job upwards (towards straight-on)"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        StagePVMapModel.is_virtual = is_virtual
        StagePVMapModel.connect_on_creation = connect_on_creation
        super(
            StagePVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def ex(self):
        """Default Getter implementation for EX"""
        
        return self.EX.get()
        

    
    @ex.setter
    def ex(self, value):
        """Default Setter implementation for EX"""
        
        return self.EX.put(value)
        
    
    
    @property
    def en(self):
        """Default Getter implementation for EN"""
        
        return self.EN.get()
        

    
    @en.setter
    def en(self, value):
        """Default Setter implementation for EN"""
        
        return self.EN.put(value)
        
    
    
    @property
    def tgtpos(self):
        """Default Getter implementation for TGTPOS"""
        
        return self.TGTPOS.get()
        

    
    @tgtpos.setter
    def tgtpos(self, value):
        """Default Setter implementation for TGTPOS"""
        
        return self.TGTPOS.put(value)
        
    
    
    @property
    def moving(self):
        """Default Getter implementation for MOVING"""
        
        return self.MOVING.get()
        

    
    
    @property
    def actpos(self):
        """Default Getter implementation for ACTPOS"""
        
        return self.ACTPOS.get()
        

    
    
    @property
    def ready(self):
        """Default Getter implementation for READY"""
        
        return self.READY.get()
        

    
    
    @property
    def joginc(self):
        """Default Getter implementation for JOGINC"""
        
        return self.JOGINC.get()
        

    
    @joginc.setter
    def joginc(self, value):
        """Default Setter implementation for JOGINC"""
        
        return self.JOGINC.put(value)
        
    
    
    @property
    def jogup(self):
        """Default Getter implementation for JOGUP"""
        
        return self.JOGUP.get()
        

    
    @jogup.setter
    def jogup(self, value):
        """Default Setter implementation for JOGUP"""
        
        return self.JOGUP.put(value)
        
    
    
    @property
    def jogdown(self):
        """Default Getter implementation for JOGDOWN"""
        
        return self.JOGDOWN.get()
        

    
    @jogdown.setter
    def jogdown(self, value):
        """Default Setter implementation for JOGDOWN"""
        
        return self.JOGDOWN.put(value)
        
    
    



class StageControlsInformationModel(ControlsInformation):
    """
    Class for controlling a stage via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[StagePVMapModel]

    

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
        StageControlsInformationModel.is_virtual = is_virtual
        StageControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            StageControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> StagePVMapModel:
        return StagePVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def ex(self):
        """Default Getter implementation for :attr:`StagePVMapModel.EX`."""    
        return self.pv_record_map.ex
    
    @ex.setter
    def ex(self, value):
        """Default Setter implementation for :attr:`StagePVMapModel.EX`.""" 
        self.pv_record_map.ex = value
    
    
    @property
    def en(self):
        """Default Getter implementation for :attr:`StagePVMapModel.EN`."""    
        return self.pv_record_map.en
    
    @en.setter
    def en(self, value):
        """Default Setter implementation for :attr:`StagePVMapModel.EN`.""" 
        self.pv_record_map.en = value
    
    
    @property
    def tgtpos(self):
        """Default Getter implementation for :attr:`StagePVMapModel.TGTPOS`."""    
        return self.pv_record_map.tgtpos
    
    @tgtpos.setter
    def tgtpos(self, value):
        """Default Setter implementation for :attr:`StagePVMapModel.TGTPOS`.""" 
        self.pv_record_map.tgtpos = value
    
    
    @property
    def moving(self):
        """Default Getter implementation for :attr:`StagePVMapModel.MOVING`."""    
        return self.pv_record_map.moving
    
    
    @property
    def actpos(self):
        """Default Getter implementation for :attr:`StagePVMapModel.ACTPOS`."""    
        return self.pv_record_map.actpos
    
    
    @property
    def ready(self):
        """Default Getter implementation for :attr:`StagePVMapModel.READY`."""    
        return self.pv_record_map.ready
    
    
    @property
    def joginc(self):
        """Default Getter implementation for :attr:`StagePVMapModel.JOGINC`."""    
        return self.pv_record_map.joginc
    
    @joginc.setter
    def joginc(self, value):
        """Default Setter implementation for :attr:`StagePVMapModel.JOGINC`.""" 
        self.pv_record_map.joginc = value
    
    
    @property
    def jogup(self):
        """Default Getter implementation for :attr:`StagePVMapModel.JOGUP`."""    
        return self.pv_record_map.jogup
    
    @jogup.setter
    def jogup(self, value):
        """Default Setter implementation for :attr:`StagePVMapModel.JOGUP`.""" 
        self.pv_record_map.jogup = value
    
    
    @property
    def jogdown(self):
        """Default Getter implementation for :attr:`StagePVMapModel.JOGDOWN`."""    
        return self.pv_record_map.jogdown
    
    @jogdown.setter
    def jogdown(self, value):
        """Default Setter implementation for :attr:`StagePVMapModel.JOGDOWN`.""" 
        self.pv_record_map.jogdown = value
    
    

    


class StagePropertiesModel(Properties):
    """
    Class for defining stage-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    camera_name: str
    
    
    
    set_max_wait_time: float
    
    
    
    max_pos: float
    
    
    
    remove: float
    
    
    
    tolerance: float
    
    
    
    subtype: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            StagePropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class StageModel(Hardware):
    """
    Middle layer class for interacting with a specific stage object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[StageControlsInformationModel]
    """Controls information pertaining to this stage
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[StagePropertiesModel]
    """Properties pertaining to this stage
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            StageModel,
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
    def validate_controls_information(cls, v: Any) -> StageControlsInformationModel:
        try:
            return StageControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> StagePropertiesModel:
        try:
            return StagePropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def ex(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.EX`."""
        return self.controls_information.ex
    
    @ex.setter
    def ex(self, value):
        """Default Setter implementation for :attr:`StageControlsInformationModel.EX`."""
        self.controls_information.ex = value
    
    
    @property
    def en(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.EN`."""
        return self.controls_information.en
    
    @en.setter
    def en(self, value):
        """Default Setter implementation for :attr:`StageControlsInformationModel.EN`."""
        self.controls_information.en = value
    
    
    @property
    def tgtpos(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.TGTPOS`."""
        return self.controls_information.tgtpos
    
    @tgtpos.setter
    def tgtpos(self, value):
        """Default Setter implementation for :attr:`StageControlsInformationModel.TGTPOS`."""
        self.controls_information.tgtpos = value
    
    
    @property
    def moving(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.MOVING`."""
        return self.controls_information.moving
    
    
    @property
    def actpos(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.ACTPOS`."""
        return self.controls_information.actpos
    
    
    @property
    def ready(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.READY`."""
        return self.controls_information.ready
    
    
    @property
    def joginc(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.JOGINC`."""
        return self.controls_information.joginc
    
    @joginc.setter
    def joginc(self, value):
        """Default Setter implementation for :attr:`StageControlsInformationModel.JOGINC`."""
        self.controls_information.joginc = value
    
    
    @property
    def jogup(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.JOGUP`."""
        return self.controls_information.jogup
    
    @jogup.setter
    def jogup(self, value):
        """Default Setter implementation for :attr:`StageControlsInformationModel.JOGUP`."""
        self.controls_information.jogup = value
    
    
    @property
    def jogdown(self):
        """Default Getter implementation for :attr:`StageControlsInformationModel.JOGDOWN`."""
        return self.controls_information.jogdown
    
    @jogdown.setter
    def jogdown(self, value):
        """Default Setter implementation for :attr:`StageControlsInformationModel.JOGDOWN`."""
        self.controls_information.jogdown = value
    
    

class StageFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.stage.Stage` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(StageFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=StageModel,
            lattice_folder="Stage",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_stage(self, name: Union[str, List[str]] = None) -> StageModel:
        """
        Returns the stage object for the given name(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str

        :return: Stage object(s).
        :rtype: :class:`stageModel.Stage`
        or Dict[str: :class:`stage.Stage`]
        """
        return self.get_hardware(name)

    
    def ex(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.EX`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.EX` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.ex)
    
    def en(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.EN`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.EN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.en)
    
    def tgtpos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.TGTPOS`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.TGTPOS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.tgtpos)
    
    def moving(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.MOVING`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.MOVING` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.moving)
    
    def actpos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.ACTPOS`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.ACTPOS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.actpos)
    
    def ready(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.READY`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.READY` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.ready)
    
    def joginc(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.JOGINC`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.JOGINC` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.joginc)
    
    def jogup(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.JOGUP`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.JOGUP` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.jogup)
    
    def jogdown(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`StageModel.JOGDOWN`.

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`StageModel.JOGDOWN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.jogdown)
    