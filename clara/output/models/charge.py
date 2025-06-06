
from CATAP.common.machine.pv_utils import StatisticalPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ChargePVMapModel(PVMap):
    
    
    Q: StatisticalPV
    
    """Bunch charge"""
    
    
    DQ: StatisticalPV
    
    """Dark current"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ChargePVMapModel.is_virtual = is_virtual
        ChargePVMapModel.connect_on_creation = connect_on_creation
        super(
            ChargePVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def q(self):
        """Default Getter implementation for Q"""
        
        return self.Q.get()
        

    
    
    @property
    def dq(self):
        """Default Getter implementation for DQ"""
        
        return self.DQ.get()
        

    
    



class ChargeControlsInformationModel(ControlsInformation):
    """
    Class for controlling a charge via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ChargePVMapModel]

    

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
        ChargeControlsInformationModel.is_virtual = is_virtual
        ChargeControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            ChargeControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ChargePVMapModel:
        return ChargePVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def q(self):
        """Default Getter implementation for :attr:`ChargePVMapModel.Q`."""    
        return self.pv_record_map.q
    
    
    @property
    def dq(self):
        """Default Getter implementation for :attr:`ChargePVMapModel.DQ`."""    
        return self.pv_record_map.dq
    
    

    


class ChargePropertiesModel(Properties):
    """
    Class for defining charge-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    type: str
    
    
    
    virtual_name: str
    
    

    def __init__(self, *args, **kwargs):
        super(
            ChargePropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class ChargeModel(Hardware):
    """
    Middle layer class for interacting with a specific charge object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ChargeControlsInformationModel]
    """Controls information pertaining to this charge
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ChargePropertiesModel]
    """Properties pertaining to this charge
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            ChargeModel,
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
    def validate_controls_information(cls, v: Any) -> ChargeControlsInformationModel:
        try:
            return ChargeControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ChargePropertiesModel:
        try:
            return ChargePropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def q(self):
        """Default Getter implementation for :attr:`ChargeControlsInformationModel.Q`."""
        return self.controls_information.q
    
    
    @property
    def dq(self):
        """Default Getter implementation for :attr:`ChargeControlsInformationModel.DQ`."""
        return self.controls_information.dq
    
    

class ChargeFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.charge.Charge` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(ChargeFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=ChargeModel,
            lattice_folder="Charge",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_charge(self, name: Union[str, List[str]] = None) -> ChargeModel:
        """
        Returns the charge object for the given name(s).

        :param name: Name(s) of the charge.
        :type name: str or list of str

        :return: Charge object(s).
        :rtype: :class:`chargeModel.Charge`
        or Dict[str: :class:`charge.Charge`]
        """
        return self.get_hardware(name)

    
    def q(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ChargeModel.Q`.

        :param name: Name(s) of the charge.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ChargeModel.Q` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda charge: charge.q)
    
    def dq(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`ChargeModel.DQ`.

        :param name: Name(s) of the charge.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`ChargeModel.DQ` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda charge: charge.dq)
    