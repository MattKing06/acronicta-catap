
from CATAP.common.machine.pv_utils import BinaryPV, StatePV, ScalarPV, StatisticalPV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class CavityPVMap(PVMap):
    
    SetStartup: BinaryPV
    
    StartupComplete: BinaryPV
    
    APIEnable: BinaryPV
    
    GetAPITrip: StatePV
    
    SetAPITrip: BinaryPV
    
    GetStatus: StatePV
    
    PowerPIDSet: BinaryPV
    
    PowerPIDStatus: StatePV
    
    PowerPIDError: BinaryPV
    
    PhasePIDSet: BinaryPV
    
    PhasePIDStatus: StatePV
    
    PhasePIDError: BinaryPV
    
    TimeRemaining: ScalarPV
    
    ModVoltSet: ScalarPV
    
    ModVoltRead: StatisticalPV
    
    PowerMWSet: ScalarPV
    
    PhaseSet: ScalarPV
    
    PowerMWMax: ScalarPV
    
    PowerMWRead: StatisticalPV
    
    PhaseRead: StatisticalPV
    
    CrestPhaseSet: ScalarPV
    
    OffCrestPhaseSet: ScalarPV
    
    OffCrestPhaseRead: StatisticalPV
    
    BeamMomentum: ScalarPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        CavityPVMap.is_virtual = is_virtual
        CavityPVMap.connect_on_creation = connect_on_creation
        super(
            CavityPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def setstartup(self):
        return self.SetStartup.get()
    
    @setstartup.setter
    def setstartup(self, value):
        self.SetStartup.put(value)
    
    
    @property
    def startupcomplete(self):
        return self.StartupComplete.get()
    
    
    @property
    def apienable(self):
        return self.APIEnable.get()
    
    @apienable.setter
    def apienable(self, value):
        self.APIEnable.put(value)
    
    
    @property
    def getapitrip(self):
        return self.GetAPITrip.get()
    
    
    @property
    def setapitrip(self):
        return self.SetAPITrip.get()
    
    @setapitrip.setter
    def setapitrip(self, value):
        self.SetAPITrip.put(value)
    
    
    @property
    def getstatus(self):
        return self.GetStatus.get()
    
    
    @property
    def powerpidset(self):
        return self.PowerPIDSet.get()
    
    @powerpidset.setter
    def powerpidset(self, value):
        self.PowerPIDSet.put(value)
    
    
    @property
    def powerpidstatus(self):
        return self.PowerPIDStatus.get()
    
    
    @property
    def powerpiderror(self):
        return self.PowerPIDError.get()
    
    
    @property
    def phasepidset(self):
        return self.PhasePIDSet.get()
    
    @phasepidset.setter
    def phasepidset(self, value):
        self.PhasePIDSet.put(value)
    
    
    @property
    def phasepidstatus(self):
        return self.PhasePIDStatus.get()
    
    
    @property
    def phasepiderror(self):
        return self.PhasePIDError.get()
    
    
    @property
    def timeremaining(self):
        return self.TimeRemaining.get()
    
    
    @property
    def modvoltset(self):
        return self.ModVoltSet.get()
    
    
    @property
    def modvoltread(self):
        return self.ModVoltRead.get()
    
    
    @property
    def powermwset(self):
        return self.PowerMWSet.get()
    
    @powermwset.setter
    def powermwset(self, value):
        self.PowerMWSet.put(value)
    
    
    @property
    def phaseset(self):
        return self.PhaseSet.get()
    
    @phaseset.setter
    def phaseset(self, value):
        self.PhaseSet.put(value)
    
    
    @property
    def powermwmax(self):
        return self.PowerMWMax.get()
    
    
    @property
    def powermwread(self):
        return self.PowerMWRead.get()
    
    
    @property
    def phaseread(self):
        return self.PhaseRead.get()
    
    
    @property
    def crestphaseset(self):
        return self.CrestPhaseSet.get()
    
    @crestphaseset.setter
    def crestphaseset(self, value):
        self.CrestPhaseSet.put(value)
    
    
    @property
    def offcrestphaseset(self):
        return self.OffCrestPhaseSet.get()
    
    @offcrestphaseset.setter
    def offcrestphaseset(self, value):
        self.OffCrestPhaseSet.put(value)
    
    
    @property
    def offcrestphaseread(self):
        return self.OffCrestPhaseRead.get()
    
    
    @property
    def beammomentum(self):
        return self.BeamMomentum.get()
    
    @beammomentum.setter
    def beammomentum(self, value):
        self.BeamMomentum.put(value)
    
    



class CavityControlsInformation(ControlsInformation):
    """
    Class for controlling a cavity via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[CavityPVMap]
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
        CavityControlsInformation.is_virtual = is_virtual
        CavityControlsInformation.connect_on_creation = connect_on_creation
        super(
            CavityControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> CavityPVMap:
        return CavityPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def setstartup(self):
        return self.pv_record_map.setstartup
    
    @setstartup.setter
    def setstartup(self, value):
        self.pv_record_map.setstartup = value
    
    
    @property
    def startupcomplete(self):
        return self.pv_record_map.startupcomplete
    
    
    @property
    def apienable(self):
        return self.pv_record_map.apienable
    
    @apienable.setter
    def apienable(self, value):
        self.pv_record_map.apienable = value
    
    
    @property
    def getapitrip(self):
        return self.pv_record_map.getapitrip
    
    
    @property
    def setapitrip(self):
        return self.pv_record_map.setapitrip
    
    @setapitrip.setter
    def setapitrip(self, value):
        self.pv_record_map.setapitrip = value
    
    
    @property
    def getstatus(self):
        return self.pv_record_map.getstatus
    
    
    @property
    def powerpidset(self):
        return self.pv_record_map.powerpidset
    
    @powerpidset.setter
    def powerpidset(self, value):
        self.pv_record_map.powerpidset = value
    
    
    @property
    def powerpidstatus(self):
        return self.pv_record_map.powerpidstatus
    
    
    @property
    def powerpiderror(self):
        return self.pv_record_map.powerpiderror
    
    
    @property
    def phasepidset(self):
        return self.pv_record_map.phasepidset
    
    @phasepidset.setter
    def phasepidset(self, value):
        self.pv_record_map.phasepidset = value
    
    
    @property
    def phasepidstatus(self):
        return self.pv_record_map.phasepidstatus
    
    
    @property
    def phasepiderror(self):
        return self.pv_record_map.phasepiderror
    
    
    @property
    def timeremaining(self):
        return self.pv_record_map.timeremaining
    
    
    @property
    def modvoltset(self):
        return self.pv_record_map.modvoltset
    
    
    @property
    def modvoltread(self):
        return self.pv_record_map.modvoltread
    
    
    @property
    def powermwset(self):
        return self.pv_record_map.powermwset
    
    @powermwset.setter
    def powermwset(self, value):
        self.pv_record_map.powermwset = value
    
    
    @property
    def phaseset(self):
        return self.pv_record_map.phaseset
    
    @phaseset.setter
    def phaseset(self, value):
        self.pv_record_map.phaseset = value
    
    
    @property
    def powermwmax(self):
        return self.pv_record_map.powermwmax
    
    
    @property
    def powermwread(self):
        return self.pv_record_map.powermwread
    
    
    @property
    def phaseread(self):
        return self.pv_record_map.phaseread
    
    
    @property
    def crestphaseset(self):
        return self.pv_record_map.crestphaseset
    
    @crestphaseset.setter
    def crestphaseset(self, value):
        self.pv_record_map.crestphaseset = value
    
    
    @property
    def offcrestphaseset(self):
        return self.pv_record_map.offcrestphaseset
    
    @offcrestphaseset.setter
    def offcrestphaseset(self, value):
        self.pv_record_map.offcrestphaseset = value
    
    
    @property
    def offcrestphaseread(self):
        return self.pv_record_map.offcrestphaseread
    
    
    @property
    def beammomentum(self):
        return self.pv_record_map.beammomentum
    
    @beammomentum.setter
    def beammomentum(self, value):
        self.pv_record_map.beammomentum = value
    
    


class CavityProperties(Properties):
    """
    Class for defining cavity-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    api_set_max_wait_time: float
    """"""
    
    phase_tolerance: float
    """"""
    
    power_tolerance: float
    """"""
    
    position: float
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            CavityProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def api_set_max_wait_time(self):
        return self.api_set_max_wait_time
    
    @property
    def phase_tolerance(self):
        return self.phase_tolerance
    
    @property
    def power_tolerance(self):
        return self.power_tolerance
    
    @property
    def position(self):
        return self.position
    

    
    @property
    def api_max_wait_time(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.api_set_max_wait_time

    @api_max_wait_time.setter
    def api_max_wait_time(self, value: float) -> None:
        self.api_set_max_wait_time = value
    
    @property
    def phase_tolerance(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.phase_tolerance

    @phase_tolerance.setter
    def phase_tolerance(self, value: float) -> None:
        self.phase_tolerance = value
    
    @property
    def power_tolerance(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.power_tolerance

    @power_tolerance.setter
    def power_tolerance(self, value: float) -> None:
        self.power_tolerance = value
    
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
    

class Cavity(Hardware):
    """
    Middle layer class for interacting with a specific cavity object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[CavityControlsInformation]
    """Controls information pertaining to this cavity
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[CavityProperties]
    """Properties pertaining to this cavity
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            Cavity,
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
    def validate_controls_information(cls, v: Any) -> CavityControlsInformation:
        try:
            return CavityControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> CavityProperties:
        try:
            return CavityProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def setstartup(self):
        return self.controls_information.setstartup
    
    @setstartup.setter
    def setstartup(self, value):
        self.controls_information.setstartup = value
    
    
    @property
    def startupcomplete(self):
        return self.controls_information.startupcomplete
    
    
    @property
    def apienable(self):
        return self.controls_information.apienable
    
    @apienable.setter
    def apienable(self, value):
        self.controls_information.apienable = value
    
    
    @property
    def getapitrip(self):
        return self.controls_information.getapitrip
    
    
    @property
    def setapitrip(self):
        return self.controls_information.setapitrip
    
    @setapitrip.setter
    def setapitrip(self, value):
        self.controls_information.setapitrip = value
    
    
    @property
    def getstatus(self):
        return self.controls_information.getstatus
    
    
    @property
    def powerpidset(self):
        return self.controls_information.powerpidset
    
    @powerpidset.setter
    def powerpidset(self, value):
        self.controls_information.powerpidset = value
    
    
    @property
    def powerpidstatus(self):
        return self.controls_information.powerpidstatus
    
    
    @property
    def powerpiderror(self):
        return self.controls_information.powerpiderror
    
    
    @property
    def phasepidset(self):
        return self.controls_information.phasepidset
    
    @phasepidset.setter
    def phasepidset(self, value):
        self.controls_information.phasepidset = value
    
    
    @property
    def phasepidstatus(self):
        return self.controls_information.phasepidstatus
    
    
    @property
    def phasepiderror(self):
        return self.controls_information.phasepiderror
    
    
    @property
    def timeremaining(self):
        return self.controls_information.timeremaining
    
    
    @property
    def modvoltset(self):
        return self.controls_information.modvoltset
    
    
    @property
    def modvoltread(self):
        return self.controls_information.modvoltread
    
    
    @property
    def powermwset(self):
        return self.controls_information.powermwset
    
    @powermwset.setter
    def powermwset(self, value):
        self.controls_information.powermwset = value
    
    
    @property
    def phaseset(self):
        return self.controls_information.phaseset
    
    @phaseset.setter
    def phaseset(self, value):
        self.controls_information.phaseset = value
    
    
    @property
    def powermwmax(self):
        return self.controls_information.powermwmax
    
    
    @property
    def powermwread(self):
        return self.controls_information.powermwread
    
    
    @property
    def phaseread(self):
        return self.controls_information.phaseread
    
    
    @property
    def crestphaseset(self):
        return self.controls_information.crestphaseset
    
    @crestphaseset.setter
    def crestphaseset(self, value):
        self.controls_information.crestphaseset = value
    
    
    @property
    def offcrestphaseset(self):
        return self.controls_information.offcrestphaseset
    
    @offcrestphaseset.setter
    def offcrestphaseset(self, value):
        self.controls_information.offcrestphaseset = value
    
    
    @property
    def offcrestphaseread(self):
        return self.controls_information.offcrestphaseread
    
    
    @property
    def beammomentum(self):
        return self.controls_information.beammomentum
    
    @beammomentum.setter
    def beammomentum(self, value):
        self.controls_information.beammomentum = value
    
    

class CavityFactory(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.cavity.Cavity` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(CavityFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Cavity,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_cavity(self, name: Union[str, List[str]] = None) -> Cavity:
        """
        Returns the cavity object for the given name(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str

        :return: Cavity object(s).
        :rtype: :class:`~CATAP.laser.components.cavity.Cavity`
        or Dict[str: :class:`~CATAP.laser.components.cavity.Cavity`]
        """
        return self.get_hardware(name)

    
    def setstartup(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'setstartup' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'SetStartup' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.setstartup)
    
    def startupcomplete(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'startupcomplete' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'StartupComplete' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.startupcomplete)
    
    def apienable(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'apienable' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'APIEnable' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.apienable)
    
    def getapitrip(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'getapitrip' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'GetAPITrip' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.getapitrip)
    
    def setapitrip(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'setapitrip' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'SetAPITrip' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.setapitrip)
    
    def getstatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'getstatus' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'GetStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.getstatus)
    
    def powerpidset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'powerpidset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PowerPIDSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powerpidset)
    
    def powerpidstatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'powerpidstatus' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PowerPIDStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powerpidstatus)
    
    def powerpiderror(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'powerpiderror' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PowerPIDError' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powerpiderror)
    
    def phasepidset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'phasepidset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PhasePIDSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phasepidset)
    
    def phasepidstatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'phasepidstatus' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PhasePIDStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phasepidstatus)
    
    def phasepiderror(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'phasepiderror' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PhasePIDError' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phasepiderror)
    
    def timeremaining(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'timeremaining' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'TimeRemaining' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.timeremaining)
    
    def modvoltset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'modvoltset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'ModVoltSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.modvoltset)
    
    def modvoltread(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'modvoltread' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'ModVoltRead' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.modvoltread)
    
    def powermwset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'powermwset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PowerMWSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powermwset)
    
    def phaseset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'phaseset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PhaseSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phaseset)
    
    def powermwmax(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'powermwmax' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PowerMWMax' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powermwmax)
    
    def powermwread(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'powermwread' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PowerMWRead' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powermwread)
    
    def phaseread(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'phaseread' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'PhaseRead' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phaseread)
    
    def crestphaseset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'crestphaseset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'CrestPhaseSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.crestphaseset)
    
    def offcrestphaseset(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'offcrestphaseset' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'OffCrestPhaseSet' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.offcrestphaseset)
    
    def offcrestphaseread(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'offcrestphaseread' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'OffCrestPhaseRead' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.offcrestphaseread)
    
    def beammomentum(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'beammomentum' property of the cavity(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the 'BeamMomentum' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.beammomentum)
    