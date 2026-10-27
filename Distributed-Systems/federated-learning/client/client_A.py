import os

from client import main

os.environ.setdefault("GROUP_ID", "Group_A")
os.environ.setdefault("DATA_PATH", "data/Group_A/train.csv")

if __name__ == "__main__":
    main()
