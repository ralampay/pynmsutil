import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.parse_savefile import ParseSavefile

class ExportJson:
    def __init__(self, save_file="", out_file=""):
        self.save_file  = save_file
        self.out_file   = out_file

    def execute(self):
        cmd = ParseSavefile(self.save_file)
        cmd.execute()

        with open(self.out_file, 'w') as out:
            out.write(cmd.json_data)
