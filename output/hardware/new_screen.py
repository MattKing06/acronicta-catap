from models.new_screen import (New_ScreenPVMapModel,
                    New_ScreenControlsInformationModel,
                    New_ScreenPropertiesModel,
                    New_ScreenModel,
                    New_ScreenFactoryModel,
                    )

class New_ScreenPVMap(New_ScreenPVMapModel):

    """
    New_Screen PV Map.
    This defines the PVs used by the New_Screen component.

    Users should add any facility specific logic to this class.
    It inherits from the New_ScreenPVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(New_ScreenPVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class New_ScreenControlsInformation(New_ScreenControlsInformationModel):

    """
    New_Screen Controls Information.
    This contains the PVs and properties for the New_Screen component.


    Users should add any facility specific logic to this class.
    It inherits from the New_ScreenControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(New_ScreenControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class New_ScreenProperties(New_ScreenPropertiesModel):

    """
    New_Screen Properties.
    This defines the properties of the New_Screen component.

    Users should add any facility specific logic to this class.
    It inherits from the New_ScreenPropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(New_ScreenProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class New_Screen(New_ScreenModel):

    """
    New_Screen.
    This represents the New_Screen component in the hardware layer.
    It provides access to the PVs and properties defined in the
    New_ScreenControlsInformation and New_ScreenProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the New_ScreenModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(New_Screen, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class New_ScreenFactory(New_ScreenFactoryModel):

    """
    New_Screen Factory.
    This is responsible for creating instances of the New_Screen component.

    Users should add any facility specific logic to this class.
    It inherits from the New_ScreenFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(New_ScreenFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model