import inquirer

def adiciona(planilha):

    qtd = planilha['Nome'].count()

    pergunta = [inquirer.List('escolha', message="Dependência Administrativa: ", choices=['Estadual', 'Federal', 'Municipal', 'Privada'])]
    resposta = inquirer.prompt(pergunta)
    planilha.loc[qtd+1, 'Dependencia Administrativa'] = resposta['escolha'].upper()
    planilha.loc[qtd+1, 'Nome']=input('Nome: ').upper()
    planilha.loc[qtd+1, 'Codigo']=int(input('Código: '))
    planilha.loc[qtd+1, 'Municipio']=input('Município: ').upper()
    planilha.loc[qtd+1, 'CEP']=int(input('CEP: '))
    planilha.loc[qtd+1, 'Endereco']=input('Endereço: ').upper()
    planilha.loc[qtd+1, 'Fone']=int(input('Telefone: '))

    planilha.to_excel('Cadastro Escolas.xlsx', index=False)
    print("\n\33[32mCadastro realizado!\33[m")

