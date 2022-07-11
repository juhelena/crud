def remove(planilha):
    linhas = int(input("Digite quantas linhas deseja remover: "))
    for i in range(linhas):
        valor = int(input("Digite o número do index para remover os dados da linha: "))
        planilha.drop(planilha.index[valor], inplace=True)
        planilha.to_excel('Cadastro Escolas.xlsx', index=False)
    print("\n\33[32mItem removido com sucesso!\33[m")