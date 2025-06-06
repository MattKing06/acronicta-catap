from models.rfheartbeat import (RFHeartbeatPVMapModel,
                    RFHeartbeatControlsInformationModel,
                    RFHeartbeatPropertiesModel,
                    RFHeartbeatModel,
                    RFHeartbeatFactoryModel,
                    )

class RFHeartbeatPVMap(RFHeartbeatPVMapModel):

    """
    RFHeartbeat PV Map.
    This defines the PVs used by the RFHeartbeat component.

    Users should add any facility specific logic to this class.
    It inherits from the RFHeartbeatPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(RFHeartbeatPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class RFHeartbeatControlsInformation(RFHeartbeatControlsInformationModel):

    """
    RFHeartbeat Controls Information.
    This contains the PVs and properties for the RFHeartbeat component.


    Users should add any facility specific logic to this class.
    It inherits from the RFHeartbeatControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(RFHeartbeatControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class RFHeartbeatProperties(RFHeartbeatPropertiesModel):

    """
    RFHeartbeat Properties.
    This defines the properties of the RFHeartbeat component.

    Users should add any facility specific logic to this class.
    It inherits from the RFHeartbeatPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(RFHeartbeatProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class RFHeartbeat(RFHeartbeatModel):

    """
    RFHeartbeat.
    This represents the RFHeartbeat component in the hardware layer.
    It provides access to the PVs and properties defined in the
    RFHeartbeatControlsInformation and RFHeartbeatProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the RFHeartbeatModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(RFHeartbeat, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class RFHeartbeatFactory(RFHeartbeatFactoryModel):

    """
    RFHeartbeat Factory.
    This is responsible for creating instances of the RFHeartbeat component.

    Users should add any facility specific logic to this class.
    It inherits from the RFHeartbeatFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(RFHeartbeatFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model