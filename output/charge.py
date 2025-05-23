
from CATAP.common.machine.pv_utils import StatisticalPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class ChargePVMap(PVMap):
    
    Q: StatisticalPV
    
    DQ: StatisticalPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        ChargePVMap.is_virtual = is_virtual
        ChargePVMap.connect_on_creation = connect_on_creation
        super(
            ChargePVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def q(self):
        return self.Q.get()
    
    
    @property
    def dq(self):
        return self.DQ.get()
    
    



class ChargeControlsInformation(ControlsInformation):
    """
    Class for controlling a charge via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[ChargePVMap]
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
        ChargeControlsInformation.is_virtual = is_virtual
        ChargeControlsInformation.connect_on_creation = connect_on_creation
        super(
            ChargeControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> ChargePVMap:
        return ChargePVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def q(self):
        return self.pv_record_map.q
    
    
    @property
    def dq(self):
        return self.pv_record_map.dq
    
    


class ChargeProperties(Properties):
    """
    Class for defining charge-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    type: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            ChargeProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def type(self):
        return self.type
    

    

class Charge(Hardware):
    """
    Middle layer class for interacting with a specific charge object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[ChargeControlsInformation]
    """Controls information pertaining to this charge
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[ChargeProperties]
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
            Charge,
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
    def validate_controls_information(cls, v: Any) -> ChargeControlsInformation:
        try:
            return ChargeControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> ChargeProperties:
        try:
            return ChargeProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def q(self):
        return self.controls_information.q
    
    
    @property
    def dq(self):
        return self.controls_information.dq
    
    

class ChargeFactory(Factory):
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
        super(ChargeFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Charge,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_charge(self, name: Union[str, List[str]] = None) -> Charge:
        """
        Returns the charge object for the given name(s).

        :param name: Name(s) of the charge.
        :type name: str or list of str

        :return: Charge object(s).
        :rtype: :class:`~CATAP.laser.components.charge.Charge`
        or Dict[str: :class:`~CATAP.laser.components.charge.Charge`]
        """
        return self.get_hardware(name)

    
    def q(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'q' property of the charge(s).

        :param name: Name(s) of the charge.
        :type name: str or list of str or None

        :return: Value(s) of the 'Q' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda charge: charge.q)
    
    def dq(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'dq' property of the charge(s).

        :param name: Name(s) of the charge.
        :type name: str or list of str or None

        :return: Value(s) of the 'DQ' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda charge: charge.dq)
    