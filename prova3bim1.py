

placacarro = [0] * 25
kmsrevisao = [0] * 25
tiprevisao = [0] * 25
valcomb = [0] * 25

for i in range(25):

    repete = True
    while(repete):
        novaplaca = int(input("Digite os números da placa: "))
        achei = False
        for j in range(25):
            if novaplaca == placacarro[j]:
                print("Placa já cadastrada")
                achei = True
                repete = True
                break
        if not achei:
            repete = False

    placacarro[i] = novaplaca
    kmsrevisao[i] = float(input("Digite a  kilometragem  de revisão do veículo: "))
    tiprevisao[i] = int(input("Digite o tipo da revisão (1-básico, 2-intermediário, 3-completa): "))
    valcomb[i] = float(input("Digite o valor combinado da revisão em reais: "))


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
        #proxlivre = 0
        print("Registro de Revisões")
        placarev = int(input("Digite os números da placa: "))
        achei = False
        for i in range(25):
            if placarev == placacarro[i]:
                print("Revisão desta placa já agendada...")
                achei = True
                break
        if not achei:
            #placacarro[proxlivre] = int(input("Digite os números da placa: "))
            #kmsrevisao[proxlivre] = int(input("Digite a quilometragem do carro: "))
            #tiprevisao[proxlivre] = int(input("Digite o tipo da revisão (1-básico, 2-intermediário, 3-completa): "))
            #valcomb[proxlivre] = float(input("Digite o valor combinado da revisão em reais: "))
            #proxlivre = proxlivre + 1
            print("Revisão registrada com sucesso!")

    if opcao == 2:
        print("Contagem de Revisões")


    if opcao == 3:
        print("Listagem de Revisões")
        for i in range(25):
            print(tiprevisao[i])


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


