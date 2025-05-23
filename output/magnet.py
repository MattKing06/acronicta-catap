
from CATAP.common.machine.pv_utils import ScalarPV, StatePV, BinaryPV, StatisticalPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class MagnetPVMap(PVMap):
    
    GETSETI: ScalarPV
    
    SPOWER: StatePV
    
    RPOWER: StatePV
    
    ILK_RESET: BinaryPV
    
    RILK: BinaryPV
    
    ILK_ON: BinaryPV
    
    ILK_OFF: BinaryPV
    
    ILK_PSU_RESET: BinaryPV
    
    READI: StatisticalPV
    
    SETI: ScalarPV
    
    SETK: ScalarPV
    
    READK: StatisticalPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        MagnetPVMap.is_virtual = is_virtual
        MagnetPVMap.connect_on_creation = connect_on_creation
        super(
            MagnetPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def getseti(self):
        return self.GETSETI.get()
    
    
    @property
    def spower(self):
        return self.SPOWER.get()
    
    @spower.setter
    def spower(self, value):
        self.SPOWER.put(value)
    
    
    @property
    def rpower(self):
        return self.RPOWER.get()
    
    @rpower.setter
    def rpower(self, value):
        self.RPOWER.put(value)
    
    
    @property
    def ilk_reset(self):
        return self.ILK_RESET.get()
    
    @ilk_reset.setter
    def ilk_reset(self, value):
        self.ILK_RESET.put(value)
    
    
    @property
    def rilk(self):
        return self.RILK.get()
    
    
    @property
    def ilk_on(self):
        return self.ILK_ON.get()
    
    @ilk_on.setter
    def ilk_on(self, value):
        self.ILK_ON.put(value)
    
    
    @property
    def ilk_off(self):
        return self.ILK_OFF.get()
    
    @ilk_off.setter
    def ilk_off(self, value):
        self.ILK_OFF.put(value)
    
    
    @property
    def ilk_psu_reset(self):
        return self.ILK_PSU_RESET.get()
    
    @ilk_psu_reset.setter
    def ilk_psu_reset(self, value):
        self.ILK_PSU_RESET.put(value)
    
    
    @property
    def readi(self):
        return self.READI.get()
    
    
    @property
    def seti(self):
        return self.SETI.get()
    
    
    @property
    def setk(self):
        return self.SETK.get()
    
    
    @property
    def readk(self):
        return self.READK.get()
    
    



class MagnetControlsInformation(ControlsInformation):
    """
    Class for controlling a magnet via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[MagnetPVMap]
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
        MagnetControlsInformation.is_virtual = is_virtual
        MagnetControlsInformation.connect_on_creation = connect_on_creation
        super(
            MagnetControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> MagnetPVMap:
        return MagnetPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def getseti(self):
        return self.pv_record_map.getseti
    
    
    @property
    def spower(self):
        return self.pv_record_map.spower
    
    @spower.setter
    def spower(self, value):
        self.pv_record_map.spower = value
    
    
    @property
    def rpower(self):
        return self.pv_record_map.rpower
    
    @rpower.setter
    def rpower(self, value):
        self.pv_record_map.rpower = value
    
    
    @property
    def ilk_reset(self):
        return self.pv_record_map.ilk_reset
    
    @ilk_reset.setter
    def ilk_reset(self, value):
        self.pv_record_map.ilk_reset = value
    
    
    @property
    def rilk(self):
        return self.pv_record_map.rilk
    
    
    @property
    def ilk_on(self):
        return self.pv_record_map.ilk_on
    
    @ilk_on.setter
    def ilk_on(self, value):
        self.pv_record_map.ilk_on = value
    
    
    @property
    def ilk_off(self):
        return self.pv_record_map.ilk_off
    
    @ilk_off.setter
    def ilk_off(self, value):
        self.pv_record_map.ilk_off = value
    
    
    @property
    def ilk_psu_reset(self):
        return self.pv_record_map.ilk_psu_reset
    
    @ilk_psu_reset.setter
    def ilk_psu_reset(self, value):
        self.pv_record_map.ilk_psu_reset = value
    
    
    @property
    def readi(self):
        return self.pv_record_map.readi
    
    
    @property
    def seti(self):
        return self.pv_record_map.seti
    
    
    @property
    def setk(self):
        return self.pv_record_map.setk
    
    
    @property
    def readk(self):
        return self.pv_record_map.readk
    
    


class MagnetProperties(Properties):
    """
    Class for defining magnet-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    type: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            MagnetProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def type(self):
        return self.type
    

    

class Magnet(Hardware):
    """
    Middle layer class for interacting with a specific magnet object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[MagnetControlsInformation]
    """Controls information pertaining to this magnet
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[MagnetProperties]
    """Properties pertaining to this magnet
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Magnet,
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
    def validate_controls_information(cls, v: Any) -> MagnetControlsInformation:
        try:
            return MagnetControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> MagnetProperties:
        try:
            return MagnetProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def getseti(self):
        return self.controls_information.getseti
    
    
    @property
    def spower(self):
        return self.controls_information.spower
    
    @spower.setter
    def spower(self, value):
        self.controls_information.spower = value
    
    
    @property
    def rpower(self):
        return self.controls_information.rpower
    
    @rpower.setter
    def rpower(self, value):
        self.controls_information.rpower = value
    
    
    @property
    def ilk_reset(self):
        return self.controls_information.ilk_reset
    
    @ilk_reset.setter
    def ilk_reset(self, value):
        self.controls_information.ilk_reset = value
    
    
    @property
    def rilk(self):
        return self.controls_information.rilk
    
    
    @property
    def ilk_on(self):
        return self.controls_information.ilk_on
    
    @ilk_on.setter
    def ilk_on(self, value):
        self.controls_information.ilk_on = value
    
    
    @property
    def ilk_off(self):
        return self.controls_information.ilk_off
    
    @ilk_off.setter
    def ilk_off(self, value):
        self.controls_information.ilk_off = value
    
    
    @property
    def ilk_psu_reset(self):
        return self.controls_information.ilk_psu_reset
    
    @ilk_psu_reset.setter
    def ilk_psu_reset(self, value):
        self.controls_information.ilk_psu_reset = value
    
    
    @property
    def readi(self):
        return self.controls_information.readi
    
    
    @property
    def seti(self):
        return self.controls_information.seti
    
    
    @property
    def setk(self):
        return self.controls_information.setk
    
    
    @property
    def readk(self):
        return self.controls_information.readk
    
    

class MagnetFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.magnet.Magnet` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(MagnetFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Magnet,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_magnet(self, name: Union[str, List[str]] = None) -> Magnet:
        """
        Returns the magnet object for the given name(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str

        :return: Magnet object(s).
        :rtype: :class:`~CATAP.laser.components.magnet.Magnet`
        or Dict[str: :class:`~CATAP.laser.components.magnet.Magnet`]
        """
        return self.get_hardware(name)

    
    def getseti(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'getseti' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'GETSETI' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.getseti)
    
    def spower(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'spower' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'SPOWER' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.spower)
    
    def rpower(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rpower' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'RPOWER' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.rpower)
    
    def ilk_reset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ilk_reset' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'ILK_RESET' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_reset)
    
    def rilk(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rilk' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'RILK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.rilk)
    
    def ilk_on(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ilk_on' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'ILK_ON' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_on)
    
    def ilk_off(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ilk_off' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'ILK_OFF' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_off)
    
    def ilk_psu_reset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ilk_psu_reset' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'ILK_PSU_RESET' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_psu_reset)
    
    def readi(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'readi' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'READI' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readi)
    
    def seti(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'seti' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'SETI' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.seti)
    
    def setk(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'setk' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'SETK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.setk)
    
    def readk(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'readk' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'READK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readk)
    