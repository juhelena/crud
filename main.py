import cadastrar
import pesquisar
import deletar
import atualizar
import pandas as pd

planilha = pd.read_excel('Cadastro Escolas.xlsx')

def menu(planilha):
    opcao = 0  
    while opcao != 5:
        print("\n\33[96m-------- MENU --------\33[m")
        print("    [\33[95m1\33[m] Cadastrar")
        print("    [\33[95m2\33[m] Pesquisar")
        print("    [\33[95m3\33[m] Atualizar")
        print("    [\33[95m4\33[m] Deletar")
        print("    [\33[95m5\33[m] Sair")
        print("\33[96m----------------------\33[m")
        opcao = int(input("Opção: "))

        if opcao == 1:
            cadastrar.adiciona(planilha)
        elif opcao == 2:       
            pesquisar.busca(planilha)
        elif opcao == 3:    
            atualizar.atualiza(planilha)
        elif opcao == 4:
            deletar.remove(planilha)
        elif opcao >= 6:
            print("\33[31mDigite uma opção válida.\33[m")
    
menu(planilha)