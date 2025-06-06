from models.camera import (CameraPVMapModel,
                    CameraControlsInformationModel,
                    CameraPropertiesModel,
                    CameraModel,
                    CameraFactoryModel,
                    )

class CameraPVMap(CameraPVMapModel):

    """
    Camera PV Map.
    This defines the PVs used by the Camera component.

    Users should add any facility specific logic to this class.
    It inherits from the CameraPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(CameraPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class CameraControlsInformation(CameraControlsInformationModel):

    """
    Camera Controls Information.
    This contains the PVs and properties for the Camera component.


    Users should add any facility specific logic to this class.
    It inherits from the CameraControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(CameraControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class CameraProperties(CameraPropertiesModel):

    """
    Camera Properties.
    This defines the properties of the Camera component.

    Users should add any facility specific logic to this class.
    It inherits from the CameraPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(CameraProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class Camera(CameraModel):

    """
    Camera.
    This represents the Camera component in the hardware layer.
    It provides access to the PVs and properties defined in the
    CameraControlsInformation and CameraProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the CameraModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(Camera, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class CameraFactory(CameraFactoryModel):

    """
    Camera Factory.
    This is responsible for creating instances of the Camera component.

    Users should add any facility specific logic to this class.
    It inherits from the CameraFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(CameraFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model