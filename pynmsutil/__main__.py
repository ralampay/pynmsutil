import sys
import argparse
import os
import os.path
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

mode_choices = [
    "monitor-coordinates"
]

def main():
    parser = argparse.ArgumentParser(description="PyNMSUtil: A command line utility in python for No Man's Sky")

    parser.add_argument("--mode", help="Mode to be used", choices=mode_choices, type=str, required=True)
    parser.add_argument("--save-file", help="Location of save file", type=str)

    args = parser.parse_args()

    mode        = args.mode
    save_file   = args.save_file

    if mode == "monitor-coordinates":
        cmd = MonitorCoordinates(save_file=save_file)

        cmd.execute()
