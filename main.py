from clp_manager import CLPClient
from gui_manager import AppGUI
from db import insert_dados

PLC_IP = '192.168.1.20'   # exemplo
RACK = 0                 # geralmente 0 para S7-1200
SLOT = 1                 # geralmente 1 para S7-1200

def main():
    clp = CLPClient(PLC_IP,RACK,SLOT)  # IP do S7-1200
    result = clp.connect()
    if result:
        print(f"Conectado ao CLP[{PLC_IP}] RACK[{RACK}] SLOT[{SLOT}]")
    else:
        print(f'ERRO ao Conectar CLP [{PLC_IP}]')

    app = AppGUI(clp)
    app.mainloop()

    clp.disconnect()

if __name__ == "__main__":
    main()
