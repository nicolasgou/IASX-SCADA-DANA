import snap7
from snap7.util import get_real, get_bool
from snap7.snap7exceptions import Snap7Exception
import time

class CLPClient:
    def __init__(self, ip, rack=0, slot=1):
        self.ip = ip
        self.rack = rack
        self.slot = slot
        self.client = snap7.client.Client()
        self.connected = False

    def connect(self):
        try:
            self.client.connect(self.ip, self.rack, self.slot)
            self.connected = self.client.get_connected()
            print("[CLP] Conectado com sucesso.")
        except Snap7Exception as e:
            print(f"[CLP] Erro ao conectar: {e}")
            self.connected = False

    def reconnect_if_needed(self):
        if not self.client.get_connected():
            print("[CLP] Tentando reconectar...")
            try:
                self.client.disconnect()
            except:
                pass
            time.sleep(1)
            self.connect()

    def read_real(self, db_number, start_byte):
        try:
            data = self.client.db_read(db_number, start_byte, 4)
            return get_real(data, 0)
        except Snap7Exception as e:
            print(f"[CLP] Erro ao ler REAL DB{db_number}:{start_byte} → {e}")
            self.reconnect_if_needed()
            return None  # retorna None se erro

    def read_bool(self, db_number, start_byte, bit_number):
        try:
            data = self.client.db_read(db_number, start_byte, 1)
            return get_bool(data, 0, bit_number)
        except Snap7Exception as e:
            print(f"[CLP] Erro ao ler BOOL DB{db_number}:{start_byte}.{bit_number} → {e}")
            self.reconnect_if_needed()
            return None

    def disconnect(self):
        try:
            self.client.disconnect()
        except:
            pass

    def is_connected(self):
        return self.client.get_connected()
