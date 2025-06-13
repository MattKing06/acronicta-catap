
from catapcore.common.machine.pv_utils import StatisticalPV, BinaryPV, StatePV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class EnergyMeterPVMapModel(PVMap):
    
    
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
        EnergyMeterPVMapModel.is_virtual = is_virtual
        EnergyMeterPVMapModel.connect_on_creation = connect_on_creation
        super(
            EnergyMeterPVMapModel,
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
        
    
    



class EnergyMeterControlsInformationModel(ControlsInformation):
    """
    Class for controlling a energymeter via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[EnergyMeterPVMapModel]

    

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
        EnergyMeterControlsInformationModel.is_virtual = is_virtual
        EnergyMeterControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            EnergyMeterControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> EnergyMeterPVMapModel:
        return EnergyMeterPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def energyreadback(self):
        """Default Getter implementation for :attr:`EnergyMeterPVMapModel.ENERGYREADBACK`."""    
        return self.pv_record_map.energyreadback
    
    
    @property
    def overrange(self):
        """Default Getter implementation for :attr:`EnergyMeterPVMapModel.OVERRANGE`."""    
        return self.pv_record_map.overrange
    
    
    @property
    def rangesp(self):
        """Default Getter implementation for :attr:`EnergyMeterPVMapModel.RANGESP`."""    
        return self.pv_record_map.rangesp
    
    @rangesp.setter
    def rangesp(self, value):
        """Default Setter implementation for :attr:`EnergyMeterPVMapModel.RANGESP`.""" 
        self.pv_record_map.rangesp = value
    
    
    @property
    def runsp(self):
        """Default Getter implementation for :attr:`EnergyMeterPVMapModel.RUNSP`."""    
        return self.pv_record_map.runsp
    
    @runsp.setter
    def runsp(self, value):
        """Default Setter implementation for :attr:`EnergyMeterPVMapModel.RUNSP`.""" 
        self.pv_record_map.runsp = value
    
    

    


class EnergyMeterPropertiesModel(Properties):
    """
    Class for defining energymeter-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    type: str
    
    
    
    virtual_name: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            EnergyMeterPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class EnergyMeterModel(Hardware):
    """
    Middle layer class for interacting with a specific energymeter object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[EnergyMeterControlsInformationModel]
    """Controls information pertaining to this energymeter
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[EnergyMeterPropertiesModel]
    """Properties pertaining to this energymeter
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            EnergyMeterModel,
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
    def validate_controls_information(cls, v: Any) -> EnergyMeterControlsInformationModel:
        try:
            return EnergyMeterControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> EnergyMeterPropertiesModel:
        try:
            return EnergyMeterPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def energyreadback(self):
        """Default Getter implementation for :attr:`EnergyMeterControlsInformationModel.ENERGYREADBACK`."""
        return self.controls_information.energyreadback
    
    
    @property
    def overrange(self):
        """Default Getter implementation for :attr:`EnergyMeterControlsInformationModel.OVERRANGE`."""
        return self.controls_information.overrange
    
    
    @property
    def rangesp(self):
        """Default Getter implementation for :attr:`EnergyMeterControlsInformationModel.RANGESP`."""
        return self.controls_information.rangesp
    
    @rangesp.setter
    def rangesp(self, value):
        """Default Setter implementation for :attr:`EnergyMeterControlsInformationModel.RANGESP`."""
        self.controls_information.rangesp = value
    
    
    @property
    def runsp(self):
        """Default Getter implementation for :attr:`EnergyMeterControlsInformationModel.RUNSP`."""
        return self.controls_information.runsp
    
    @runsp.setter
    def runsp(self, value):
        """Default Setter implementation for :attr:`EnergyMeterControlsInformationModel.RUNSP`."""
        self.controls_information.runsp = value
    
    

class EnergyMeterFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.energymeter.EnergyMeter` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(EnergyMeterFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=EnergyMeterModel,
            lattice_folder="EnergyMeter",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_energymeter(self, name: Union[str, List[str]] = None) -> EnergyMeterModel:
        """
        Returns the energymeter object for the given name(s).

        :param name: Name(s) of the energymeter.
        :type name: str or list of str

        :return: Energymeter object(s).
        :rtype: :class:`energymeterModel.EnergyMeter`
        or Dict[str: :class:`energymeter.EnergyMeter`]
        """
        return self.get_hardware(name)

    
    def energyreadback(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`EnergyMeterModel.ENERGYREADBACK`.

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`EnergyMeterModel.ENERGYREADBACK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.energyreadback)
    
    def overrange(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`EnergyMeterModel.OVERRANGE`.

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`EnergyMeterModel.OVERRANGE` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.overrange)
    
    def rangesp(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`EnergyMeterModel.RANGESP`.

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`EnergyMeterModel.RANGESP` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.rangesp)
    
    def runsp(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`EnergyMeterModel.RUNSP`.

        :param name: Name(s) of the energymeter.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`EnergyMeterModel.RUNSP` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda energymeter: energymeter.runsp)
    