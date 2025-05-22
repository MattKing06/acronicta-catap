
from CATAP.common.machine.pv_utils import ScalarPV, BinaryPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class LaserMirrorPVMap(PVMap):
    
    H_MREL: ScalarPV
    
    H_POS: ScalarPV
    
    POSBTN: BinaryPV
    
    V_MREL: ScalarPV
    
    V_POS: ScalarPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        LaserMirrorPVMap.is_virtual = is_virtual
        LaserMirrorPVMap.connect_on_creation = connect_on_creation
        super(
            LaserMirrorPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def h_mrel(self):
        return self.H_MREL.get()
    
    @h_mrel.setter
    def h_mrel(self, value):
        self.H_MREL.put(value)
    
    
    @property
    def h_pos(self):
        return self.H_POS.get()
    
    
    @property
    def posbtn(self):
        return self.POSBTN.get()
    
    @posbtn.setter
    def posbtn(self, value):
        self.POSBTN.put(value)
    
    
    @property
    def v_mrel(self):
        return self.V_MREL.get()
    
    @v_mrel.setter
    def v_mrel(self, value):
        self.V_MREL.put(value)
    
    
    @property
    def v_pos(self):
        return self.V_POS.get()
    
    



class LaserMirrorControlsInformation(ControlsInformation):
    """
    Class for controlling a lasermirror via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[LaserMirrorPVMap]
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
        LaserMirrorControlsInformation.is_virtual = is_virtual
        LaserMirrorControlsInformation.connect_on_creation = connect_on_creation
        super(
            LaserMirrorControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> LaserMirrorPVMap:
        return LaserMirrorPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def h_mrel(self):
        return self.pv_record_map.h_mrel
    
    @h_mrel.setter
    def h_mrel(self, value):
        self.pv_record_map.h_mrel = value
    
    
    @property
    def h_pos(self):
        return self.pv_record_map.h_pos
    
    
    @property
    def posbtn(self):
        return self.pv_record_map.posbtn
    
    @posbtn.setter
    def posbtn(self, value):
        self.pv_record_map.posbtn = value
    
    
    @property
    def v_mrel(self):
        return self.pv_record_map.v_mrel
    
    @v_mrel.setter
    def v_mrel(self, value):
        self.pv_record_map.v_mrel = value
    
    
    @property
    def v_pos(self):
        return self.pv_record_map.v_pos
    
    


class LaserMirrorProperties(Properties):
    """
    Class for defining lasermirror-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    virtual_name: str
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            LaserMirrorProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def virtual_name(self):
        return self.virtual_name
    

    

class LaserMirror(Hardware):
    """
    Middle layer class for interacting with a specific lasermirror object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[LaserMirrorControlsInformation]
    """Controls information pertaining to this lasermirror
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[LaserMirrorProperties]
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
            LaserMirror,
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
    def validate_controls_information(cls, v: Any) -> LaserMirrorControlsInformation:
        try:
            return LaserMirrorControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> LaserMirrorProperties:
        try:
            return LaserMirrorProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def h_mrel(self):
        return self.controls_information.h_mrel
    
    @h_mrel.setter
    def h_mrel(self, value):
        self.controls_information.h_mrel = value
    
    
    @property
    def h_pos(self):
        return self.controls_information.h_pos
    
    
    @property
    def posbtn(self):
        return self.controls_information.posbtn
    
    @posbtn.setter
    def posbtn(self, value):
        self.controls_information.posbtn = value
    
    
    @property
    def v_mrel(self):
        return self.controls_information.v_mrel
    
    @v_mrel.setter
    def v_mrel(self, value):
        self.controls_information.v_mrel = value
    
    
    @property
    def v_pos(self):
        return self.controls_information.v_pos
    
    

class LaserMirrorFactory(Factory):
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
        super(LaserMirrorFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=LaserMirror,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_lasermirror(self, name: Union[str, List[str]] = None) -> LaserMirror:
        """
        Returns the lasermirror object for the given name(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str

        :return: Lasermirror object(s).
        :rtype: :class:`~CATAP.laser.components.lasermirror.LaserMirror`
        or Dict[str: :class:`~CATAP.laser.components.lasermirror.LaserMirror`]
        """
        return self.get_hardware(name)

    
    def h_mrel(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'h_mrel' property of the lasermirror(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the 'H_MREL' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.h_mrel)
    
    def h_pos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'h_pos' property of the lasermirror(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the 'H_POS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.h_pos)
    
    def posbtn(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'posbtn' property of the lasermirror(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the 'POSBTN' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.posbtn)
    
    def v_mrel(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'v_mrel' property of the lasermirror(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the 'V_MREL' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.v_mrel)
    
    def v_pos(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'v_pos' property of the lasermirror(s).

        :param name: Name(s) of the lasermirror.
        :type name: str or list of str or None

        :return: Value(s) of the 'V_POS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda lasermirror: lasermirror.v_pos)
    