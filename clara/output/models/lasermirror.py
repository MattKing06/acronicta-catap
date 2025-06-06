
from CATAP.common.machine.pv_utils import ScalarPV, BinaryPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class LaserMirrorPVMapModel(PVMap):
    
    
    H_MREL: ScalarPV
    
    """Step-size for horizontal motor"""
    
    
    H_POS: ScalarPV
    
    """Position for horizontal motor"""
    
    
    POSBTN: BinaryPV = None
    
    """Trigger movement for the mirror"""
    
    
    V_MREL: ScalarPV
    
    """Step-size for vertical motor"""
    
    
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
        LaserMirrorPVMapModel.is_virtual = is_virtual
        LaserMirrorPVMapModel.connect_on_creation = connect_on_creation
        super(
            LaserMirrorPVMapModel,
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
    def v_mrel(self):
        """Default Getter implementation for V_MREL"""
        
        return self.V_MREL.get()
        

    
    @v_mrel.setter
    def v_mrel(self, value):
        """Default Setter implementation for V_MREL"""
        
        return self.V_MREL.put(value)
        
    
    
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
        

    
    



class LaserMirrorControlsInformationModel(ControlsInformation):
    """
    Class for controlling a lasermirror via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[LaserMirrorPVMapModel]

    
    
    step_max: float
    
    
    
    default_step: float
    
    
    
    right_sense: int
    
    
    
    up_sense: int
    
    
    
    left_sense: int
    
    
    
    down_sense: int
    
    

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
        LaserMirrorControlsInformationModel.is_virtual = is_virtual
        LaserMirrorControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            LaserMirrorControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> LaserMirrorPVMapModel:
        return LaserMirrorPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def h_mrel(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.H_MREL`."""    
        return self.pv_record_map.h_mrel
    
    @h_mrel.setter
    def h_mrel(self, value):
        """Default Setter implementation for :attr:`LaserMirrorPVMapModel.H_MREL`.""" 
        self.pv_record_map.h_mrel = value
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.H_POS`."""    
        return self.pv_record_map.h_pos
    
    
    @property
    def posbtn(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.POSBTN`."""    
        return self.pv_record_map.posbtn
    
    @posbtn.setter
    def posbtn(self, value):
        """Default Setter implementation for :attr:`LaserMirrorPVMapModel.POSBTN`.""" 
        self.pv_record_map.posbtn = value
    
    
    @property
    def v_mrel(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.V_MREL`."""    
        return self.pv_record_map.v_mrel
    
    @v_mrel.setter
    def v_mrel(self, value):
        """Default Setter implementation for :attr:`LaserMirrorPVMapModel.V_MREL`.""" 
        self.pv_record_map.v_mrel = value
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.V_POS`."""    
        return self.pv_record_map.v_pos
    
    
    @property
    def h_mrel_rbv(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.H_MREL_RBV`."""    
        return self.pv_record_map.h_mrel_rbv
    
    
    @property
    def v_mrel_rbv(self):
        """Default Getter implementation for :attr:`LaserMirrorPVMapModel.V_MREL_RBV`."""    
        return self.pv_record_map.v_mrel_rbv
    
    

    
    @property
    def step_max(self) -> float:
        """Default Getter implementation for step_max."""
        
        return self.step_max
        
    
    @property
    def default_step(self) -> float:
        """Default Getter implementation for default_step."""
        
        return self.default_step
        
    
    @property
    def right_sense(self) -> int:
        """Default Getter implementation for right_sense."""
        
        return self.right_sense
        
    
    @property
    def up_sense(self) -> int:
        """Default Getter implementation for up_sense."""
        
        return self.up_sense
        
    
    @property
    def left_sense(self) -> int:
        """Default Getter implementation for left_sense."""
        
        return self.left_sense
        
    
    @property
    def down_sense(self) -> int:
        """Default Getter implementation for down_sense."""
        
        return self.down_sense
        
    


class LaserMirrorPropertiesModel(Properties):
    """
    Class for defining lasermirror-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    virtual_name: str
    
    
    
    horizontal_channel: int = None
    
    
    
    vertical_channel: int = None
    
    

    def __init__(self, *args, **kwargs):
        super(
            LaserMirrorPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class LaserMirrorModel(Hardware):
    """
    Middle layer class for interacting with a specific lasermirror object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[LaserMirrorControlsInformationModel]
    """Controls information pertaining to this lasermirror
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[LaserMirrorPropertiesModel]
    """Properties pertaining to this lasermirror
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            LaserMirrorModel,
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
    def validate_controls_information(cls, v: Any) -> LaserMirrorControlsInformationModel:
        try:
            return LaserMirrorControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> LaserMirrorPropertiesModel:
        try:
            return LaserMirrorPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def h_mrel(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.H_MREL`."""
        return self.controls_information.h_mrel
    
    @h_mrel.setter
    def h_mrel(self, value):
        """Default Setter implementation for :attr:`LaserMirrorControlsInformationModel.H_MREL`."""
        self.controls_information.h_mrel = value
    
    
    @property
    def h_pos(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.H_POS`."""
        return self.controls_information.h_pos
    
    
    @property
    def posbtn(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.POSBTN`."""
        return self.controls_information.posbtn
    
    @posbtn.setter
    def posbtn(self, value):
        """Default Setter implementation for :attr:`LaserMirrorControlsInformationModel.POSBTN`."""
        self.controls_information.posbtn = value
    
    
    @property
    def v_mrel(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.V_MREL`."""
        return self.controls_information.v_mrel
    
    @v_mrel.setter
    def v_mrel(self, value):
        """Default Setter implementation for :attr:`LaserMirrorControlsInformationModel.V_MREL`."""
        self.controls_information.v_mrel = value
    
    
    @property
    def v_pos(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.V_POS`."""
        return self.controls_information.v_pos
    
    
    @property
    def h_mrel_rbv(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.H_MREL_RBV`."""
        return self.controls_information.h_mrel_rbv
    
    
    @property
    def v_mrel_rbv(self):
        """Default Getter implementation for :attr:`LaserMirrorControlsInformationModel.V_MREL_RBV`."""
        return self.controls_information.v_mrel_rbv
    
    

class LaserMirrorFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.lasermirror.LaserMirror` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(LaserMirrorFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=LaserMirrorModel,
            lattice_folder="LaserMirror",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_lasermirror(self, name: Union[str, List[str]] = None) -> LaserMirrorModel:
        """
        Returns the lasermirror object for the given name(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str

        :return: Lasermirror object(s).
        :rtype: :class:`lasermirrorModel.LaserMirror`
        or Dict[str: :class:`lasermirror.LaserMirror`]
        """
        return self.get_hardware(name)

    
    def h_mrel(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.H_MREL`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.H_MREL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.h_mrel)
    
    def h_pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.H_POS`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.H_POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.h_pos)
    
    def posbtn(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.POSBTN`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.POSBTN` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.posbtn)
    
    def v_mrel(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.V_MREL`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.V_MREL` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.v_mrel)
    
    def v_pos(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.V_POS`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.V_POS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.v_pos)
    
    def h_mrel_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.H_MREL_RBV`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.H_MREL_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.h_mrel_rbv)
    
    def v_mrel_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`LaserMirrorModel.V_MREL_RBV`.

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`LaserMirrorModel.V_MREL_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.v_mrel_rbv)
    