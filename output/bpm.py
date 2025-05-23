
from CATAP.common.machine.pv_utils import BinaryPV, ScalarPV, StatisticalPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class BPMPVMap(PVMap):
    
    AWAK: BinaryPV
    
    RA1: ScalarPV
    
    RA2: ScalarPV
    
    RD1: ScalarPV
    
    RD2: ScalarPV
    
    RDY: BinaryPV
    
    SA1: ScalarPV
    
    SA2: ScalarPV
    
    SD1: ScalarPV
    
    SD2: ScalarPV
    
    X: StatisticalPV
    
    Y: StatisticalPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        BPMPVMap.is_virtual = is_virtual
        BPMPVMap.connect_on_creation = connect_on_creation
        super(
            BPMPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def awak(self):
        return self.AWAK.get()
    
    
    @property
    def ra1(self):
        return self.RA1.get()
    
    
    @property
    def ra2(self):
        return self.RA2.get()
    
    
    @property
    def rd1(self):
        return self.RD1.get()
    
    
    @property
    def rd2(self):
        return self.RD2.get()
    
    
    @property
    def rdy(self):
        return self.RDY.get()
    
    
    @property
    def sa1(self):
        return self.SA1.get()
    
    
    @property
    def sa2(self):
        return self.SA2.get()
    
    
    @property
    def sd1(self):
        return self.SD1.get()
    
    
    @property
    def sd2(self):
        return self.SD2.get()
    
    
    @property
    def x(self):
        return self.X.get()
    
    
    @property
    def y(self):
        return self.Y.get()
    
    



class BPMControlsInformation(ControlsInformation):
    """
    Class for controlling a bpm via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[BPMPVMap]
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
        BPMControlsInformation.is_virtual = is_virtual
        BPMControlsInformation.connect_on_creation = connect_on_creation
        super(
            BPMControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> BPMPVMap:
        return BPMPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def awak(self):
        return self.pv_record_map.awak
    
    
    @property
    def ra1(self):
        return self.pv_record_map.ra1
    
    
    @property
    def ra2(self):
        return self.pv_record_map.ra2
    
    
    @property
    def rd1(self):
        return self.pv_record_map.rd1
    
    
    @property
    def rd2(self):
        return self.pv_record_map.rd2
    
    
    @property
    def rdy(self):
        return self.pv_record_map.rdy
    
    
    @property
    def sa1(self):
        return self.pv_record_map.sa1
    
    
    @property
    def sa2(self):
        return self.pv_record_map.sa2
    
    
    @property
    def sd1(self):
        return self.pv_record_map.sd1
    
    
    @property
    def sd2(self):
        return self.pv_record_map.sd2
    
    
    @property
    def x(self):
        return self.pv_record_map.x
    
    
    @property
    def y(self):
        return self.pv_record_map.y
    
    


class BPMProperties(Properties):
    """
    Class for defining bpm-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    position: float
    """"""
    
    bpm_type: Any
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            BPMProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def position(self):
        return self.position
    
    @property
    def bpm_type(self):
        return self.bpm_type
    

    
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
    

class BPM(Hardware):
    """
    Middle layer class for interacting with a specific bpm object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[BPMControlsInformation]
    """Controls information pertaining to this bpm
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[BPMProperties]
    """Properties pertaining to this bpm
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            BPM,
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
    def validate_controls_information(cls, v: Any) -> BPMControlsInformation:
        try:
            return BPMControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> BPMProperties:
        try:
            return BPMProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def awak(self):
        return self.controls_information.awak
    
    
    @property
    def ra1(self):
        return self.controls_information.ra1
    
    
    @property
    def ra2(self):
        return self.controls_information.ra2
    
    
    @property
    def rd1(self):
        return self.controls_information.rd1
    
    
    @property
    def rd2(self):
        return self.controls_information.rd2
    
    
    @property
    def rdy(self):
        return self.controls_information.rdy
    
    
    @property
    def sa1(self):
        return self.controls_information.sa1
    
    
    @property
    def sa2(self):
        return self.controls_information.sa2
    
    
    @property
    def sd1(self):
        return self.controls_information.sd1
    
    
    @property
    def sd2(self):
        return self.controls_information.sd2
    
    
    @property
    def x(self):
        return self.controls_information.x
    
    
    @property
    def y(self):
        return self.controls_information.y
    
    

class BPMFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.bpm.BPM` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(BPMFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=BPM,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_bpm(self, name: Union[str, List[str]] = None) -> BPM:
        """
        Returns the bpm object for the given name(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str

        :return: Bpm object(s).
        :rtype: :class:`~CATAP.laser.components.bpm.BPM`
        or Dict[str: :class:`~CATAP.laser.components.bpm.BPM`]
        """
        return self.get_hardware(name)

    
    def awak(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'awak' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'AWAK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.awak)
    
    def ra1(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ra1' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'RA1' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.ra1)
    
    def ra2(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ra2' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'RA2' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.ra2)
    
    def rd1(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rd1' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'RD1' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.rd1)
    
    def rd2(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rd2' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'RD2' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.rd2)
    
    def rdy(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'rdy' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'RDY' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.rdy)
    
    def sa1(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'sa1' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'SA1' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sa1)
    
    def sa2(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'sa2' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'SA2' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sa2)
    
    def sd1(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'sd1' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'SD1' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sd1)
    
    def sd2(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'sd2' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'SD2' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sd2)
    
    def x(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'x' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'X' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.x)
    
    def y(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'y' property of the bpm(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the 'Y' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.y)
    