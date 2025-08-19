from models.bpm import (BPMPVMapModel,
                    BPMControlsInformationModel,
                    BPMPropertiesModel,
                    BPMModel,
                    BPMFactoryModel,
                    )
from pydantic import field_validator
from typing import Any

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

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> BPMPVMap:
        """ Validate the PV Map Dictionary and Convert to PV Types """
        return BPMPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )


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

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> BPMControlsInformation:
        """ Validate the Controls Information Dictionary and Convert to BPMControlsInformation Type """
        try:
            return BPMControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> BPMProperties:
        """ Validate the Properties Dictionary and Convert to BPMProperties Type """
        try:
            return BPMProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")


class BPMFactory(BPMFactoryModel):

    """
    BPM Factory.
    This is responsible for creating instances of the BPM component.

    Users should add any facility specific logic to this class.
    It inherits from the BPMFactoryModel to provide a structure.
    """

    def __init__(self, *args, **kwargs):
        super(BPMFactory, self).__init__(
            hardware_type=BPM,
            *args,
            **kwargs,
        )
        # Initialize any additional properties or methods specific to this model