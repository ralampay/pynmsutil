import sys
import argparse
import os
import os.path
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from modules.monitor_coordinates import MonitorCoordinates
from modules.export_json import ExportJson

mode_choices = [
    "monitor-coordinates",
    "export-json"
]

def main():
    parser = argparse.ArgumentParser(description="PyNMSUtil: A command line utility in python for No Man's Sky")

    parser.add_argument("--mode", help="Mode to be used", choices=mode_choices, type=str, required=True)
    parser.add_argument("--save-file", help="Location of save file", type=str)
    parser.add_argument("--out-file", help="Output file", type=str)

    args = parser.parse_args()

    mode        = args.mode
    save_file   = args.save_file
    out_file    = args.out_file

    if mode == "monitor-coordinates":
        cmd = MonitorCoordinates(save_file=save_file)

        cmd.execute()
    elif mode == "export-json":
        cmd = ExportJson(save_file=save_file, out_file=out_file)

        cmd.execute()

if __name__ == '__main__':
    main()
