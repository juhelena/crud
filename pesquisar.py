from time import sleep

def busca(planilha):
    print("\n\33[96m[1]\33[m Buscar por Dependência Administrativa")
    print("\33[96m[2]\33[m Buscar por Município")
    print("\33[96m[3]\33[m Buscar por Código da Escola")
    print("\33[96m[4]\33[m Quantidade de Escolas")
    opcao = int(input("Opção: "))

    if opcao == 1:
        print("\n\33[96m[1]\33[mEstadual \33[96m[2]\33[mFederal \33[96m[3]\33[mMunicipal \33[96m[4]\33[mPrivada")
        escolha = int(input("Opção: "))
        if escolha == 1:
            print("\33[33\nmESCOLA ESTADUAL\33[m")
            print(planilha.loc[planilha['Dependencia Administrativa']=='ESTADUAL', ['Dependencia Administrativa', 'Nome', 'Municipio', 'CEP']])
        elif escolha == 2:
            print("\33[33\nmESCOLA FEDERAL\33[m")
            print(planilha.loc[planilha['Dependencia Administrativa']=='FEDERAL', ['Dependencia Administrativa', 'Nome', 'Municipio', 'CEP']])
        elif escolha == 3:
            print("\33[33\nmESCOLA MUNICIPAL\33[m")
            print(planilha.loc[planilha['Dependencia Administrativa']=='MUNICIPAL', ['Dependencia Administrativa', 'Nome', 'Municipio', 'CEP']])
        elif escolha == 4:
            print("\33[33\nmESCOLA PRIVADA\33[m")
            print(planilha.loc[planilha['Dependencia Administrativa']=='PRIVADA', ['Dependencia Administrativa', 'Nome', 'Municipio', 'CEP']])
        elif escolha >= 5:
            print("\33[31mDigite uma opção válida.\33[m")
    
    elif opcao == 2:
        valor = input("\nDigite o município: ").upper()
        print(f'\33[33\nmBuscando os dados do município de {valor}...\33[m')
        sleep(1.5)
        existe = False
        for i in planilha['Municipio']:
            if i == valor:
                existe = True
        if not existe:
            print("\33[31mMunicipio não encontrado na planilha.\33[m")
        else:
            print(planilha.loc[planilha['Municipio'] == valor])

    elif opcao == 3:
        valor = int(input("\nDigite o cógido da escola: "))
        print("\33[33\nmBuscando os dados...\33[m")
        sleep(1.5)
        existe = False
        for i in planilha['Codigo']:
            if i == valor:
                existe = True
        if not existe:
            print("\33[31mCódigo da escola não encontrado na planilha.\33[m")
        else:
            print(planilha.loc[planilha['Codigo'] == valor])

    elif opcao == 4:
        print("\33[33\nmQuantidade de Escolas\33[m")
        sleep(1)
        print(planilha['Dependencia Administrativa'].value_counts())

    elif opcao >= 5:
            print("\33[31mDigite uma opção válida.\33[m")
