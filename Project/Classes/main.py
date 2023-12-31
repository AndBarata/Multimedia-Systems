from PerfectPitch import PerfectPitch

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

perfectPitch = PerfectPitch()

if __name__ == "__main__":

    # Initializes GUI
    print("Program started")
    perfectPitch.startInitialWindow()
