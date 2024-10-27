# Importa o layout e bibliotecas necessárias
from layout import layout  # Função para exibir o layout do programa
from pymem import *  # Importa a biblioteca pymem para manipulação de memória
from pymem.process import *  # Importa ferramentas de manipulação de processos
from pymem.exception import *  # Importa exceções específicas do pymem
from settings import *  # Importa configurações adicionais do arquivo settings
from time import sleep  # Importa sleep para pausar entre operações
from os import system  # Importa system para limpar a tela no console

# Função para obter o ponteiro para um endereço específico na memória do jogo
def getPointer(base, offsets):
    # Lê o endereço base na memória do processo
    addr = pm.read_ulonglong(base)
    # Itera sobre os offsets fornecidos para calcular o endereço final
    for offset in offsets:
        if offset != offsets[-1]:  # Se não for o último offset, continua o cálculo
            addr = pm.read_ulonglong(addr + offset)
    # Adiciona o último offset para obter o endereço final
    addr += offsets[-1]
    return addr  # Retorna o endereço final calculado

# Função para definir o valor da vida no jogo para 100.0
def life():
    return pm.write_float(getPointer(module + endereco, offsetLife), 100.0)

# Função para definir o valor da energia no jogo para 100.0
def energy():
    return pm.write_float(getPointer(module + endereco, offsetEnergy), 100.0)

# Função para definir o valor da stamina no jogo para 100.0
def stamina():
    return pm.write_float(getPointer(module + endereco, offsetStamina), 100.0)

# Função principal que controla o fluxo do programa
def main():
    global pm, module  # Define `pm` e `module` como variáveis globais
    system("cls")  # Limpa a tela do console
    print(layout())  # Exibe o layout inicial do programa
    
    # Loop que continua até encontrar o processo do jogo
    while True:
        try:
            # Tenta criar uma instância de Pymem para o processo do jogo "TheForest.exe"
            pm = Pymem("TheForest.exe")
            # Obtém o módulo base do jogo para operações de memória
            module = module_from_name(pm.process_handle, "TheForest.exe").lpBaseOfDll
            print("[*] Processo encontrado!")  # Confirma que o processo foi encontrado
            break  # Interrompe o loop, pois o processo foi localizado
        except ProcessNotFound:
            # Se o processo não foi encontrado, atualiza a mensagem e tenta novamente
            system("cls")  # Limpa a tela do console
            print(layout())  # Exibe o layout do programa
            print("[*] Procurando processo do jogo...")  # Mostra status de procura
            sleep(3)  # Aguarda 3 segundos antes de tentar novamente

    # Início das operações principais após encontrar o processo
    try:
        print("[*] Iniciando...")  
        sleep(1)
        print("[*] Life: [OK]")  # Confirma que a função `life()` está pronta
        sleep(0.5)
        print("[*] Energy: [OK]")  # Confirma que a função `energy()` está pronta
        sleep(0.5)
        print("[*] Stamina: [OK]")  # Confirma que a função `stamina()` está pronta
        sleep(1)
        
        # Loop principal para manter os valores de vida, energia e stamina no jogo
        while True:
            try:
                # Atualiza os valores de vida, energia e stamina no jogo
                life()
                energy()
                stamina()
                # Exibe uma mensagem de sucesso na mesma linha
                print("\r[*] Injetado com sucesso!", end="")
            except Exception as e:
                # Se ocorrer um erro (ex.: processo encerrado), atualiza a interface
                system("cls")  # Limpa a tela
                print(layout())  # Exibe o layout inicial novamente
                print("[*] Life: [OK]")  # Reexibe status de vida
                print("[*] Energy: [OK]")  # Reexibe status de energia
                print("[*] Stamina: [OK]")  # Reexibe status de stamina
                print("[*] Injetando...")  # Indica tentativa de reinjeção
                sleep(3)  
    except Exception as e:
        # Captura erros fora do loop principal e exibe a mensagem de erro
        print(f"[*] Erro: {e}")

# Executa a função principal quando o script é executado diretamente
if __name__ == "__main__":
    main()
