import json
import struct
import lz4.block as lb

class ParseSavefile:
    def __init__(self, save_file):
        self.save_file = save_file

    def execute(self):
        with open(self.save_file, 'rb') as src:
            dest = b''
            while src.read(4) == b'\xE5\xA1\xED\xFE':
                block_size = struct.unpack('i', src.read(4))[0]
                dest_size = struct.unpack('i', src.read(4))[0]
                src.read(4)
                dest += lb.decompress(src.read(block_size), uncompressed_size=dest_size)

            if src.read(1):
                src.seek(0)
                dest = src.read().rstrip(b'\x00')
            else:
                dest = dest.rstrip(b'\x00')

            self.data       = json.loads(dest.decode('utf-8'))
            self.json_data  = json.dumps(self.data, indent=2)
