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
   return pm.write_float(getPointer(module + endereco, offset ),100.0)

def main():
    system("cls")
    print(layout())

    try:
        print("[*] Iniciando...")
        sleep(1)
        if 'module' in globals():
            print(f"[*] Processo {module} encontrado!")
        else:
            raise NameError("Processo não encontrado!")

        sleep(1)
        print("[*] Rodando...")
        while True:
            life()

    except Exception as e:
        print(f"[*] Erro: {e}")

if __name__ == "__main__":
    main()
