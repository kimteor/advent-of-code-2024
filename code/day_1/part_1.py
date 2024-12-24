from pathlib import Path
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]


file_path = PROJECT_ROOT / "data" / "input" / "day1" / "input.txt"
content = file_path.read_text()
lines = content.split("\n")
left_locations = []
right_locations = []
for line in lines:
    left, right = line.split("   ")
    left_locations.append(int(left))
    right_locations.append(int(right))

left_locations = np.array(left_locations)
right_locations = np.array(right_locations)

assert left_locations.shape == right_locations.shape, "Shape mismatch"

left_locations = np.sort(left_locations)
right_locations = np.sort(right_locations)
distance = np.abs(left_locations - right_locations)
answer = distance.sum()
print(answer)
