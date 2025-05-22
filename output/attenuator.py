
from CATAP.common.machine.pv_utils import BinaryPV, ScalarPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class AttenuatorPVMap(PVMap):
    
    ENABLE: BinaryPV
    
    ROT_MABS: ScalarPV
    
    ROT_RPOS: ScalarPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        AttenuatorPVMap.is_virtual = is_virtual
        AttenuatorPVMap.connect_on_creation = connect_on_creation
        super(
            AttenuatorPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def enable(self):
        return self.ENABLE.get()
    
    @enable.setter
    def enable(self, value):
        self.ENABLE.put(value)
    
    
    @property
    def rot_mabs(self):
        return self.ROT_MABS.get()
    
    @rot_mabs.setter
    def rot_mabs(self, value):
        self.ROT_MABS.put(value)
    
    
    @property
    def rot_rpos(self):
        return self.ROT_RPOS.get()
    
    



class AttenuatorControlsInformation(ControlsInformation):
    """
    Class for controlling a attenuator via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[AttenuatorPVMap]
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
        AttenuatorControlsInformation.is_virtual = is_virtual
        AttenuatorControlsInformation.connect_on_creation = connect_on_creation
        super(
            AttenuatorControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> AttenuatorPVMap:
        return AttenuatorPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def enable(self):
        return self.pv_record_map.enable
    
    @enable.setter
    def enable(self, value):
        self.pv_record_map.enable = value
    
    
    @property
    def rot_mabs(self):
        return self.pv_record_map.rot_mabs
    
    @rot_mabs.setter
    def rot_mabs(self, value):
        self.pv_record_map.rot_mabs = value
    
    
    @property
    def rot_rpos(self):
        return self.pv_record_map.rot_rpos
    
    


class AttenuatorProperties(Properties):
    """
    Class for defining attenuator-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    attenuator_set_max_wait_time: float
    """"""
    
    attenuator_type: str
    """"""
    
    maximum: int
    """"""
    
    minimum: int
    """"""
    
    position: float
    """"""
    
    tolerance: float
    """"""
    
    virtual_name: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            AttenuatorProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def attenuator_set_max_wait_time(self):
        return self.attenuator_set_max_wait_time
    
    @property
    def attenuator_type(self):
        return self.attenuator_type
    
    @property
    def maximum(self):
        return self.maximum
    
    @property
    def minimum(self):
        return self.minimum
    
    @property
    def position(self):
        return self.position
    
    @property
    def tolerance(self):
        return self.tolerance
    
    @property
    def virtual_name(self):
        return self.virtual_name
    

    
    @property
    def attenuator_max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.attenuator_set_max_wait_time

    @attenuator_max_wait_time.setter
    def attenuator_max_wait_time(self, value: float) -> None:
        self.attenuator_set_max_wait_time = value
    
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
    

class Attenuator(Hardware):
    """
    Middle layer class for interacting with a specific attenuator object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[AttenuatorControlsInformation]
    """Controls information pertaining to this attenuator
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[AttenuatorProperties]
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
            Attenuator,
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
    def validate_controls_information(cls, v: Any) -> AttenuatorControlsInformation:
        try:
            return AttenuatorControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> AttenuatorProperties:
        try:
            return AttenuatorProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def enable(self):
        return self.controls_information.enable
    
    @enable.setter
    def enable(self, value):
        self.controls_information.enable = value
    
    
    @property
    def rot_mabs(self):
        return self.controls_information.rot_mabs
    
    @rot_mabs.setter
    def rot_mabs(self, value):
        self.controls_information.rot_mabs = value
    
    
    @property
    def rot_rpos(self):
        return self.controls_information.rot_rpos
    
    

class AttenuatorFactory(Factory):
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
        super(AttenuatorFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Attenuator,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_attenuator(self, name: Union[str, List[str]] = None) -> Attenuator:
        """
        Returns the attenuator object for the given name(s).

        :param name: Name(s) of the attenuator.
        :type name: str or list of str

        :return: Attenuator object(s).
        :rtype: :class:`~CATAP.laser.components.attenuator.Attenuator`
        or Dict[str: :class:`~CATAP.laser.components.attenuator.Attenuator`]
        """
        return self.get_hardware(name)

    
    def enable(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'enable' property of the attenuator(s).

        :param name: Name(s) of the attenuator.
        :type name: str or list of str or None

        :return: Value(s) of the 'ENABLE' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda attenuator: attenuator.enable)
    
    def rot_mabs(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rot_mabs' property of the attenuator(s).

        :param name: Name(s) of the attenuator.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROT_MABS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda attenuator: attenuator.rot_mabs)
    
    def rot_rpos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rot_rpos' property of the attenuator(s).

        :param name: Name(s) of the attenuator.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROT_RPOS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda attenuator: attenuator.rot_rpos)
    