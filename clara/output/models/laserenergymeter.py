
from CATAP.common.machine.pv_utils import StatisticalPV, BinaryPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class LaserEnergyMeterPVMapModel(PVMap):
    
    
    ENERGYREADBACK: StatisticalPV
    
    """Readback of the measured laser energy"""
    
    
    OVERRANGE: BinaryPV
    
    """State of energy readback being over-range set in RANGESP"""
    
    
    RANGESP: StatePV
    
    """Set the state range for energy readback"""
    
    
    RUNSP: BinaryPV
    
    """Enable/Disable the energy meter"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        LaserEnergyMeterPVMapModel.is_virtual = is_virtual
        LaserEnergyMeterPVMapModel.connect_on_creation = connect_on_creation
        super(
            LaserEnergyMeterPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def energyreadback(self):
        """Default Getter implementation for ENERGYREADBACK"""
        
        return self.ENERGYREADBACK.get()
        

    
    
    @property
    def overrange(self):
        """Default Getter implementation for OVERRANGE"""
        
        return self.OVERRANGE.get()
        

    
    
    @property
    def rangesp(self):
        """Default Getter implementation for RANGESP"""
        
        return self.RANGESP.get()
        

    
    @rangesp.setter
    def rangesp(self, value):
        """Default Setter implementation for RANGESP"""
        
        return self.RANGESP.put(value)
        
    
    
    @property
    def runsp(self):
        """Default Getter implementation for RUNSP"""
        
        return self.RUNSP.get()
        

    
    @runsp.setter
    def runsp(self, value):
        """Default Setter implementation for RUNSP"""
        
        return self.RUNSP.put(value)
        
    
    



class LaserEnergyMeterControlsInformationModel(ControlsInformation):
    """
    Class for controlling a laserenergymeter via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[LaserEnergyMeterPVMapModel]

    

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
        LaserEnergyMeterControlsInformationModel.is_virtual = is_virtual
        LaserEnergyMeterControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            LaserEnergyMeterControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> LaserEnergyMeterPVMapModel:
        return LaserEnergyMeterPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def energyreadback(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterPVMapModel.ENERGYREADBACK`."""    
        return self.pv_record_map.energyreadback
    
    
    @property
    def overrange(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterPVMapModel.OVERRANGE`."""    
        return self.pv_record_map.overrange
    
    
    @property
    def rangesp(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterPVMapModel.RANGESP`."""    
        return self.pv_record_map.rangesp
    
    @rangesp.setter
    def rangesp(self, value):
        """Default Setter implementation for :attr:`LaserEnergyMeterPVMapModel.RANGESP`.""" 
        self.pv_record_map.rangesp = value
    
    
    @property
    def runsp(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterPVMapModel.RUNSP`."""    
        return self.pv_record_map.runsp
    
    @runsp.setter
    def runsp(self, value):
        """Default Setter implementation for :attr:`LaserEnergyMeterPVMapModel.RUNSP`.""" 
        self.pv_record_map.runsp = value
    
    

    


class LaserEnergyMeterPropertiesModel(Properties):
    """
    Class for defining laserenergymeter-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    calibration_factor: float
    
    

    def __init__(self, *args, **kwargs):
        super(
            LaserEnergyMeterPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class LaserEnergyMeterModel(Hardware):
    """
    Middle layer class for interacting with a specific laserenergymeter object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[LaserEnergyMeterControlsInformationModel]
    """Controls information pertaining to this laserenergymeter
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[LaserEnergyMeterPropertiesModel]
    """Properties pertaining to this laserenergymeter
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            LaserEnergyMeterModel,
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
    def validate_controls_information(cls, v: Any) -> LaserEnergyMeterControlsInformationModel:
        try:
            return LaserEnergyMeterControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> LaserEnergyMeterPropertiesModel:
        try:
            return LaserEnergyMeterPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def energyreadback(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterControlsInformationModel.ENERGYREADBACK`."""
        return self.controls_information.energyreadback
    
    
    @property
    def overrange(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterControlsInformationModel.OVERRANGE`."""
        return self.controls_information.overrange
    
    
    @property
    def rangesp(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterControlsInformationModel.RANGESP`."""
        return self.controls_information.rangesp
    
    @rangesp.setter
    def rangesp(self, value):
        """Default Setter implementation for :attr:`LaserEnergyMeterControlsInformationModel.RANGESP`."""
        self.controls_information.rangesp = value
    
    
    @property
    def runsp(self):
        """Default Getter implementation for :attr:`LaserEnergyMeterControlsInformationModel.RUNSP`."""
        return self.controls_information.runsp
    
    @runsp.setter
    def runsp(self, value):
        """Default Setter implementation for :attr:`LaserEnergyMeterControlsInformationModel.RUNSP`."""
        self.controls_information.runsp = value
    
    

class LaserEnergyMeterFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.laserenergymeter.LaserEnergyMeter` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(LaserEnergyMeterFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=LaserEnergyMeterModel,
            lattice_folder="LaserEnergyMeter",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_laserenergymeter(self, name: Union[str, List[str]] = None) -> LaserEnergyMeterModel:
        """
        Returns the laserenergymeter object for the given name(s).

        :param name: Name(s) of the laserenergymeter.
        :type name: str or list of str

        :return: Laserenergymeter object(s).
        :rtype: :class:`laserenergymeterModel.LaserEnergyMeter`
        or Dict[str: :class:`laserenergymeter.LaserEnergyMeter`]
        """
        return self.get_hardware(name)

    
    def energyreadback(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserEnergyMeterModel.ENERGYREADBACK`.

        :param name: Name(s) of the laserenergymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserEnergyMeterModel.ENERGYREADBACK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda laserenergymeter: laserenergymeter.energyreadback)
    
    def overrange(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserEnergyMeterModel.OVERRANGE`.

        :param name: Name(s) of the laserenergymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserEnergyMeterModel.OVERRANGE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda laserenergymeter: laserenergymeter.overrange)
    
    def rangesp(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserEnergyMeterModel.RANGESP`.

        :param name: Name(s) of the laserenergymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserEnergyMeterModel.RANGESP` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda laserenergymeter: laserenergymeter.rangesp)
    
    def runsp(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserEnergyMeterModel.RUNSP`.

        :param name: Name(s) of the laserenergymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserEnergyMeterModel.RUNSP` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda laserenergymeter: laserenergymeter.runsp)
    