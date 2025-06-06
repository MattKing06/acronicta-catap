
from CATAP.common.machine.pv_utils import PV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class RFHeartbeatPVMapModel(PVMap):
    
    
    KEEP_ALIVE: PV
    
    """"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        RFHeartbeatPVMapModel.is_virtual = is_virtual
        RFHeartbeatPVMapModel.connect_on_creation = connect_on_creation
        super(
            RFHeartbeatPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def keep_alive(self):
        """Default Getter implementation for KEEP_ALIVE"""
        
        return self.KEEP_ALIVE.get()
        

    
    



class RFHeartbeatControlsInformationModel(ControlsInformation):
    """
    Class for controlling a rfheartbeat via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[RFHeartbeatPVMapModel]

    
    
    PV: bool
    
    

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
        RFHeartbeatControlsInformationModel.is_virtual = is_virtual
        RFHeartbeatControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            RFHeartbeatControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> RFHeartbeatPVMapModel:
        return RFHeartbeatPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def keep_alive(self):
        """Default Getter implementation for :attr:`RFHeartbeatPVMapModel.KEEP_ALIVE`."""    
        return self.pv_record_map.keep_alive
    
    

    
    @property
    def pv(self) -> bool:
        """Default Getter implementation for PV."""
        
        return self.PV
        
    


class RFHeartbeatPropertiesModel(Properties):
    """
    Class for defining rfheartbeat-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    

    def __init__(self, *args, **kwargs):
        super(
            RFHeartbeatPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class RFHeartbeatModel(Hardware):
    """
    Middle layer class for interacting with a specific rfheartbeat object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[RFHeartbeatControlsInformationModel]
    """Controls information pertaining to this rfheartbeat
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[RFHeartbeatPropertiesModel]
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
            RFHeartbeatModel,
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
    def validate_controls_information(cls, v: Any) -> RFHeartbeatControlsInformationModel:
        try:
            return RFHeartbeatControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> RFHeartbeatPropertiesModel:
        try:
            return RFHeartbeatPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def keep_alive(self):
        """Default Getter implementation for :attr:`RFHeartbeatControlsInformationModel.KEEP_ALIVE`."""
        return self.controls_information.keep_alive
    
    

class RFHeartbeatFactoryModel(Factory):
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
        super(RFHeartbeatFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=RFHeartbeatModel,
            lattice_folder="RFHeartbeat",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_rfheartbeat(self, name: Union[str, List[str]] = None) -> RFHeartbeatModel:
        """
        Returns the rfheartbeat object for the given name(s).

        :param name: Name(s) of the rfheartbeat.
        :type name: str or list of str

        :return: Rfheartbeat object(s).
        :rtype: :class:`rfheartbeatModel.RFHeartbeat`
        or Dict[str: :class:`rfheartbeat.RFHeartbeat`]
        """
        return self.get_hardware(name)

    
    def keep_alive(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`RFHeartbeatModel.KEEP_ALIVE`.

        :param name: Name(s) of the rfheartbeat.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`RFHeartbeatModel.KEEP_ALIVE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda rfheartbeat: rfheartbeat.keep_alive)
    