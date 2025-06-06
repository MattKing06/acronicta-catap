from models.energymeter import (EnergyMeterPVMapModel,
                    EnergyMeterControlsInformationModel,
                    EnergyMeterPropertiesModel,
                    EnergyMeterModel,
                    EnergyMeterFactoryModel,
                    )

class EnergyMeterPVMap(EnergyMeterPVMapModel):

    """
    EnergyMeter PV Map.
    This defines the PVs used by the EnergyMeter component.

    Users should add any facility specific logic to this class.
    It inherits from the EnergyMeterPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(EnergyMeterPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class EnergyMeterControlsInformation(EnergyMeterControlsInformationModel):

    """
    EnergyMeter Controls Information.
    This contains the PVs and properties for the EnergyMeter component.


    Users should add any facility specific logic to this class.
    It inherits from the EnergyMeterControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(EnergyMeterControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class EnergyMeterProperties(EnergyMeterPropertiesModel):

    """
    EnergyMeter Properties.
    This defines the properties of the EnergyMeter component.

    Users should add any facility specific logic to this class.
    It inherits from the EnergyMeterPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(EnergyMeterProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class EnergyMeter(EnergyMeterModel):

    """
    EnergyMeter.
    This represents the EnergyMeter component in the hardware layer.
    It provides access to the PVs and properties defined in the
    EnergyMeterControlsInformation and EnergyMeterProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the EnergyMeterModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(EnergyMeter, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class EnergyMeterFactory(EnergyMeterFactoryModel):

    """
    EnergyMeter Factory.
    This is responsible for creating instances of the EnergyMeter component.

    Users should add any facility specific logic to this class.
    It inherits from the EnergyMeterFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(EnergyMeterFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model