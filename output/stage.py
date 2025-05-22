
from CATAP.common.machine.pv_utils import BinaryPV, ScalarPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class StagePVMap(PVMap):
    
    EX: BinaryPV
    
    EN: BinaryPV
    
    TGTPOS: ScalarPV
    
    MOVING: BinaryPV
    
    ACTPOS: ScalarPV
    
    READY: BinaryPV
    
    JOGINC: ScalarPV
    
    JOGUP: BinaryPV
    
    JOGDOWN: BinaryPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        StagePVMap.is_virtual = is_virtual
        StagePVMap.connect_on_creation = connect_on_creation
        super(
            StagePVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def ex(self):
        return self.EX.get()
    
    @ex.setter
    def ex(self, value):
        self.EX.put(value)
    
    
    @property
    def en(self):
        return self.EN.get()
    
    @en.setter
    def en(self, value):
        self.EN.put(value)
    
    
    @property
    def tgtpos(self):
        return self.TGTPOS.get()
    
    @tgtpos.setter
    def tgtpos(self, value):
        self.TGTPOS.put(value)
    
    
    @property
    def moving(self):
        return self.MOVING.get()
    
    
    @property
    def actpos(self):
        return self.ACTPOS.get()
    
    
    @property
    def ready(self):
        return self.READY.get()
    
    
    @property
    def joginc(self):
        return self.JOGINC.get()
    
    @joginc.setter
    def joginc(self, value):
        self.JOGINC.put(value)
    
    
    @property
    def jogup(self):
        return self.JOGUP.get()
    
    @jogup.setter
    def jogup(self, value):
        self.JOGUP.put(value)
    
    
    @property
    def jogdown(self):
        return self.JOGDOWN.get()
    
    @jogdown.setter
    def jogdown(self, value):
        self.JOGDOWN.put(value)
    
    



class StageControlsInformation(ControlsInformation):
    """
    Class for controlling a stage via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[StagePVMap]
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
        StageControlsInformation.is_virtual = is_virtual
        StageControlsInformation.connect_on_creation = connect_on_creation
        super(
            StageControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> StagePVMap:
        return StagePVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def ex(self):
        return self.pv_record_map.ex
    
    @ex.setter
    def ex(self, value):
        self.pv_record_map.ex = value
    
    
    @property
    def en(self):
        return self.pv_record_map.en
    
    @en.setter
    def en(self, value):
        self.pv_record_map.en = value
    
    
    @property
    def tgtpos(self):
        return self.pv_record_map.tgtpos
    
    @tgtpos.setter
    def tgtpos(self, value):
        self.pv_record_map.tgtpos = value
    
    
    @property
    def moving(self):
        return self.pv_record_map.moving
    
    
    @property
    def actpos(self):
        return self.pv_record_map.actpos
    
    
    @property
    def ready(self):
        return self.pv_record_map.ready
    
    
    @property
    def joginc(self):
        return self.pv_record_map.joginc
    
    @joginc.setter
    def joginc(self, value):
        self.pv_record_map.joginc = value
    
    
    @property
    def jogup(self):
        return self.pv_record_map.jogup
    
    @jogup.setter
    def jogup(self, value):
        self.pv_record_map.jogup = value
    
    
    @property
    def jogdown(self):
        return self.pv_record_map.jogdown
    
    @jogdown.setter
    def jogdown(self, value):
        self.pv_record_map.jogdown = value
    
    


class StageProperties(Properties):
    """
    Class for defining stage-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    camera_name: str
    """"""
    
    position: float
    """"""
    
    set_max_wait_time: float
    """"""
    
    max_pos: float
    """"""
    
    remove: float
    """"""
    
    tolerance: float
    """"""
    
    type: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            StageProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def camera_name(self):
        return self.camera_name
    
    @property
    def position(self):
        return self.position
    
    @property
    def set_max_wait_time(self):
        return self.set_max_wait_time
    
    @property
    def max_pos(self):
        return self.max_pos
    
    @property
    def remove(self):
        return self.remove
    
    @property
    def tolerance(self):
        return self.tolerance
    
    @property
    def type(self):
        return self.type
    

    
    @property
    def position(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.position

    @position.setter
    def position(self, value: float) -> None:
        self.position = value
    
    @property
    def max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.set_max_wait_time

    @max_wait_time.setter
    def max_wait_time(self, value: float) -> None:
        self.set_max_wait_time = value
    
    @property
    def max_pos(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.max_pos

    @max_pos.setter
    def max_pos(self, value: float) -> None:
        self.max_pos = value
    
    @property
    def remove(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.remove

    @remove.setter
    def remove(self, value: float) -> None:
        self.remove = value
    
    @property
    def tolerance(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.tolerance

    @tolerance.setter
    def tolerance(self, value: float) -> None:
        self.tolerance = value
    

class Stage(Hardware):
    """
    Middle layer class for interacting with a specific stage object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[StageControlsInformation]
    """Controls information pertaining to this stage
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[StageProperties]
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
            Stage,
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
    def validate_controls_information(cls, v: Any) -> StageControlsInformation:
        try:
            return StageControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> StageProperties:
        try:
            return StageProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def ex(self):
        return self.controls_information.ex
    
    @ex.setter
    def ex(self, value):
        self.controls_information.ex = value
    
    
    @property
    def en(self):
        return self.controls_information.en
    
    @en.setter
    def en(self, value):
        self.controls_information.en = value
    
    
    @property
    def tgtpos(self):
        return self.controls_information.tgtpos
    
    @tgtpos.setter
    def tgtpos(self, value):
        self.controls_information.tgtpos = value
    
    
    @property
    def moving(self):
        return self.controls_information.moving
    
    
    @property
    def actpos(self):
        return self.controls_information.actpos
    
    
    @property
    def ready(self):
        return self.controls_information.ready
    
    
    @property
    def joginc(self):
        return self.controls_information.joginc
    
    @joginc.setter
    def joginc(self, value):
        self.controls_information.joginc = value
    
    
    @property
    def jogup(self):
        return self.controls_information.jogup
    
    @jogup.setter
    def jogup(self, value):
        self.controls_information.jogup = value
    
    
    @property
    def jogdown(self):
        return self.controls_information.jogdown
    
    @jogdown.setter
    def jogdown(self, value):
        self.controls_information.jogdown = value
    
    

class StageFactory(Factory):
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
        super(StageFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Stage,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_stage(self, name: Union[str, List[str]] = None) -> Stage:
        """
        Returns the stage object for the given name(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str

        :return: Stage object(s).
        :rtype: :class:`~CATAP.laser.components.stage.Stage`
        or Dict[str: :class:`~CATAP.laser.components.stage.Stage`]
        """
        return self.get_hardware(name)

    
    def ex(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ex' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'EX' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.ex)
    
    def en(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'en' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'EN' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.en)
    
    def tgtpos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'tgtpos' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'TGTPOS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.tgtpos)
    
    def moving(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'moving' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'MOVING' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.moving)
    
    def actpos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'actpos' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'ACTPOS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.actpos)
    
    def ready(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ready' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'READY' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.ready)
    
    def joginc(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'joginc' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'JOGINC' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.joginc)
    
    def jogup(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'jogup' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'JOGUP' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.jogup)
    
    def jogdown(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'jogdown' property of the stage(s).

        :param name: Name(s) of the stage.
        :type name: str or list of str or None

        :return: Value(s) of the 'JOGDOWN' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda stage: stage.jogdown)
    