from models.quadrupole import (QuadrupolePVMapModel,
                    QuadrupoleControlsInformationModel,
                    QuadrupolePropertiesModel,
                    QuadrupoleModel,
                    QuadrupoleFactoryModel,
                    )

class QuadrupolePVMap(QuadrupolePVMapModel):

    """
    Quadrupole PV Map.
    This defines the PVs used by the Quadrupole component.

    Users should add any facility specific logic to this class.
    It inherits from the QuadrupolePVMapModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(QuadrupolePVMap, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class QuadrupoleControlsInformation(QuadrupoleControlsInformationModel):

    """
    Quadrupole Controls Information.
    This contains the PVs and properties for the Quadrupole component.


    Users should add any facility specific logic to this class.
    It inherits from the QuadrupoleControlsInformationModel to provide a structure.
    """
    def __init__(self, *args, **kwargs):
        super(QuadrupoleControlsInformation, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model


class QuadrupoleProperties(QuadrupolePropertiesModel):

    """
    Quadrupole Properties.
    This defines the properties of the Quadrupole component.

    Users should add any facility specific logic to this class.
    It inherits from the QuadrupolePropertiesModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(QuadrupoleProperties, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class Quadrupole(QuadrupoleModel):

    """
    Quadrupole.
    This represents the Quadrupole component in the hardware layer.
    It provides access to the PVs and properties defined in the
    QuadrupoleControlsInformation and QuadrupoleProperties models.

    Users should add any facility specific logic to this class.
    It inherits from the QuadrupoleModel to provide a structure.

    """
    def __init__(self, *args, **kwargs):
        super(Quadrupole, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model

class QuadrupoleFactory(QuadrupoleFactoryModel):

    """
    Quadrupole Factory.
    This is responsible for creating instances of the Quadrupole component.

    Users should add any facility specific logic to this class.
    It inherits from the QuadrupoleFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(QuadrupoleFactory, self).__init__(*args, **kwargs)
        # Initialize any additional properties or methods specific to this model