#!/usr/bin/env python3
"""Generate small SYNTHETIC demo partitions (image_id,label) for the FL tutorial.

No third-party data is used. client.py only needs a 'label' column.
Usage:  python data/make_demo_data.py   (run from federated-learning/)
"""
import csv
import random
from pathlib import Path

NUM_CLASSES = 5
ROWS_PER_GROUP = 800
GROUPS = ["Group_A", "Group_B", "Group_C"]


def main(seed: int = 42) -> None:
    rng = random.Random(seed)
    root = Path(__file__).resolve().parent
    all_rows = []
    for gi, group in enumerate(GROUPS):
        # Mildly different class priors per group (non-IID), all classes present.
        weights = [1.0] * NUM_CLASSES
        weights[gi % NUM_CLASSES] = 3.0
        rows = [
            (f"synthetic_{group}_{i:05d}.jpg", rng.choices(range(NUM_CLASSES), weights)[0])
            for i in range(ROWS_PER_GROUP)
        ]
        out = root / group
        out.mkdir(exist_ok=True)
        with open(out / "train.csv", "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["image_id", "label"])
            writer.writerows(rows)
        all_rows += rows
    with open(root / "train.csv", "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["image_id", "label"])
        writer.writerows(all_rows)
    print(f"Wrote {len(GROUPS)} partitions x {ROWS_PER_GROUP} rows + combined train.csv")


if __name__ == "__main__":
    main()
