from catapcore.common.machine.pv_utils import StatisticalPV
from hardware.cavity import CavityFactory
import time
import os

# x = StatisticalPV(
#     name="VM-CAV:01:PHASE_READBACK", protocol="PVA", auto_buffer=True, buffer_size=100
# )
# while not x.is_buffer_full:
#     time.sleep(1.0)


# Set EPICS CA server port
os.environ["EPICS_PVA_NAME_SERVERS"] = "localhost:7000"

# Instantiate the factory
cavities = CavityFactory()

# Get current amplitude and phase readings
amplitudes = cavities.amplitude_readback()
phases = cavities.phase_readback()

# Print readings for each cavity
for name in cavities.names:
    print(f"{name} Amplitude: {amplitudes.get(name, None)}")
    print(f"{name} Phase: {phases.get(name, None)}")

# Access statistics for a specific cavity
cavity = cavities.get_cavity("CAV-01")
amp_stats = cavity.get_statistics("AMPLITUDE_READBACK")

if not cavity.status == "OK":
    cavity.status = "OK"
# Check buffer status and clear if full)
print("Full Buffer?:", amp_stats.is_buffer_full)
while not amp_stats.is_buffer_full:
    time.sleep(1.0)
    print(
        f"Waiting for {cavity.name} amplitude buffer to fill "
        f"({len(amp_stats.buffer)}/{amp_stats.buffer_size})",
        end="\r",
    )
if amp_stats.is_buffer_full:
    amp_stats.buffer_size = 25
    amp_stats.clear_buffer()
    print(f"Buffer cleared: ({len(amp_stats.buffer)}/{amp_stats.buffer_size})")

# Wait for buffer to fill
while not amp_stats.is_buffer_full:
    print(
        f"Waiting for {cavity.name} amplitude buffer to fill "
        f"({len(amp_stats.buffer)}/{amp_stats.buffer_size})",
        end="\r",
    )
    time.sleep(1.0)

# Print statistics
print(
    f"\nFilled buffer for {cavity.name} AMPLITUDE ({len(amp_stats.buffer)}/{amp_stats.buffer_size})"
)
print("Amplitude Mean:", amp_stats.mean)
print("Amplitude Std Dev:", amp_stats.stdev)
print("Amplitude Min:", amp_stats.min)
print("Amplitude Max:", amp_stats.max)
