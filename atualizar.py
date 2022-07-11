from pandas import DataFrame

def atualiza(planilha: DataFrame):
    linha = int(input("Digite o numero do index: "))
    coluna = input("Digite o nome da coluna: ")
    valor = input("Digite o valor que deseja atualizar: ").upper()
    planilha.at[linha,coluna]=valor
    planilha.to_excel('Cadastro Escolas.xlsx', index=False)
    print("\n\33[32mValor alterado com sucesso!\33[m")