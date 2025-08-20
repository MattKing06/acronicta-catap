import os
import time
from p4p.server import Server, ServerOperation
from p4p.server.thread import SharedPV
from p4p.nt import NTScalar, NTEnum

# Configuration dictionary for PVs
PV_CONFIG = [
    {
        "PHASE_SETPOINT": {"virtual_pv": "SIM:CAV:01:PHASE_SETPOINT", "type": "scalar"},
        "AMPLITUDE_SETPOINT": {"pv": "CAV:01:AMPLITUDE_SETPOINT", "type": "scalar"},
        "PHASE_READBACK": {"pv": "CAV:01:PHASE_READBACK", "type": "scalar"},
        "AMPLITUDE_READBACK": {"pv": "CAV:01:AMPLITUDE_READBACK"},
        "CAVITY_STATUS": {
            "pv": "CAV:01:CAVITY_STATUS",
            "type": "state",
            "states": {"OK": 0, "FAULT": 1, "OFF": 2},
        },
        "PROBE_TRACE": {"virtual_pv": "SIM:CAV:01:PROBE_TRACE", "type": "waveform"},
    },
    {
        "PHASE_SETPOINT": {"virtual_pv": "VIRT:CAV2:PHASE_SETPOINT", "type": "scalar"},
        "AMPLITUDE_SETPOINT": {"pv": "MOD:CAV2:AMPLITUDE_SETPOINT", "type": "scalar"},
        "PHASE_READBACK": {"pv": "MOD:CAV2:PHASE_READBACK", "type": "scalar"},
        "AMPLITUDE_READBACK": {"pv": "MOD:CAV2:AMPLITUDE_READBACK", "type": "scalar"},
        "CAVITY_STATUS": {
            "pv": "MOD:CAV2:STATUS",
            "type": "state",
            "states": {"OK": 0, "FAULT": 1, "OFF": 2},
        },
        "PROBE_TRACE": {"virtual_pv": "VIRT:CAV2:PROBE_TRACE", "type": "waveform"},
    },
    {
        "PHASE_SETPOINT": {
            "virtual_pv": "SIMSYS:CAV3:PHASE_SETPOINT",
            "type": "scalar",
        },
        "AMPLITUDE_SETPOINT": {"pv": "SYS:CAV3:AMPLITUDE_SETPOINT", "type": "scalar"},
        "PHASE_READBACK": {"pv": "SYS:CAV3:PHASE_READBACK", "type": "scalar"},
        "AMPLITUDE_READBACK": {"pv": "SYS:CAV3:AMPLITUDE_READBACK", "type": "scalar"},
        "CAVITY_STATUS": {
            "pv": "SYS:CAV3:STATUS",
            "type": "state",
            "states": {"OK": 0, "FAULT": 1, "OFF": 2},
        },
        "PROBE_TRACE": {"virtual_pv": "SIMSYS:CAV3:PROBE_TRACE", "type": "waveform"},
    },
    {
        "PHASE_SETPOINT": {"virtual_pv": "VCTRL:CAV4:PHASE_SETPOINT", "type": "scalar"},
        "AMPLITUDE_SETPOINT": {"pv": "CTRL:CAV4:AMPLITUDE_SETPOINT", "type": "scalar"},
        "PHASE_READBACK": {"pv": "CTRL:CAV4:PHASE_READBACK", "type": "scalar"},
        "AMPLITUDE_READBACK": {"pv": "CTRL:CAV4:PHASE_READBACK", "type": "scalar"},
        "CAVITY_STATUS": {
            "pv": "CTRL:CAV4:STATUS",
            "type": "state",
            "states": {"OK": 0, "FAULT": 1, "OFF": 2},
        },
        "PROBE_TRACE": {"virtual_pv": "VCTRL:CAV4:PROBE_TRACE", "type": "waveform"},
    },
]


class Handler:
    """
    Handler class for processing 'put' operations on PVs.
    """

    def put(self, pv: SharedPV, op: ServerOperation):
        """
        Handles 'put' operations by posting the new value to the PV.
        Adds a timestamp if one is not already present.

        Args:
            pv (SharedPV): The process variable to update.
            op (ServerOperation): The operation containing the new value.
        """
        if not op.value().raw.changed("timeStamp"):
            timestamp = time.time()
            pv.post(op.value(), timestamp=timestamp)
        else:
            pv.post(op.value())
        op.done()


def time_in_seconds_and_nanoseconds(timestamp: float):
    """
    Converts a floating-point timestamp into seconds and nanoseconds.

    Args:
        timestamp (float): The timestamp to convert.

    Returns:
        tuple: (seconds, nanoseconds)
    """
    seconds = int(timestamp)
    nanoseconds = int((timestamp % 1) * 1e9)
    return seconds, nanoseconds


def get_server_conf():
    """
    Retrieves EPICS server configuration from environment variables.

    Returns:
        dict: Configuration dictionary for the EPICS server.
    """
    return {
        "EPICS_PVAS_BROADCAST_PORT": str(os.getenv("EPICS_PVAS_BROADCAST_PORT", 6090)),
        "EPICS_PVAS_SERVER_PORT": str(os.getenv("EPICS_PVAS_SERVER_PORT", 6090)),
        "EPICS_PVA_ADDR_LIST": str(os.getenv("EPICS_PVA_ADDR_LIST", "")),
        "EPICS_PVA_AUTO_ADDR_LIST": str(os.getenv("EPICS_PVA_AUTO_ADDR_LIST", "YES")),
        "EPICS_PVA_SERVER_PORT": str(os.getenv("EPICS_PVA_SERVER_PORT", 6090)),
        "EPICS_PVA_INTF_ADDR_LIST": str(os.getenv("EPICS_PVA_INTF_ADDR_LIST", "")),
    }


def create_pv(cfg: dict):
    """
    Creates a SharedPV object based on the configuration.

    Args:
        name (str): The name of the PV.
        cfg (dict): Configuration dictionary for the PV.

    Returns:
        SharedPV: The created process variable.
    """
    pv_type = cfg.get("type", "scalar")
    seconds, nanoseconds = time_in_seconds_and_nanoseconds(time.time())

    if pv_type == "scalar":
        nt = NTScalar("d")
        initial = 0.0
        return SharedPV(nt=nt, initial=initial, handler=Handler())

    elif pv_type == "waveform":
        nt = NTScalar("ad", display=True)
        initial = []
        return SharedPV(nt=nt, initial=initial, handler=Handler())

    elif pv_type == "state":
        initial = NTEnum.buildType()()
        initial.value.index = 0
        initial.value.choices = list(cfg["states"].keys())
        initial.timeStamp = {
            "secondsPastEpoch": seconds,
            "nanoseconds": nanoseconds,
            "userTag": 0,
        }
        return SharedPV(handler=Handler(), initial=initial)

    return None


def main():
    # Create PV objects
    pv_objects = {}
    for entry in PV_CONFIG:
        for _, cfg in entry.items():
            name = (
                cfg.get("virtual_pv")
                if "virtual_pv" in cfg
                else f"VM-{cfg.get('pv', '')}"
            )
            if name is None:
                continue
            pv = create_pv(cfg)
            if pv:
                pv_objects[name] = pv

    # Start the EPICS server
    conf = get_server_conf()
    print(f"Starting server with configuration: {conf}")
    with Server(providers=[pv_objects], conf=conf) as server:
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Server stopped by user.")
            server.stop()


if __name__ == "__main__":
    main()
