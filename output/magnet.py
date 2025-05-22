
from CATAP.common.machine.pv_utils import ScalarPV, BinaryPV, StatisticalPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class MagnetPVMap(PVMap):
    
    GETSETI: ScalarPV
    
    ILK_RESET: BinaryPV
    
    READI: StatisticalPV
    
    RILK: StatePV
    
    RPOWER: StatePV
    
    SETI: ScalarPV
    
    SETK: ScalarPV
    
    SPOWER: StatePV
    
    ILK_ON: BinaryPV
    
    ILK_OFF: BinaryPV
    
    ILK_PSU_RESET: BinaryPV = None
    
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
    def ilk_reset(self):
        return self.ILK_RESET.get()
    
    @ilk_reset.setter
    def ilk_reset(self, value):
        self.ILK_RESET.put(value)
    
    
    @property
    def readi(self):
        return self.READI.get()
    
    
    @property
    def rilk(self):
        return self.RILK.get()
    
    
    @property
    def rpower(self):
        return self.RPOWER.get()
    
    
    @property
    def seti(self):
        return self.SETI.get()
    
    @seti.setter
    def seti(self, value):
        self.SETI.put(value)
    
    
    @property
    def setk(self):
        return self.SETK.get()
    
    @setk.setter
    def setk(self, value):
        self.SETK.put(value)
    
    
    @property
    def spower(self):
        return self.SPOWER.get()
    
    @spower.setter
    def spower(self, value):
        self.SPOWER.put(value)
    
    
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
    def ilk_reset(self):
        return self.pv_record_map.ilk_reset
    
    @ilk_reset.setter
    def ilk_reset(self, value):
        self.pv_record_map.ilk_reset = value
    
    
    @property
    def readi(self):
        return self.pv_record_map.readi
    
    
    @property
    def rilk(self):
        return self.pv_record_map.rilk
    
    
    @property
    def rpower(self):
        return self.pv_record_map.rpower
    
    
    @property
    def seti(self):
        return self.pv_record_map.seti
    
    @seti.setter
    def seti(self, value):
        self.pv_record_map.seti = value
    
    
    @property
    def setk(self):
        return self.pv_record_map.setk
    
    @setk.setter
    def setk(self, value):
        self.pv_record_map.setk = value
    
    
    @property
    def spower(self):
        return self.pv_record_map.spower
    
    @spower.setter
    def spower(self, value):
        self.pv_record_map.spower = value
    
    
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
    def readk(self):
        return self.pv_record_map.readk
    
    


class MagnetProperties(Properties):
    """
    Class for defining magnet-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    degauss_tolerance: float
    """"""
    
    degauss_values: str
    """"""
    
    field_integral_coefficients: str
    """"""
    
    mag_set_max_wait_time: float
    """"""
    
    magnet_type: str
    """"""
    
    magnetic_length: float
    """"""
    
    manufacturer: str
    """"""
    
    max_i: float
    """"""
    
    min_i: float
    """"""
    
    num_degauss_steps: int
    """"""
    
    position: float
    """"""
    
    ri_tolerance: float
    """"""
    
    serial_number: str | int
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
    def degauss_tolerance(self):
        return self.degauss_tolerance
    
    @property
    def degauss_values(self):
        return self.degauss_values
    
    @property
    def field_integral_coefficients(self):
        return self.field_integral_coefficients
    
    @property
    def mag_set_max_wait_time(self):
        return self.mag_set_max_wait_time
    
    @property
    def magnet_type(self):
        return self.magnet_type
    
    @property
    def magnetic_length(self):
        return self.magnetic_length
    
    @property
    def manufacturer(self):
        return self.manufacturer
    
    @property
    def max_i(self):
        return self.max_i
    
    @property
    def min_i(self):
        return self.min_i
    
    @property
    def num_degauss_steps(self):
        return self.num_degauss_steps
    
    @property
    def position(self):
        return self.position
    
    @property
    def ri_tolerance(self):
        return self.ri_tolerance
    
    @property
    def serial_number(self):
        return self.serial_number
    

    
    @property
    def degauss_tolerance(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.degauss_tolerance

    @degauss_tolerance.setter
    def degauss_tolerance(self, value: float) -> None:
        self.degauss_tolerance = value
    
    @property
    def mag_max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.mag_set_max_wait_time

    @mag_max_wait_time.setter
    def mag_max_wait_time(self, value: float) -> None:
        self.mag_set_max_wait_time = value
    
    @property
    def magnetic_length(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.magnetic_length

    @magnetic_length.setter
    def magnetic_length(self, value: float) -> None:
        self.magnetic_length = value
    
    @property
    def max_i(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.max_i

    @max_i.setter
    def max_i(self, value: float) -> None:
        self.max_i = value
    
    @property
    def min_i(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.min_i

    @min_i.setter
    def min_i(self, value: float) -> None:
        self.min_i = value
    
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
    def ri_tolerance(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.ri_tolerance

    @ri_tolerance.setter
    def ri_tolerance(self, value: float) -> None:
        self.ri_tolerance = value
    

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
    def ilk_reset(self):
        return self.controls_information.ilk_reset
    
    @ilk_reset.setter
    def ilk_reset(self, value):
        self.controls_information.ilk_reset = value
    
    
    @property
    def readi(self):
        return self.controls_information.readi
    
    
    @property
    def rilk(self):
        return self.controls_information.rilk
    
    
    @property
    def rpower(self):
        return self.controls_information.rpower
    
    
    @property
    def seti(self):
        return self.controls_information.seti
    
    @seti.setter
    def seti(self, value):
        self.controls_information.seti = value
    
    
    @property
    def setk(self):
        return self.controls_information.setk
    
    @setk.setter
    def setk(self, value):
        self.controls_information.setk = value
    
    
    @property
    def spower(self):
        return self.controls_information.spower
    
    @spower.setter
    def spower(self, value):
        self.controls_information.spower = value
    
    
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
    
    def ilk_reset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ilk_reset' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'ILK_RESET' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.ilk_reset)
    
    def readi(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'readi' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'READI' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readi)
    
    def rilk(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rilk' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'RILK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.rilk)
    
    def rpower(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rpower' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'RPOWER' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.rpower)
    
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
    
    def spower(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'spower' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'SPOWER' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.spower)
    
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
    
    def readk(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'readk' property of the magnet(s).

        :param name: Name(s) of the magnet.
        :type name: str or list of str or None

        :return: Value(s) of the 'READK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda magnet: magnet.readk)
    