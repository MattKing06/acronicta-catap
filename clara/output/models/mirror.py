
from catapcore.common.machine.pv_utils import ScalarPV, BinaryPV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class MirrorPVMapModel(PVMap):
    
    
    H_MREL: ScalarPV
    
    """Step-size for horizontal motor"""
    
    
    H_POS: ScalarPV
    
    """Position for horizontal motor"""
    
    
    V_MREL: ScalarPV
    
    """Step-size for vertical motor"""
    
    
    POSBTN: BinaryPV = None
    
    """Trigger movement for the mirror"""
    
    
    V_POS: ScalarPV
    
    """Position for vertical motor"""
    
    
    H_MREL_RBV: ScalarPV = None
    
    """Readback for horizontal motor step-size"""
    
    
    V_MREL_RBV: ScalarPV = None
    
    """Readback for the vertical motor step-size"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        MirrorPVMapModel.is_virtual = is_virtual
        MirrorPVMapModel.connect_on_creation = connect_on_creation
        super(
            MirrorPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def h_mrel(self):
        """Default Getter implementation for H_MREL"""
        
        return self.H_MREL.get()
        

    
    @h_mrel.setter
    def h_mrel(self, value):
        """Default Setter implementation for H_MREL"""
        
        return self.H_MREL.put(value)
        
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for H_POS"""
        
        return self.H_POS.get()
        

    
    
    @property
    def v_mrel(self):
        """Default Getter implementation for V_MREL"""
        
        return self.V_MREL.get()
        

    
    @v_mrel.setter
    def v_mrel(self, value):
        """Default Setter implementation for V_MREL"""
        
        return self.V_MREL.put(value)
        
    
    
    @property
    def posbtn(self):
        """Default Getter implementation for POSBTN"""
        
        if self.POSBTN:
            return self.POSBTN.get()
        

    
    @posbtn.setter
    def posbtn(self, value):
        """Default Setter implementation for POSBTN"""
        
        if self.POSBTN:
            return self.POSBTN.put(value)
        
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for V_POS"""
        
        return self.V_POS.get()
        

    
    
    @property
    def h_mrel_rbv(self):
        """Default Getter implementation for H_MREL_RBV"""
        
        if self.H_MREL_RBV:
            return self.H_MREL_RBV.get()
        

    
    
    @property
    def v_mrel_rbv(self):
        """Default Getter implementation for V_MREL_RBV"""
        
        if self.V_MREL_RBV:
            return self.V_MREL_RBV.get()
        

    
    



class MirrorControlsInformationModel(ControlsInformation):
    """
    Class for controlling a mirror via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[MirrorPVMapModel]

    
    
    step_max: float
    
    
    
    default_step: float
    
    

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
        MirrorControlsInformationModel.is_virtual = is_virtual
        MirrorControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            MirrorControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> MirrorPVMapModel:
        return MirrorPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def h_mrel(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.H_MREL`."""    
        return self.pv_record_map.h_mrel
    
    @h_mrel.setter
    def h_mrel(self, value):
        """Default Setter implementation for :attr:`MirrorPVMapModel.H_MREL`.""" 
        self.pv_record_map.h_mrel = value
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.H_POS`."""    
        return self.pv_record_map.h_pos
    
    
    @property
    def v_mrel(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.V_MREL`."""    
        return self.pv_record_map.v_mrel
    
    @v_mrel.setter
    def v_mrel(self, value):
        """Default Setter implementation for :attr:`MirrorPVMapModel.V_MREL`.""" 
        self.pv_record_map.v_mrel = value
    
    
    @property
    def posbtn(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.POSBTN`."""    
        return self.pv_record_map.posbtn
    
    @posbtn.setter
    def posbtn(self, value):
        """Default Setter implementation for :attr:`MirrorPVMapModel.POSBTN`.""" 
        self.pv_record_map.posbtn = value
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.V_POS`."""    
        return self.pv_record_map.v_pos
    
    
    @property
    def h_mrel_rbv(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.H_MREL_RBV`."""    
        return self.pv_record_map.h_mrel_rbv
    
    
    @property
    def v_mrel_rbv(self):
        """Default Getter implementation for :attr:`MirrorPVMapModel.V_MREL_RBV`."""    
        return self.pv_record_map.v_mrel_rbv
    
    

    
    @property
    def step_max(self) -> float:
        """Default Getter implementation for step_max."""
        
        return self.step_max
        
    
    @property
    def default_step(self) -> float:
        """Default Getter implementation for default_step."""
        
        return self.default_step
        
    


class MirrorPropertiesModel(Properties):
    """
    Class for defining mirror-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    virtual_name: str
    
    
    
    horizontal_channel: int = None
    
    
    
    vertical_channel: int = None
    
    

    def __init__(self, *args, **kwargs):
        super(
            MirrorPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class MirrorModel(Hardware):
    """
    Middle layer class for interacting with a specific mirror object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[MirrorControlsInformationModel]
    """Controls information pertaining to this mirror
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[MirrorPropertiesModel]
    """Properties pertaining to this mirror
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""
    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            MirrorModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            
            "H_MREL",
            
            "H_POS",
            
            "V_MREL",
            
            "POSBTN",
            
            "V_POS",
            
            "H_MREL_RBV",
            
            "V_MREL_RBV",
            
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> MirrorControlsInformationModel:
        try:
            return MirrorControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> MirrorPropertiesModel:
        try:
            return MirrorPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def h_mrel(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.H_MREL`."""
        return self.controls_information.h_mrel
    
    @h_mrel.setter
    def h_mrel(self, value):
        """Default Setter implementation for :attr:`MirrorControlsInformationModel.H_MREL`."""
        self.controls_information.h_mrel = value
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.H_POS`."""
        return self.controls_information.h_pos
    
    
    @property
    def v_mrel(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.V_MREL`."""
        return self.controls_information.v_mrel
    
    @v_mrel.setter
    def v_mrel(self, value):
        """Default Setter implementation for :attr:`MirrorControlsInformationModel.V_MREL`."""
        self.controls_information.v_mrel = value
    
    
    @property
    def posbtn(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.POSBTN`."""
        return self.controls_information.posbtn
    
    @posbtn.setter
    def posbtn(self, value):
        """Default Setter implementation for :attr:`MirrorControlsInformationModel.POSBTN`."""
        self.controls_information.posbtn = value
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.V_POS`."""
        return self.controls_information.v_pos
    
    
    @property
    def h_mrel_rbv(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.H_MREL_RBV`."""
        return self.controls_information.h_mrel_rbv
    
    
    @property
    def v_mrel_rbv(self):
        """Default Getter implementation for :attr:`MirrorControlsInformationModel.V_MREL_RBV`."""
        return self.controls_information.v_mrel_rbv
    
    

class MirrorFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.mirror.Mirror` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(MirrorFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=MirrorModel,
            lattice_folder="Mirror",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_mirror(self, name: Union[str, List[str]] = None) -> MirrorModel:
        """
        Returns the mirror object for the given name(s).

        :param name: Name(s) of the mirror.
        :type name: str or list of str

        :return: Mirror object(s).
        :rtype: :class:`mirrorModel.Mirror`
        or Dict[str: :class:`mirror.Mirror`]
        """
        return self.get_hardware(name)

    
    def h_mrel(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.H_MREL`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.H_MREL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.h_mrel)
    
    def h_pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.H_POS`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.H_POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.h_pos)
    
    def v_mrel(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.V_MREL`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.V_MREL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.v_mrel)
    
    def posbtn(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.POSBTN`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.POSBTN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.posbtn)
    
    def v_pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.V_POS`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.V_POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.v_pos)
    
    def h_mrel_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.H_MREL_RBV`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.H_MREL_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.h_mrel_rbv)
    
    def v_mrel_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`MirrorModel.V_MREL_RBV`.

        :param name: Name(s) of the mirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`MirrorModel.V_MREL_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda mirror: mirror.v_mrel_rbv)
    