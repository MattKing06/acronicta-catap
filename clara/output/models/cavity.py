
from catapcore.common.machine.pv_utils import BinaryPV, StatePV, ScalarPV, StatisticalPV
from catapcore.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from catapcore.common.machine.factory import Factory
from catapcore.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class CavityPVMapModel(PVMap):
    
    
    SetStartup: BinaryPV
    
    """Startup RF"""
    
    
    StartupComplete: BinaryPV
    
    """Check API setup status"""
    
    
    APIEnable: BinaryPV
    
    """Enable RF API"""
    
    
    GetAPITrip: StatePV
    
    """Get API trip status"""
    
    
    SetAPITrip: BinaryPV
    
    """Reset API trips"""
    
    
    GetStatus: StatePV
    
    """Get API status"""
    
    
    PowerPIDSet: BinaryPV
    
    """Set power PID on"""
    
    
    PowerPIDStatus: StatePV
    
    """Get power PID status"""
    
    
    PowerPIDError: BinaryPV
    
    """Check if power PID within tolerance"""
    
    
    PhasePIDSet: BinaryPV
    
    """Set phase PID on"""
    
    
    PhasePIDStatus: StatePV
    
    """Get phase PID status"""
    
    
    PhasePIDError: BinaryPV
    
    """Check if phase PID within tolerance"""
    
    
    PowerMWMax: ScalarPV
    
    """Maximum set cavity forward power"""
    
    
    PowerMWSet: ScalarPV
    
    """Set cavity forward power"""
    
    
    PhaseSet: ScalarPV
    
    """Set cavity phase"""
    
    
    PowerMWRead: StatisticalPV
    
    """Read cavity forward power"""
    
    
    PhaseRead: StatisticalPV
    
    """Read cavity phase"""
    
    
    CrestPhaseSet: ScalarPV
    
    """Set crest phase"""
    
    
    OffCrestPhaseSet: ScalarPV
    
    """Set cavity off-crest phase"""
    
    
    OffCrestPhaseRead: StatisticalPV
    
    """Set cavity off-crest phase"""
    
    
    BeamMomentum: ScalarPV
    
    """Beam momentum at the exit of the cavity, used in k-value calculations for all magnets in that section."""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        CavityPVMapModel.is_virtual = is_virtual
        CavityPVMapModel.connect_on_creation = connect_on_creation
        super(
            CavityPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def setstartup(self):
        """Default Getter implementation for SetStartup"""
        
        return self.SetStartup.get()
        

    
    @setstartup.setter
    def setstartup(self, value):
        """Default Setter implementation for SetStartup"""
        
        return self.SetStartup.put(value)
        
    
    
    @property
    def startupcomplete(self):
        """Default Getter implementation for StartupComplete"""
        
        return self.StartupComplete.get()
        

    
    
    @property
    def apienable(self):
        """Default Getter implementation for APIEnable"""
        
        return self.APIEnable.get()
        

    
    @apienable.setter
    def apienable(self, value):
        """Default Setter implementation for APIEnable"""
        
        return self.APIEnable.put(value)
        
    
    
    @property
    def getapitrip(self):
        """Default Getter implementation for GetAPITrip"""
        
        return self.GetAPITrip.get()
        

    
    
    @property
    def setapitrip(self):
        """Default Getter implementation for SetAPITrip"""
        
        return self.SetAPITrip.get()
        

    
    @setapitrip.setter
    def setapitrip(self, value):
        """Default Setter implementation for SetAPITrip"""
        
        return self.SetAPITrip.put(value)
        
    
    
    @property
    def getstatus(self):
        """Default Getter implementation for GetStatus"""
        
        return self.GetStatus.get()
        

    
    
    @property
    def powerpidset(self):
        """Default Getter implementation for PowerPIDSet"""
        
        return self.PowerPIDSet.get()
        

    
    @powerpidset.setter
    def powerpidset(self, value):
        """Default Setter implementation for PowerPIDSet"""
        
        return self.PowerPIDSet.put(value)
        
    
    
    @property
    def powerpidstatus(self):
        """Default Getter implementation for PowerPIDStatus"""
        
        return self.PowerPIDStatus.get()
        

    
    
    @property
    def powerpiderror(self):
        """Default Getter implementation for PowerPIDError"""
        
        return self.PowerPIDError.get()
        

    
    
    @property
    def phasepidset(self):
        """Default Getter implementation for PhasePIDSet"""
        
        return self.PhasePIDSet.get()
        

    
    @phasepidset.setter
    def phasepidset(self, value):
        """Default Setter implementation for PhasePIDSet"""
        
        return self.PhasePIDSet.put(value)
        
    
    
    @property
    def phasepidstatus(self):
        """Default Getter implementation for PhasePIDStatus"""
        
        return self.PhasePIDStatus.get()
        

    
    
    @property
    def phasepiderror(self):
        """Default Getter implementation for PhasePIDError"""
        
        return self.PhasePIDError.get()
        

    
    
    @property
    def powermwmax(self):
        """Default Getter implementation for PowerMWMax"""
        
        return self.PowerMWMax.get()
        

    
    
    @property
    def powermwset(self):
        """Default Getter implementation for PowerMWSet"""
        
        return self.PowerMWSet.get()
        

    
    @powermwset.setter
    def powermwset(self, value):
        """Default Setter implementation for PowerMWSet"""
        
        return self.PowerMWSet.put(value)
        
    
    
    @property
    def phaseset(self):
        """Default Getter implementation for PhaseSet"""
        
        return self.PhaseSet.get()
        

    
    @phaseset.setter
    def phaseset(self, value):
        """Default Setter implementation for PhaseSet"""
        
        return self.PhaseSet.put(value)
        
    
    
    @property
    def powermwread(self):
        """Default Getter implementation for PowerMWRead"""
        
        return self.PowerMWRead.get()
        

    
    
    @property
    def phaseread(self):
        """Default Getter implementation for PhaseRead"""
        
        return self.PhaseRead.get()
        

    
    
    @property
    def crestphaseset(self):
        """Default Getter implementation for CrestPhaseSet"""
        
        return self.CrestPhaseSet.get()
        

    
    @crestphaseset.setter
    def crestphaseset(self, value):
        """Default Setter implementation for CrestPhaseSet"""
        
        return self.CrestPhaseSet.put(value)
        
    
    
    @property
    def offcrestphaseset(self):
        """Default Getter implementation for OffCrestPhaseSet"""
        
        return self.OffCrestPhaseSet.get()
        

    
    @offcrestphaseset.setter
    def offcrestphaseset(self, value):
        """Default Setter implementation for OffCrestPhaseSet"""
        
        return self.OffCrestPhaseSet.put(value)
        
    
    
    @property
    def offcrestphaseread(self):
        """Default Getter implementation for OffCrestPhaseRead"""
        
        return self.OffCrestPhaseRead.get()
        

    
    
    @property
    def beammomentum(self):
        """Default Getter implementation for BeamMomentum"""
        
        return self.BeamMomentum.get()
        

    
    @beammomentum.setter
    def beammomentum(self, value):
        """Default Setter implementation for BeamMomentum"""
        
        return self.BeamMomentum.put(value)
        
    
    



class CavityControlsInformationModel(ControlsInformation):
    """
    Class for controlling a cavity via EPICS

    Inherits from:
        :class:`~catapcore.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[CavityPVMapModel]

    

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
        CavityControlsInformationModel.is_virtual = is_virtual
        CavityControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            CavityControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> CavityPVMapModel:
        return CavityPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def setstartup(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.SetStartup`."""    
        return self.pv_record_map.setstartup
    
    @setstartup.setter
    def setstartup(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.SetStartup`.""" 
        self.pv_record_map.setstartup = value
    
    
    @property
    def startupcomplete(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.StartupComplete`."""    
        return self.pv_record_map.startupcomplete
    
    
    @property
    def apienable(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.APIEnable`."""    
        return self.pv_record_map.apienable
    
    @apienable.setter
    def apienable(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.APIEnable`.""" 
        self.pv_record_map.apienable = value
    
    
    @property
    def getapitrip(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.GetAPITrip`."""    
        return self.pv_record_map.getapitrip
    
    
    @property
    def setapitrip(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.SetAPITrip`."""    
        return self.pv_record_map.setapitrip
    
    @setapitrip.setter
    def setapitrip(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.SetAPITrip`.""" 
        self.pv_record_map.setapitrip = value
    
    
    @property
    def getstatus(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.GetStatus`."""    
        return self.pv_record_map.getstatus
    
    
    @property
    def powerpidset(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PowerPIDSet`."""    
        return self.pv_record_map.powerpidset
    
    @powerpidset.setter
    def powerpidset(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.PowerPIDSet`.""" 
        self.pv_record_map.powerpidset = value
    
    
    @property
    def powerpidstatus(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PowerPIDStatus`."""    
        return self.pv_record_map.powerpidstatus
    
    
    @property
    def powerpiderror(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PowerPIDError`."""    
        return self.pv_record_map.powerpiderror
    
    
    @property
    def phasepidset(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PhasePIDSet`."""    
        return self.pv_record_map.phasepidset
    
    @phasepidset.setter
    def phasepidset(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.PhasePIDSet`.""" 
        self.pv_record_map.phasepidset = value
    
    
    @property
    def phasepidstatus(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PhasePIDStatus`."""    
        return self.pv_record_map.phasepidstatus
    
    
    @property
    def phasepiderror(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PhasePIDError`."""    
        return self.pv_record_map.phasepiderror
    
    
    @property
    def powermwmax(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PowerMWMax`."""    
        return self.pv_record_map.powermwmax
    
    
    @property
    def powermwset(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PowerMWSet`."""    
        return self.pv_record_map.powermwset
    
    @powermwset.setter
    def powermwset(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.PowerMWSet`.""" 
        self.pv_record_map.powermwset = value
    
    
    @property
    def phaseset(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PhaseSet`."""    
        return self.pv_record_map.phaseset
    
    @phaseset.setter
    def phaseset(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.PhaseSet`.""" 
        self.pv_record_map.phaseset = value
    
    
    @property
    def powermwread(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PowerMWRead`."""    
        return self.pv_record_map.powermwread
    
    
    @property
    def phaseread(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.PhaseRead`."""    
        return self.pv_record_map.phaseread
    
    
    @property
    def crestphaseset(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.CrestPhaseSet`."""    
        return self.pv_record_map.crestphaseset
    
    @crestphaseset.setter
    def crestphaseset(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.CrestPhaseSet`.""" 
        self.pv_record_map.crestphaseset = value
    
    
    @property
    def offcrestphaseset(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.OffCrestPhaseSet`."""    
        return self.pv_record_map.offcrestphaseset
    
    @offcrestphaseset.setter
    def offcrestphaseset(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.OffCrestPhaseSet`.""" 
        self.pv_record_map.offcrestphaseset = value
    
    
    @property
    def offcrestphaseread(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.OffCrestPhaseRead`."""    
        return self.pv_record_map.offcrestphaseread
    
    
    @property
    def beammomentum(self):
        """Default Getter implementation for :attr:`CavityPVMapModel.BeamMomentum`."""    
        return self.pv_record_map.beammomentum
    
    @beammomentum.setter
    def beammomentum(self, value):
        """Default Setter implementation for :attr:`CavityPVMapModel.BeamMomentum`.""" 
        self.pv_record_map.beammomentum = value
    
    

    


class CavityPropertiesModel(Properties):
    """
    Class for defining cavity-specific properties.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Properties`
    """
    
    
    virtual_name: str
    
    
    
    type: str
    
    
    
    api_set_max_wait_time: float
    
    
    
    phase_tolerance: float
    
    
    
    power_tolerance: float
    
    

    def __init__(self, *args, **kwargs):
        super(
            CavityPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class CavityModel(Hardware):
    """
    Middle layer class for interacting with a specific cavity object.

    Inherits from:
        :class:`~catapcore.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[CavityControlsInformationModel]
    """Controls information pertaining to this cavity
    (see :class:`~catapcore.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[CavityPropertiesModel]
    """Properties pertaining to this cavity
    (see :class:`~catapcore.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            CavityModel,
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
    def validate_controls_information(cls, v: Any) -> CavityControlsInformationModel:
        try:
            return CavityControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> CavityPropertiesModel:
        try:
            return CavityPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def setstartup(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.SetStartup`."""
        return self.controls_information.setstartup
    
    @setstartup.setter
    def setstartup(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.SetStartup`."""
        self.controls_information.setstartup = value
    
    
    @property
    def startupcomplete(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.StartupComplete`."""
        return self.controls_information.startupcomplete
    
    
    @property
    def apienable(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.APIEnable`."""
        return self.controls_information.apienable
    
    @apienable.setter
    def apienable(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.APIEnable`."""
        self.controls_information.apienable = value
    
    
    @property
    def getapitrip(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.GetAPITrip`."""
        return self.controls_information.getapitrip
    
    
    @property
    def setapitrip(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.SetAPITrip`."""
        return self.controls_information.setapitrip
    
    @setapitrip.setter
    def setapitrip(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.SetAPITrip`."""
        self.controls_information.setapitrip = value
    
    
    @property
    def getstatus(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.GetStatus`."""
        return self.controls_information.getstatus
    
    
    @property
    def powerpidset(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PowerPIDSet`."""
        return self.controls_information.powerpidset
    
    @powerpidset.setter
    def powerpidset(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.PowerPIDSet`."""
        self.controls_information.powerpidset = value
    
    
    @property
    def powerpidstatus(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PowerPIDStatus`."""
        return self.controls_information.powerpidstatus
    
    
    @property
    def powerpiderror(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PowerPIDError`."""
        return self.controls_information.powerpiderror
    
    
    @property
    def phasepidset(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PhasePIDSet`."""
        return self.controls_information.phasepidset
    
    @phasepidset.setter
    def phasepidset(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.PhasePIDSet`."""
        self.controls_information.phasepidset = value
    
    
    @property
    def phasepidstatus(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PhasePIDStatus`."""
        return self.controls_information.phasepidstatus
    
    
    @property
    def phasepiderror(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PhasePIDError`."""
        return self.controls_information.phasepiderror
    
    
    @property
    def powermwmax(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PowerMWMax`."""
        return self.controls_information.powermwmax
    
    
    @property
    def powermwset(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PowerMWSet`."""
        return self.controls_information.powermwset
    
    @powermwset.setter
    def powermwset(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.PowerMWSet`."""
        self.controls_information.powermwset = value
    
    
    @property
    def phaseset(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PhaseSet`."""
        return self.controls_information.phaseset
    
    @phaseset.setter
    def phaseset(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.PhaseSet`."""
        self.controls_information.phaseset = value
    
    
    @property
    def powermwread(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PowerMWRead`."""
        return self.controls_information.powermwread
    
    
    @property
    def phaseread(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.PhaseRead`."""
        return self.controls_information.phaseread
    
    
    @property
    def crestphaseset(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.CrestPhaseSet`."""
        return self.controls_information.crestphaseset
    
    @crestphaseset.setter
    def crestphaseset(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.CrestPhaseSet`."""
        self.controls_information.crestphaseset = value
    
    
    @property
    def offcrestphaseset(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.OffCrestPhaseSet`."""
        return self.controls_information.offcrestphaseset
    
    @offcrestphaseset.setter
    def offcrestphaseset(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.OffCrestPhaseSet`."""
        self.controls_information.offcrestphaseset = value
    
    
    @property
    def offcrestphaseread(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.OffCrestPhaseRead`."""
        return self.controls_information.offcrestphaseread
    
    
    @property
    def beammomentum(self):
        """Default Getter implementation for :attr:`CavityControlsInformationModel.BeamMomentum`."""
        return self.controls_information.beammomentum
    
    @beammomentum.setter
    def beammomentum(self, value):
        """Default Setter implementation for :attr:`CavityControlsInformationModel.BeamMomentum`."""
        self.controls_information.beammomentum = value
    
    

class CavityFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`catapcore.laser.components.cavity.Cavity` objects.

    Inherits from:
        :class:`~catapcore.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(CavityFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=CavityModel,
            lattice_folder="Cavity",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_cavity(self, name: Union[str, List[str]] = None) -> CavityModel:
        """
        Returns the cavity object for the given name(s).

        :param name: Name(s) of the cavity.
        :type name: str or list of str

        :return: Cavity object(s).
        :rtype: :class:`cavityModel.Cavity`
        or Dict[str: :class:`cavity.Cavity`]
        """
        return self.get_hardware(name)

    
    def setstartup(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.SetStartup`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.SetStartup` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.setstartup)
    
    def startupcomplete(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.StartupComplete`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.StartupComplete` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.startupcomplete)
    
    def apienable(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.APIEnable`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.APIEnable` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.apienable)
    
    def getapitrip(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.GetAPITrip`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.GetAPITrip` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.getapitrip)
    
    def setapitrip(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.SetAPITrip`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.SetAPITrip` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.setapitrip)
    
    def getstatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.GetStatus`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.GetStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.getstatus)
    
    def powerpidset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PowerPIDSet`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PowerPIDSet` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powerpidset)
    
    def powerpidstatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PowerPIDStatus`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PowerPIDStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powerpidstatus)
    
    def powerpiderror(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PowerPIDError`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PowerPIDError` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powerpiderror)
    
    def phasepidset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PhasePIDSet`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PhasePIDSet` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phasepidset)
    
    def phasepidstatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PhasePIDStatus`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PhasePIDStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phasepidstatus)
    
    def phasepiderror(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PhasePIDError`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PhasePIDError` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phasepiderror)
    
    def powermwmax(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PowerMWMax`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PowerMWMax` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powermwmax)
    
    def powermwset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PowerMWSet`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PowerMWSet` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powermwset)
    
    def phaseset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PhaseSet`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PhaseSet` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phaseset)
    
    def powermwread(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PowerMWRead`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PowerMWRead` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.powermwread)
    
    def phaseread(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.PhaseRead`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.PhaseRead` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.phaseread)
    
    def crestphaseset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.CrestPhaseSet`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.CrestPhaseSet` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.crestphaseset)
    
    def offcrestphaseset(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.OffCrestPhaseSet`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.OffCrestPhaseSet` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.offcrestphaseset)
    
    def offcrestphaseread(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.OffCrestPhaseRead`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.OffCrestPhaseRead` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.offcrestphaseread)
    
    def beammomentum(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CavityModel.BeamMomentum`.

        :param name: Name(s) of the cavity.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CavityModel.BeamMomentum` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda cavity: cavity.beammomentum)
    