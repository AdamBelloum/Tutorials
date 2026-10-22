import os

from client import main

os.environ.setdefault("GROUP_ID", "Group_C")
os.environ.setdefault("DATA_PATH", "data/Group_C/train.csv")

if __name__ == "__main__":
    main()
