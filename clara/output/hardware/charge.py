from models.charge import (ChargePVMapModel,
                    ChargeControlsInformationModel,
                    ChargePropertiesModel,
                    ChargeModel,
                    ChargeFactoryModel,
                    )

class ChargePVMap(ChargePVMapModel):

    """
    Charge PV Map.
    This defines the PVs used by the Charge component.

    Users should add any facility specific logic to this class.
    It inherits from the ChargePVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(ChargePVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class ChargeControlsInformation(ChargeControlsInformationModel):

    """
    Charge Controls Information.
    This contains the PVs and properties for the Charge component.


    Users should add any facility specific logic to this class.
    It inherits from the ChargeControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(ChargeControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class ChargeProperties(ChargePropertiesModel):

    """
    Charge Properties.
    This defines the properties of the Charge component.

    Users should add any facility specific logic to this class.
    It inherits from the ChargePropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(ChargeProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class Charge(ChargeModel):

    """
    Charge.
    This represents the Charge component in the hardware layer.
    It provides access to the PVs and properties defined in the
    ChargeControlsInformation and ChargeProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the ChargeModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(Charge, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class ChargeFactory(ChargeFactoryModel):

    """
    Charge Factory.
    This is responsible for creating instances of the Charge component.

    Users should add any facility specific logic to this class.
    It inherits from the ChargeFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(ChargeFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model