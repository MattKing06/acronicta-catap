import os
import enum
from caproto.server import pvproperty, PVGroup, run
from caproto import ChannelType

# Set the EPICS Channel Access server port
os.environ["EPICS_CA_SERVER_PORT"] = "6000"


class StatusEnum(enum.Enum):
    """
    Enum representing acquisition status.
    """

    STOP = 0
    START = 1


class BPMv1(PVGroup):
    """
    First version of a Beam Position Monitor (BPM) IOC.
    Provides scalar readback values for X and Y positions.
    """

    x_pv = pvproperty(
        name=":X_RB",
        value=0.0,
        dtype=ChannelType.FLOAT,
        doc="X position readback (scalar)",
    )

    y_pv = pvproperty(
        name=":Y_VAL",
        value=0.0,
        dtype=ChannelType.FLOAT,
        doc="Y position value (scalar)",
    )


class BPMv2(PVGroup):
    """
    Second version of a Beam Position Monitor (BPM) IOC.
    Includes scalar readbacks, a boolean acquisition status,
    and an enum control for acquisition.
    """

    x_pv = pvproperty(
        name=":X_RBV",
        value=0.0,
        dtype=ChannelType.FLOAT,
        doc="X position readback value",
    )

    y_pv = pvproperty(
        name=":Y_READBACK",
        value=0.0,
        dtype=ChannelType.FLOAT,
        doc="Y position readback value",
    )

    acquisition_status_pv = pvproperty(
        name=":ACQUIRE_RBV",
        value=False,
        dtype=ChannelType.INT,
        doc="Boolean readback for acquisition status",
    )

    set_acquire_pv = pvproperty(
        name=":ACQUIRE",
        value=StatusEnum.STOP.value,
        dtype=ChannelType.ENUM,
        enum_strings=[e.name for e in StatusEnum],
        doc="Enum control for acquisition (STOP/START)",
    )

    @set_acquire_pv.putter
    async def set_acquire_pv(self, instance, value):
        """
        Handle 'put' operations for the enum PV.
        """
        if (
            value not in StatusEnum._value2member_map_
            and value not in StatusEnum._member_names_
        ):
            print(
                f"Invalid value: {value}. ",
                f"Must be one of {[e.value for e in StatusEnum]}."
            )
            return
        else:
            ioc = instance.group
            print(f"Acquisition set to: {StatusEnum[value].name}")
            # Update the enum PV value
            await ioc.acquisition_status_pv.write(value)


def main():
    """
    Main function to instantiate and run two IOC groups under a shared CA server.
    """
    # Create two IOC instances with distinct prefixes
    ioc1 = BPMv1(prefix="VM-BPM-01")
    ioc2 = BPMv2(prefix="VM-BPM-02")

    # Combine their PV databases
    combined_pvdb = {**ioc1.pvdb, **ioc2.pvdb}

    # Run the combined IOC
    run(combined_pvdb)


if __name__ == "__main__":
    main()
