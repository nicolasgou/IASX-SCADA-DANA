# 🛠️ Monitor de Prensas - Visor Industrial com Python + Siemens S7-1200

Este projeto é uma aplicação Python com interface gráfica para **monitoramento contínuo (24/7)** de **prensas de forjaria automotiva** via **CLP Siemens S7-1200**, utilizando **CustomTkinter** para uma visualização em tempo real em uma **TV de 50''** conectada a um **PC industrial** ou **Raspberry Pi**.


## 📸 Visão Geral

- Interface gráfica moderna com **CustomTkinter**.
- Leitura de variáveis **analógicas e digitais** do CLP (pressão, posição, status).
- Comunicação via **PROFINET (S7-ISO-on-TCP)** utilizando a biblioteca `snap7`.
- Compatível com **Raspberry Pi**, **Ubuntu**, **PCs industriais**.
- Operação ininterrupta: sistema robusto para execução contínua em ambientes industriais.

## 📦 Estrutura do Projeto

          IASX-SCADA-DANA/
              ├── main.py # Arquivo principal do app
              ├── clp_manager.py # Comunicação com o CLP Siemens
              ├── gui_manager.py # Interface gráfica com CustomTkinter
              ├── utils.py # Funções auxiliares (reconexão, logs)
              ├── requirements.txt # Lista de bibliotecas Python
              └── README.md # Este arquivo

## ✅ Requisitos

- Python 3.7 ou superior
- Sistema Linux (Raspberry Pi OS, Ubuntu ou Debian)
- Acesso à rede com IP do CLP S7-1200
- Porta TCP 102 liberada


## 🔌 Comunicação com o CLP Siemens
A comunicação é feita com o protocolo S7-ISO-on-TCP, que é a base do PROFINET e compatível com o CLP S7-1200.
Requisitos do CLP:
 - IP fixo e acessível pela rede
 - DBs (blocos de dados) configurados com permissões de leitura
 - Rack e Slot corretos (geralmente Rack 0, Slot 1)
 - Nenhuma senha de proteção ativa (ou configure login no futuro)

## 🖥️ Exibição na TV Industrial
O aplicativo é otimizado para telas Full HD (1920x1080), ideal para exibição contínua em TVs de 50''.
Recomenda-se executar em modo maximizado com o Raspberry Pi ou PC conectado via HDMI.

## 💡 Funcionalidades Futuras
 - Armazenamento de histórico de variáveis em CSV
 - Gráficos de tendência (pressão e posição)
 - Alarmes com alertas visuais e sonoros
 - Tela de manutenção
 - Configuração de limites e parâmetros via config.json

---
## 🚀 Configuracao e Instalação

### 1. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Download and compile snap7 for rpi
```
wget http://sourceforge.net/projects/snap7/files/1.2.1/snap7-full-1.2.1.tar.gz/download 
tar -zxvf download.tar.gz
cd snap7-full-1.2.1/build/unix
sudo make –f arm_v6_linux.mk all
```
copy compiled library to your lib directories
```
sudo cp ../bin/arm_v6-linux/libsnap7.so /usr/lib/libsnap7.so
sudo cp ../bin/arm_v6-linux/libsnap7.so /usr/local/lib/libsnap7.so
```
### 3. install python pip if you don't have it:
```
sudo apt-get install python-pip
sudo pip install python-snap7
```
You will need to edit the lib_location on common.py in the directory:
```
/usr/local/lib/python2.7/dist-packages/snap7/
```
Add a line in the __init__ part of the Snap7Library class:
```
lib_location='/usr/local/lib/libsnap7.so' 
```
example below:

```
class Snap7Library(object):
    """
    Snap7 loader and encapsulator. We make this a singleton to make
    sure the library is loaded only once.
    """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._instance.lib_location = None
            cls._instance.cdll = None
        return cls._instance

    def __init__(self, lib_location=None):
        lib_location='/usr/local/lib/libsnap7.so' # add this line here
        if self.cdll:
            return
        self.lib_location = lib_location or self.lib_location or find_library('snap7')
        if not self.lib_location:
            msg = "can't find snap7 library. If installed, try running ldconfig"
            raise Snap7Exception(msg)
        self.cdll = cdll.LoadLibrary(self.lib_location)

```
### 4. Clone do Projeto
```
git clone https://github.com/seu-usuario/IASX-SCADA-DANA.git
cd IASX-SCADA-DANA
```



### 5. Instale as dependências Python

```
cd IASX-SCADA-DANA
pip install --break-system-packages -r requirements.txt
```



### ▶️ 6. Executar
```
cd IASX-SCADA-DANA
python3 main.py

```

# 👨‍💻 Autor
NicolasGou
Engenheiro de Software e Arquitetura de Sistemas
Especialista em Soluções Industriais, Visão Computacional e IIoT














