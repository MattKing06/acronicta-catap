
from catapcore.common.machine.pv_utils import BinaryPV, ScalarPV, StatisticalPV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class BPMPVMapModel(PVMap):
    
    
    AWAK: BinaryPV
    
    """Status of triggering on the BPM"""
    
    
    RA1: ScalarPV
    
    """The readback for the attenuator 1 setting"""
    
    
    RA2: ScalarPV
    
    """The readback for the attenuator 2 setting"""
    
    
    RD1: ScalarPV
    
    """The readback for the delay 1 setting"""
    
    
    RD2: ScalarPV
    
    """The readback for the delay 2 setting"""
    
    
    RDY: BinaryPV
    
    """Describes whether there is beam or not for the BPM"""
    
    
    SA1: ScalarPV
    
    """The setter for attenuator 1"""
    
    
    SA2: ScalarPV
    
    """The setter for attenuator 2"""
    
    
    SD1: ScalarPV
    
    """The setter for delay 1"""
    
    
    SD2: ScalarPV
    
    """The setter for delay 2"""
    
    
    X: StatisticalPV
    
    """readback for the beam x-position"""
    
    
    Y: StatisticalPV
    
    """readback for the beam y-position"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        BPMPVMapModel.is_virtual = is_virtual
        BPMPVMapModel.connect_on_creation = connect_on_creation
        super(
            BPMPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def awak(self):
        """Default Getter implementation for AWAK"""
        
        return self.AWAK.get()
        

    
    
    @property
    def ra1(self):
        """Default Getter implementation for RA1"""
        
        return self.RA1.get()
        

    
    
    @property
    def ra2(self):
        """Default Getter implementation for RA2"""
        
        return self.RA2.get()
        

    
    
    @property
    def rd1(self):
        """Default Getter implementation for RD1"""
        
        return self.RD1.get()
        

    
    
    @property
    def rd2(self):
        """Default Getter implementation for RD2"""
        
        return self.RD2.get()
        

    
    
    @property
    def rdy(self):
        """Default Getter implementation for RDY"""
        
        return self.RDY.get()
        

    
    
    @property
    def sa1(self):
        """Default Getter implementation for SA1"""
        
        return self.SA1.get()
        

    
    
    @property
    def sa2(self):
        """Default Getter implementation for SA2"""
        
        return self.SA2.get()
        

    
    
    @property
    def sd1(self):
        """Default Getter implementation for SD1"""
        
        return self.SD1.get()
        

    
    
    @property
    def sd2(self):
        """Default Getter implementation for SD2"""
        
        return self.SD2.get()
        

    
    
    @property
    def x(self):
        """Default Getter implementation for X"""
        
        return self.X.get()
        

    
    
    @property
    def y(self):
        """Default Getter implementation for Y"""
        
        return self.Y.get()
        

    
    



class BPMControlsInformationModel(ControlsInformation):
    """
    Class for controlling a bpm via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[BPMPVMapModel]

    

    """Dictionary of PVs read in from a config file (see :class:`~catapcore.common.machine.hardware.PVMap`)"""
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
        BPMControlsInformationModel.is_virtual = is_virtual
        BPMControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            BPMControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> BPMPVMapModel:
        return BPMPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def awak(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.AWAK`."""    
        return self.pv_record_map.awak
    
    
    @property
    def ra1(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.RA1`."""    
        return self.pv_record_map.ra1
    
    
    @property
    def ra2(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.RA2`."""    
        return self.pv_record_map.ra2
    
    
    @property
    def rd1(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.RD1`."""    
        return self.pv_record_map.rd1
    
    
    @property
    def rd2(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.RD2`."""    
        return self.pv_record_map.rd2
    
    
    @property
    def rdy(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.RDY`."""    
        return self.pv_record_map.rdy
    
    
    @property
    def sa1(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.SA1`."""    
        return self.pv_record_map.sa1
    
    
    @property
    def sa2(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.SA2`."""    
        return self.pv_record_map.sa2
    
    
    @property
    def sd1(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.SD1`."""    
        return self.pv_record_map.sd1
    
    
    @property
    def sd2(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.SD2`."""    
        return self.pv_record_map.sd2
    
    
    @property
    def x(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.X`."""    
        return self.pv_record_map.x
    
    
    @property
    def y(self):
        """Default Getter implementation for :attr:`BPMPVMapModel.Y`."""    
        return self.pv_record_map.y
    
    

    


class BPMPropertiesModel(Properties):
    """
    Class for defining bpm-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    type: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            BPMPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class BPMModel(Hardware):
    """
    Middle layer class for interacting with a specific bpm object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[BPMControlsInformationModel]
    """Controls information pertaining to this bpm
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[BPMPropertiesModel]
    """Properties pertaining to this bpm
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""
    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            BPMModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            
            "AWAK",
            
            "RA1",
            
            "RA2",
            
            "RD1",
            
            "RD2",
            
            "RDY",
            
            "SA1",
            
            "SA2",
            
            "SD1",
            
            "SD2",
            
            "X",
            
            "Y",
            
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> BPMControlsInformationModel:
        try:
            return BPMControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> BPMPropertiesModel:
        try:
            return BPMPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def awak(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.AWAK`."""
        return self.controls_information.awak
    
    
    @property
    def ra1(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.RA1`."""
        return self.controls_information.ra1
    
    
    @property
    def ra2(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.RA2`."""
        return self.controls_information.ra2
    
    
    @property
    def rd1(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.RD1`."""
        return self.controls_information.rd1
    
    
    @property
    def rd2(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.RD2`."""
        return self.controls_information.rd2
    
    
    @property
    def rdy(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.RDY`."""
        return self.controls_information.rdy
    
    
    @property
    def sa1(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.SA1`."""
        return self.controls_information.sa1
    
    
    @property
    def sa2(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.SA2`."""
        return self.controls_information.sa2
    
    
    @property
    def sd1(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.SD1`."""
        return self.controls_information.sd1
    
    
    @property
    def sd2(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.SD2`."""
        return self.controls_information.sd2
    
    
    @property
    def x(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.X`."""
        return self.controls_information.x
    
    
    @property
    def y(self):
        """Default Getter implementation for :attr:`BPMControlsInformationModel.Y`."""
        return self.controls_information.y
    
    

class BPMFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.bpm.BPM` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(BPMFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=BPMModel,
            lattice_folder="BPM",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_bpm(self, name: Union[str, List[str]] = None) -> BPMModel:
        """
        Returns the bpm object for the given name(s).

        :param name: Name(s) of the bpm.
        :type name: str or list of str

        :return: Bpm object(s).
        :rtype: :class:`bpmModel.BPM`
        or Dict[str: :class:`bpm.BPM`]
        """
        return self.get_hardware(name)

    
    def awak(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.AWAK`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.AWAK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.awak)
    
    def ra1(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.RA1`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.RA1` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.ra1)
    
    def ra2(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.RA2`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.RA2` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.ra2)
    
    def rd1(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.RD1`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.RD1` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.rd1)
    
    def rd2(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.RD2`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.RD2` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.rd2)
    
    def rdy(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.RDY`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.RDY` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.rdy)
    
    def sa1(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.SA1`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.SA1` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sa1)
    
    def sa2(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.SA2`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.SA2` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sa2)
    
    def sd1(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.SD1`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.SD1` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sd1)
    
    def sd2(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.SD2`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.SD2` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.sd2)
    
    def x(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.X`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.X` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.x)
    
    def y(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`BPMModel.Y`.

        :param name: Name(s) of the bpm.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`BPMModel.Y` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda bpm: bpm.y)
    