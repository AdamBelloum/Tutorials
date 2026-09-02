import os

from client import main

os.environ.setdefault("GROUP_ID", "Group_B")
os.environ.setdefault("DATA_PATH", "data/Group_B/train.csv")

if __name__ == "__main__":
    main()
