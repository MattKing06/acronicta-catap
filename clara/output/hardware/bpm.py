from models.bpm import (BPMPVMapModel,
                    BPMControlsInformationModel,
                    BPMPropertiesModel,
                    BPMModel,
                    BPMFactoryModel,
                    )

class BPMPVMap(BPMPVMapModel):

    """
    BPM PV Map.
    This defines the PVs used by the BPM component.

    Users should add any facility specific logic to this class.
    It inherits from the BPMPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(BPMPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class BPMControlsInformation(BPMControlsInformationModel):

    """
    BPM Controls Information.
    This contains the PVs and properties for the BPM component.


    Users should add any facility specific logic to this class.
    It inherits from the BPMControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(BPMControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class BPMProperties(BPMPropertiesModel):

    """
    BPM Properties.
    This defines the properties of the BPM component.

    Users should add any facility specific logic to this class.
    It inherits from the BPMPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(BPMProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class BPM(BPMModel):

    """
    BPM.
    This represents the BPM component in the hardware layer.
    It provides access to the PVs and properties defined in the
    BPMControlsInformation and BPMProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the BPMModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(BPM, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class BPMFactory(BPMFactoryModel):

    """
    BPM Factory.
    This is responsible for creating instances of the BPM component.

    Users should add any facility specific logic to this class.
    It inherits from the BPMFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(BPMFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model