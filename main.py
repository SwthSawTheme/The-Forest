from layout import layout
from pymem import *
from pymem.process import *
from pymem.exception import *
from settings import *
from time import sleep
from os import system

try:
    pm = Pymem("TheForest.exe")
    module = module = module_from_name(pm.process_handle,"TheForest.exe").lpBaseOfDll

except ProcessNotFound:
    pass

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
    system("cls")
    print(layout())
    end = hex(module).replace("0","")
    try:
        print("[*] Iniciando...")
        sleep(1)
        if 'module' in globals():
            print(f"[*] Processo 0{end} encontrado!")
        else:
            raise NameError("Processo não encontrado!")

        sleep(0.5)
        print(f"[*] Life: [OK]")
        sleep(0.5)
        print(f"[*] Energy: [OK]")
        sleep(0.5)
        print(f"[*] Stamina: [OK]")
        sleep(0.5)
        print("[*] Rodando...")
        while True:
            life()
            energy()
            stamina()
    except Exception as e:
        print(f"[*] Erro: {e}")

if __name__ == "__main__":
    main()
