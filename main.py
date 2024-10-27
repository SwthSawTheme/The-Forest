from layout import layout
from pymem import *
from pymem.process import *
from pymem.exception import *
from settings import *
from time import sleep
from os import system

def getPointer(base, offsets):
    addr = pm.read_ulonglong(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = pm.read_ulonglong(addr + offset)
    addr += offsets[-1]
    return addr


def life():
   return pm.write_float(getPointer(module + endereco, offsetLife ),100.0)

def energy():
    return pm.write_float(getPointer(module + endereco, offsetEnergy),100.0)

def stamina():
    return pm.write_float(getPointer(module + endereco, offsetStamina),100.0)

def main():
    global pm, module
    system("cls")
    print(layout())
    
    while True:
        try:
            pm = Pymem("TheForest.exe")
            module = module_from_name(pm.process_handle, "TheForest.exe").lpBaseOfDll
            print("[*] Processo encontrado!")
            break
        except ProcessNotFound:
            # Atualiza apenas a mensagem de status em vez de limpar toda a tela
            system("cls")
            print(layout())
            print("[*] Procurando processo do jogo...")
            sleep(3)

    try:
        # Inicia a execução principal
        print("[*] Iniciando...")
        sleep(1)
        print("[*] Life: [OK]")
        sleep(0.5)
        print("[*] Energy: [OK]")
        sleep(0.5)
        print("[*] Stamina: [OK]")
        sleep(1)
        
        while True:
            try:
                life()
                energy()
                stamina()
                print("\r[*] Injetado com sucesso!", end="")  # Atualiza sem piscar
                sleep(0.5)
            except Exception as e:
                system("cls")
                print(layout())
                print("[*] Life: [OK]")
                print("[*] Energy: [OK]")
                print("[*] Stamina: [OK]")
                print("[*] Injetando...")
                sleep(3)
    except Exception as e:
        print(f"[*] Erro: {e}")

if __name__ == "__main__":
    main()
