import os
import threading
import time
import sys

# Caproto (Channel Access) imports
from caproto.server import pvproperty, PVGroup, run

# P4P (PVAccess) imports
from p4p.server import Server, ServerOperation
from p4p.server.thread import SharedPV
from p4p.nt import NTScalar

# ------------------------------------------------------------------------------
# Environment Configuration
# ------------------------------------------------------------------------------

# Set distinct ports for Channel Access and PVAccess servers
os.environ["EPICS_CA_SERVER_PORT"] = "6000"
os.environ["EPICS_PVA_SERVER_PORT"] = "7000"

# ------------------------------------------------------------------------------
# Channel Access IOC (Caproto)
# ------------------------------------------------------------------------------


class CAIOC(PVGroup):
    """
    Channel Access IOC hosting cavity temperature and pressure PVs.
    """

    cavity_temperature = pvproperty(
        name=":CAVITY_TEMP", value=25.0, doc="Cavity temperature in Celsius"
    )

    cavity_pressure = pvproperty(
        name=":CAVITY_PRESSURE", value=1.0, doc="Cavity pressure in Bar"
    )


def run_ca_ioc():
    """
    Starts the Channel Access IOC with prefix 'CA'.
    """
    ioc = CAIOC(prefix="VM-H20-PID-01")
    run(ioc.pvdb)


# ------------------------------------------------------------------------------
# PVAccess IOC (P4P)
# ------------------------------------------------------------------------------


class PVAHandler:
    """
    Handler for PVAccess 'put' operations.
    Posts the new value and marks the operation as complete.
    """

    def put(self, pv, op: ServerOperation):
        pv.post(op.value())
        op.done()


def run_pva_ioc(stop_event):
    """
    Starts the PVAccess IOC with two scalar PVs for PID control.
    Runs until stop_event is set.
    """
    pid_setpoint = SharedPV(
        nt=NTScalar("d"),
        initial=24.5,
        handler=PVAHandler(),
    )
    pid_readback = SharedPV(
        nt=NTScalar("d"),
        initial=24.7,
        handler=PVAHandler(),
    )

    pvdb = {
        "VM-H20-PID-01:PID_SETPOINT": pid_setpoint,
        "VM-H20-PID-01:PID_READBACK": pid_readback,
    }

    with Server(providers=[pvdb]):
        while not stop_event.is_set():
            time.sleep(0.5)


# ------------------------------------------------------------------------------
# Main Execution: Run both IOCs concurrently with graceful shutdown
# ------------------------------------------------------------------------------


def main():
    stop_event = threading.Event()

    # Start Channel Access IOC
    ca_thread = threading.Thread(target=run_ca_ioc, daemon=True)

    # Start PVAccess IOC with stop event
    pva_thread = threading.Thread(
        target=run_pva_ioc,
        args=(stop_event,),
        daemon=True,
    )

    ca_thread.start()
    pva_thread.start()

    print(
        "Both Channel Access and PVAccess IOCs are running. Press Ctrl+C to exit.",
    )

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down IOCs...")
        stop_event.set()
        ca_thread.join(timeout=2)
        pva_thread.join(timeout=2)
        print("IOCs stopped successfully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
