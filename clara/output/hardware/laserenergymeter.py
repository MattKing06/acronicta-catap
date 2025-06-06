from models.laserenergymeter import (LaserEnergyMeterPVMapModel,
                    LaserEnergyMeterControlsInformationModel,
                    LaserEnergyMeterPropertiesModel,
                    LaserEnergyMeterModel,
                    LaserEnergyMeterFactoryModel,
                    )

class LaserEnergyMeterPVMap(LaserEnergyMeterPVMapModel):

    """
    LaserEnergyMeter PV Map.
    This defines the PVs used by the LaserEnergyMeter component.

    Users should add any facility specific logic to this class.
    It inherits from the LaserEnergyMeterPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(LaserEnergyMeterPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class LaserEnergyMeterControlsInformation(LaserEnergyMeterControlsInformationModel):

    """
    LaserEnergyMeter Controls Information.
    This contains the PVs and properties for the LaserEnergyMeter component.


    Users should add any facility specific logic to this class.
    It inherits from the LaserEnergyMeterControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(LaserEnergyMeterControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class LaserEnergyMeterProperties(LaserEnergyMeterPropertiesModel):

    """
    LaserEnergyMeter Properties.
    This defines the properties of the LaserEnergyMeter component.

    Users should add any facility specific logic to this class.
    It inherits from the LaserEnergyMeterPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(LaserEnergyMeterProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class LaserEnergyMeter(LaserEnergyMeterModel):

    """
    LaserEnergyMeter.
    This represents the LaserEnergyMeter component in the hardware layer.
    It provides access to the PVs and properties defined in the
    LaserEnergyMeterControlsInformation and LaserEnergyMeterProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the LaserEnergyMeterModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(LaserEnergyMeter, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class LaserEnergyMeterFactory(LaserEnergyMeterFactoryModel):

    """
    LaserEnergyMeter Factory.
    This is responsible for creating instances of the LaserEnergyMeter component.

    Users should add any facility specific logic to this class.
    It inherits from the LaserEnergyMeterFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(LaserEnergyMeterFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model