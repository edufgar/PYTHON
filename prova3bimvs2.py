#Exercício Concessionária

placacarro = [0] * 25
kmsrevisao = [0] * 25
tiprevisao = [0] * 25
valcomb = [0] * 25
proxlivre = 0

opcao = 0
while(opcao != 6):
    print("Menu")
    print("1 Registrar uma única revisão")
    print("2 Contagem de revisões")
    print("3 Listagem de revisões")
    print("4 A revisão mais cara e a mais barata")
    print("6 Sair")
    opcao = int(input("Digite a opcão desejada: "))

    if opcao == 1:

        print("Registro de Revisões")
        placarev = int(input("Digite os números da placa: "))
        achei = False
        for i in range(25):
            if placarev == placacarro[i]:
                print("Revisão desta placa já agendada...")
                achei = True
                break
        if not achei:
            placacarro[proxlivre] = int(input("Digite os números da placa: "))
            kmsrevisao[proxlivre] = int(input("Digite a quilometragem do carro: "))
            tiprevisao[proxlivre] = int(input("Digite o tipo da revisão (1-básico, 2-intermediário, 3-completa): "))
            valcomb[proxlivre] = float(input("Digite o valor combinado da revisão em reais: "))
            proxlivre = proxlivre + 1
            print("Revisão registrada com sucesso!")

    if opcao == 2:
        print("Contagem de Revisões")
        km10 = 0
        km20 = 0
        km30 = 0
        km40 = 0
        for i in range(25):
            if kmsrevisao[i] == 10000:
                km10 = km10 + 1
            if kmsrevisao[i] == 20000:
                km20 = km20 + 1
            if kmsrevisao[i] == 30000:
                km30 = km30 + 1
            if kmsrevisao[i] >= 40000:
                km40 = km40 + 1

        print("Na revisão de 10 mil km temos o número de: ", km10)
        print("Na revisão de 20 mil km temos o número de: ", km20)
        print("Na revisão de 30 mil km temos o número de: ", km30)
        print("Na revisão de 40 mil km temos o número de: ", km40)

    if opcao == 3:
        print("Listagem de Revisões")
        for i in range(25):
            print("As Placas dos carros: ", placacarro[i])
            print("As suas respectivas Kms: ", kmsrevisao[i])
            print("Os tipos de revisão: ", tiprevisao[i])
            print("Os valores combinados: ", valcomb[i])

        for i in range(25):
            if tiprevisao == 1:
                print("A revisão do tipo ", tiprevisao[i], " tem como valor combinado ", valcomb[i])
        for i in range(25):
            if tiprevisao == 2:
                print("A revisão do tipo ", tiprevisao[i], " tem como valor combinado ", valcomb[i])
        for i in range(25):
            if tiprevisao == 3:
                print("A revisão do tipo ", tiprevisao[i], " tem como valor combinado ", valcomb[i])
                
                
    if opcao == 4:
        arevisaomaiscara = 0
        placarevisaomaiscara = 0
        for i in range(25):
            if valcomb[i] > arevisaomaiscara:
                arevisaomaiscara = valcomb[i]
                placarevisaomaiscara = placacarro[i]
        print("A placa ", placarevisaomaiscara)
        print("A revisão mais cara é ", arevisaomaiscara)

        arevisaomaisbarata = 0
        placarevisaomaisbarata = 0
        for i in range(25):
            if i == 0:
                arevisaomaisbarata = valcomb[i]
                placarevisaomaisbarata = placacarro[i]
            else:
                if valcomb[i] < arevisaomaisbarata:
                    arevisaomaisbarata = valcomb[i]
                    placarevisaomaisbarata = placacarro[i]
        print("A placa ", placarevisaomaisbarata)
        print("A revisão mais cara é ", arevisaomaisbarata)

