import re
import json
import os
import time
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.parse_savefile import ParseSavefile

class MonitorCoordinates:
    def __init__(self, save_file=""):
        self.save_file  = save_file
        self.content    = ""

        self.mappings = {
            "dZj": "VoxelX",
            "IyE": "VoxelY",
            "uXE": "VoxelZ",
            "vby": "SolarSystemIndex",
            "jsv": "PlanetIndex"
        }

    def execute(self):
        print("MODE: Monitor Coordinates")
        print(f"Processing save file: {self.save_file}")

        initial_timestamp = os.path.getmtime(self.save_file)

        self.display_coordinates()

        current_timestamp = os.path.getmtime(self.save_file)

        while True:
            current_timestamp = os.path.getmtime(self.save_file)
            if current_timestamp != initial_timestamp:
                self.display_coordinates()
                initial_timestamp = current_timestamp

            time.sleep(1)

    def display_coordinates(self):
        cmd = ParseSavefile(self.save_file)
        cmd.execute()

        data = cmd.data

        player_state = data["6f="]

        coordinates = player_state["yhJ"]["oZw"]

        voxel_x             = coordinates["dZj"]
        voxel_y             = coordinates["IyE"]
        voxel_z             = coordinates["uXE"]
        solar_system_index  = coordinates["vby"]
        planet_index        = coordinates["jsv"]

        summary = player_state["n:R"]

        print(f"Summary: {summary}")
        print(f"(x, y, z): ({voxel_x}, {voxel_y}, {voxel_z})")
        print(f"Solar System Index: {solar_system_index}")
        print(f"Planet Index: {planet_index}")
