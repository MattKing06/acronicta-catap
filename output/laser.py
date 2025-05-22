
from CATAP.common.machine.pv_utils import 
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class LaserPVMap(PVMap):
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        LaserPVMap.is_virtual = is_virtual
        LaserPVMap.connect_on_creation = connect_on_creation
        super(
            LaserPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    



class LaserControlsInformation(ControlsInformation):
    """
    Class for controlling a laser via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[LaserPVMap]
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
        LaserControlsInformation.is_virtual = is_virtual
        LaserControlsInformation.connect_on_creation = connect_on_creation
        super(
            LaserControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> LaserPVMap:
        return LaserPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    


class LaserProperties(Properties):
    """
    Class for defining laser-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    aliases: list
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            LaserProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def aliases(self):
        return self.aliases
    

    

class Laser(Hardware):
    """
    Middle layer class for interacting with a specific laser object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[LaserControlsInformation]
    """Controls information pertaining to this laser
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[LaserProperties]
    """Properties pertaining to this laser
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Laser,
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
    def validate_controls_information(cls, v: Any) -> LaserControlsInformation:
        try:
            return LaserControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> LaserProperties:
        try:
            return LaserProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    

class LaserFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.laser.Laser` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(LaserFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Laser,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_laser(self, name: Union[str, List[str]] = None) -> Laser:
        """
        Returns the laser object for the given name(s).

        :param name: Name(s) of the laser.
        :type name: str or list of str

        :return: Laser object(s).
        :rtype: :class:`~CATAP.laser.components.laser.Laser`
        or Dict[str: :class:`~CATAP.laser.components.laser.Laser`]
        """
        return self.get_hardware(name)

    