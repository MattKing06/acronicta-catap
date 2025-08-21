from hardware.bpm import BPMFactory
import time
import os

os.environ["EPICS_CA_SERVER_PORT"] = "6000"

bpms = BPMFactory()

# Get current values for X/Y PVs
# All PVs, Acquiring, and Calibrations are handled already!
x_readings = bpms.x()
y_readings = bpms.y()
for name in bpms.names:
    print(f"{name} X: {x_readings.get(name, None)}")
    print(f"{name} Y: {y_readings.get(name, None)}")
# Access X statistics
bpm = bpms.get_bpm("BPM-01")
x_stats = bpm.get_statistics("X")
# Check buffer and clear ready for new data points
print("Full Buffer?: ", x_stats.is_buffer_full)
if x_stats.is_buffer_full:
    x_stats.buffer_size = 100
    x_stats.clear_buffer()
while not x_stats.is_buffer_full:
    print(
        f"waiting for {bpm.name} x buffer to fill ({len(x_stats.buffer)}/{x_stats.buffer_size})",
        end="\r",
    )
    time.sleep(0.1)
# Print out common statistics for x position
print(f"Filled buffer for {bpm.name} X ({len(x_stats.buffer)}/{x_stats.buffer_size})")
print("X Mean: ", x_stats.mean)
print("X Standard Deviation: ", x_stats.stdev)
print("X Min: ", x_stats.min)
print("X Max: ", x_stats.max)
