from models.screen import (ScreenPVMapModel,
                    ScreenControlsInformationModel,
                    ScreenPropertiesModel,
                    ScreenModel,
                    ScreenFactoryModel,
                    )

class ScreenPVMap(ScreenPVMapModel):

    """
    Screen PV Map.
    This defines the PVs used by the Screen component.

    Users should add any facility specific logic to this class.
    It inherits from the ScreenPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(ScreenPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class ScreenControlsInformation(ScreenControlsInformationModel):

    """
    Screen Controls Information.
    This contains the PVs and properties for the Screen component.


    Users should add any facility specific logic to this class.
    It inherits from the ScreenControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(ScreenControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class ScreenProperties(ScreenPropertiesModel):

    """
    Screen Properties.
    This defines the properties of the Screen component.

    Users should add any facility specific logic to this class.
    It inherits from the ScreenPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(ScreenProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class Screen(ScreenModel):

    """
    Screen.
    This represents the Screen component in the hardware layer.
    It provides access to the PVs and properties defined in the
    ScreenControlsInformation and ScreenProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the ScreenModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class ScreenFactory(ScreenFactoryModel):

    """
    Screen Factory.
    This is responsible for creating instances of the Screen component.

    Users should add any facility specific logic to this class.
    It inherits from the ScreenFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(ScreenFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model