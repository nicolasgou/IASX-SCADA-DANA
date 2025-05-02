import customtkinter as ctk
from clp_manager import CLPClient

class AppGUI(ctk.CTk):
    def __init__(self, clp_client):
        super().__init__()
        self.clp = clp_client
        self.title("Monitoramento Prensas")
        self.geometry("1920x1080")  # TV 50'' geralmente é FullHD

        # Layout
        # Prensa 1
        self.label_Title1 = ctk.CTkLabel(self, text="Prensa 1:", font=("Arial", 40))
        self.label_Title1.pack(pady=30)

        self.label_pressao1 = ctk.CTkLabel(self, text="Pressão 1:", font=("Arial", 40))
        self.label_pressao1.pack(pady=30)

        self.label_posicao1 = ctk.CTkLabel(self, text="Posição 1:", font=("Arial", 40))
        self.label_posicao1.pack(pady=30)

        self.label_status1 = ctk.CTkLabel(self, text="Status 1:", font=("Arial", 40))
        self.label_status1.pack(pady=30)
        # Prensa 2
        self.label_Title2 = ctk.CTkLabel(self, text="Prensa 2:", font=("Arial", 40))
        self.label_Title2.pack(pady=30)

        self.label_pressao2 = ctk.CTkLabel(self, text="Pressão 2:", font=("Arial", 40))
        self.label_pressao2.pack(pady=30)

        self.label_posicao2 = ctk.CTkLabel(self, text="Posição 2:", font=("Arial", 40))
        self.label_posicao2.pack(pady=30)

        self.label_status2 = ctk.CTkLabel(self, text="Status 2:", font=("Arial", 40))
        self.label_status2.pack(pady=30)
        
        # Prensa 3
        self.label_Title3 = ctk.CTkLabel(self, text="Prensa 3:", font=("Arial", 40))
        self.label_Title3.pack(pady=30)

        self.label_pressao3 = ctk.CTkLabel(self, text="Pressão 3:", font=("Arial", 40))
        self.label_pressao3.pack(pady=30)

        self.label_posicao3 = ctk.CTkLabel(self, text="Posição 3:", font=("Arial", 40))
        self.label_posicao3.pack(pady=30)

        self.label_status3 = ctk.CTkLabel(self, text="Status 3:", font=("Arial", 40))
        self.label_status3.pack(pady=30)

        # Atualizar dados
        try:
            self.update_data()
        except Exception as e:
            print(f"Erro: {e}")


    def update_data(self):
        if self.clp.is_connected():
            # pressao = self.clp.read_real(db_number=2, start_byte=0)
            # posicao = self.clp.read_real(db_number=2, start_byte=4)

            # Prensa 1
            pressao1 = self.clp.read_int(db_number=2, start_byte=0)
            self.label_pressao1.configure(text=f"Pressão 1: {pressao1:.2f} bar")

            posicao1 = self.clp.read_int(db_number=2, start_byte=6)
            self.label_posicao1.configure(text=f"Posição 1: {posicao1:.2f} mm")

            status1 = self.clp.read_bool(db_number=2, start_byte=12, bit_number=0)
            self.label_status1.configure(text=f"Status 1: {status1}")

            # Prensa 2
            pressao2 = self.clp.read_int(db_number=2, start_byte=2)
            self.label_pressao2.configure(text=f"Pressão 2: {pressao2:.2f} bar")

            posicao2 = self.clp.read_int(db_number=2, start_byte=8)
            self.label_posicao2.configure(text=f"Posição 2: {posicao2:.2f} mm")

            status2 = self.clp.read_bool(db_number=2, start_byte=12, bit_number=1)
            self.label_status2.configure(text=f"Status 2: {status2}")

            # Prensa 3
            pressao3 = self.clp.read_int(db_number=2, start_byte=4)
            self.label_pressao3.configure(text=f"Pressão 3: {pressao3:.2f} bar")

            posicao3 = self.clp.read_int(db_number=2, start_byte=10)
            self.label_posicao3.configure(text=f"Posição 3: {posicao3:.2f} mm")
            
            status3 = self.clp.read_bool(db_number=2, start_byte=12, bit_number=2)
            self.label_status3.configure(text=f"Status 3: {status3}")
            
        self.after(1000, self.update_data)  # Atualiza a cada 1 segundo
