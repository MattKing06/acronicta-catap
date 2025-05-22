
from CATAP.common.machine.pv_utils import PV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class RFHeartbeatPVMap(PVMap):
    
    KEEP_ALIVE: PV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        RFHeartbeatPVMap.is_virtual = is_virtual
        RFHeartbeatPVMap.connect_on_creation = connect_on_creation
        super(
            RFHeartbeatPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def keep_alive(self):
        return self.KEEP_ALIVE.get()
    
    



class RFHeartbeatControlsInformation(ControlsInformation):
    """
    Class for controlling a rfheartbeat via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[RFHeartbeatPVMap]
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
        RFHeartbeatControlsInformation.is_virtual = is_virtual
        RFHeartbeatControlsInformation.connect_on_creation = connect_on_creation
        super(
            RFHeartbeatControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> RFHeartbeatPVMap:
        return RFHeartbeatPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def keep_alive(self):
        return self.pv_record_map.keep_alive
    
    


class RFHeartbeatProperties(Properties):
    """
    Class for defining rfheartbeat-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    

    def __init__(self, *args, **kwargs):
        super(
            RFHeartbeatProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    

    

class RFHeartbeat(Hardware):
    """
    Middle layer class for interacting with a specific rfheartbeat object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[RFHeartbeatControlsInformation]
    """Controls information pertaining to this rfheartbeat
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[RFHeartbeatProperties]
    """Properties pertaining to this rfheartbeat
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            RFHeartbeat,
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
    def validate_controls_information(cls, v: Any) -> RFHeartbeatControlsInformation:
        try:
            return RFHeartbeatControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> RFHeartbeatProperties:
        try:
            return RFHeartbeatProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def keep_alive(self):
        return self.controls_information.keep_alive
    
    

class RFHeartbeatFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.rfheartbeat.RFHeartbeat` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(RFHeartbeatFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=RFHeartbeat,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_rfheartbeat(self, name: Union[str, List[str]] = None) -> RFHeartbeat:
        """
        Returns the rfheartbeat object for the given name(s).

        :param name: Name(s) of the rfheartbeat.
        :type name: str or list of str

        :return: Rfheartbeat object(s).
        :rtype: :class:`~CATAP.laser.components.rfheartbeat.RFHeartbeat`
        or Dict[str: :class:`~CATAP.laser.components.rfheartbeat.RFHeartbeat`]
        """
        return self.get_hardware(name)

    
    def keep_alive(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'keep_alive' property of the rfheartbeat(s).

        :param name: Name(s) of the rfheartbeat.
        :type name: str or list of str or None

        :return: Value(s) of the 'KEEP_ALIVE' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda rfheartbeat: rfheartbeat.keep_alive)
    