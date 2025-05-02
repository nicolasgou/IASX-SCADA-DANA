import snap7
from snap7.util import get_real, get_bool, get_int

class CLPClient:
    def __init__(self, ip, rack, slot):
        self.client = snap7.client.Client()
        self.ip = ip
        self.rack = rack
        self.slot = slot

    def connect(self):
        try:
            self.client.connect(self.ip, self.rack, self.slot)
            if self.client.get_connected():
                return True
            else:
                return False
        except Exception as e:
            print(f"Erro: {e}")


    def read_int(self, db_number, start_byte):
        data = self.client.db_read(db_number, start_byte, 2)
        return get_int(data, 0)

    def read_real(self, db_number, start_byte):
        data = self.client.db_read(db_number, start_byte, 4)
        return get_real(data, 0)
    
    def read_bool(self, db_number, start_byte, bit_number):
        data = self.client.db_read(db_number, start_byte, 1)
        return get_bool(data, 0, bit_number)


    def disconnect(self):
        self.client.disconnect()

    def is_connected(self):
        return self.client.get_connected()
