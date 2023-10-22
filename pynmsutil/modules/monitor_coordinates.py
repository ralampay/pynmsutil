import re
import json

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
        self.set_content()
        #print(self.content)

        pattern = r'\{"dZj":-?\d+\,"IyE":-?\d+,"uXE":-?\d+,"vby":-?\d+,"jsv":-?\d+}'

        matches = re.findall(pattern, self.content)

        if len(matches) > 0:
            data = json.loads(matches[0])

            for key, val in data.items():
                print(f"{self.mappings[key]}: {val}", end=" ")
            print("")
                
        else:
            print("No coordinates found")

    def set_content(self):
        self.content = ""
        
        try:
            with open(self.save_file, "rb") as binary_file:
                while True:
                    byte = binary_file.read(1)

                    if not byte:
                        break

                    try:
                        char = byte.decode("ascii")

                        if char.isprintable():
                            self.content += char
                        else:
                            self.content += "."
                    except UnicodeDecodeError:
                        self.content += "."
        except FileNotFoundError:
            print(f"Save file {self.save_file} not found.")
        except Exception as e:
            print(f"Exception occured: {e}")
