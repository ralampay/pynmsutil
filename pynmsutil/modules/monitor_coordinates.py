
class MonitorCoordinates:
    def __init__(self, save_file=""):
        self.save_file  = save_file
        self.content    = ""

        self.coordinates = {
            "x": -1,
            "y": -1,
            "z": -1
        }

    def execute(self):
        print("MODE: Monitor Coordinates")
        print(f"Processing save file: {self.save_file}")

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
