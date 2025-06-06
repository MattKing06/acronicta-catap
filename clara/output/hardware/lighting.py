from models.lighting import (LightingPVMapModel,
                    LightingControlsInformationModel,
                    LightingPropertiesModel,
                    LightingModel,
                    LightingFactoryModel,
                    )

class LightingPVMap(LightingPVMapModel):

    """
    Lighting PV Map.
    This defines the PVs used by the Lighting component.

    Users should add any facility specific logic to this class.
    It inherits from the LightingPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(LightingPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class LightingControlsInformation(LightingControlsInformationModel):

    """
    Lighting Controls Information.
    This contains the PVs and properties for the Lighting component.


    Users should add any facility specific logic to this class.
    It inherits from the LightingControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(LightingControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class LightingProperties(LightingPropertiesModel):

    """
    Lighting Properties.
    This defines the properties of the Lighting component.

    Users should add any facility specific logic to this class.
    It inherits from the LightingPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(LightingProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class Lighting(LightingModel):

    """
    Lighting.
    This represents the Lighting component in the hardware layer.
    It provides access to the PVs and properties defined in the
    LightingControlsInformation and LightingProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the LightingModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(Lighting, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class LightingFactory(LightingFactoryModel):

    """
    Lighting Factory.
    This is responsible for creating instances of the Lighting component.

    Users should add any facility specific logic to this class.
    It inherits from the LightingFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(LightingFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model