import os

def menu():
    os.system('cls')
    cmd = int(input("""
    1 - Comedorias e Restaurantes parceiros
    2 - Troca de Enxovais (Lençol, Toalhas, Travesseiros, Tapetes...)
    3 - Controle dos Dispositivos do Quarto (Tv, Ar-Condicionado, Luz, Cortina)
    4 - Informações Turisticas (Locais Próximos, Praias, Parques...)
    5 - Informações do Hotel (Eventos, Horários das Refeições)
    6 - Serviços adicionais (Parceiros do Hotel: Serviços de Massagem, Passeios de Bug, Fotográfos...)

Digite o número que deseja: """))

    if cmd == 1:
        tela1()
    elif cmd == 2:
        tela2()
    elif cmd == 3:
        tela3()
    elif cmd == 4:
        tela4()
    elif cmd == 5:
        tela5()
    elif cmd == 6:
        tela6()
    else:
        os.system('cls')
        print("Você digitou um comando inválido, digite novamente uma das opções abaixo:")
        menu()

def tela1():
    os.system('cls')
    print('Comedorias e Restaurantes parceiros:\n\n')
    print('1. Filé do Zezé \n2. Najuany Bistrô\n3. Basílico Ristorante\n4. Bodega do Sertão\n5. Del Mare')
    input('\n\nPressione ENTER para voltar ao Menu')
    menu()

def tela2():#troca de enxovais
    while True:
        os.system('cls')
        print('você abriu a tela 2')
        cmd = int(input("""
        1 - Troca de Travesseiros
        2 - Solicitar troca de toalhas
        3 - Solicitar troca de roupas de cama
        4 - Solicitar troca de tapetes
        5 - Voltar ao menu

        Digite o número que deseja: """))
        
        if cmd == 1:#troca de travesseiros
            os.system('cls')
            print('Seus travesseiros serão trocados!!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 2:#troca de toalhas
            os.system('cls')
            print('Suas toalhas serão trocadas!!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 3:#troca de roupas de cama
            os.system('cls')
            print('Suas roupas de cama serão trocadas!!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 4:
            os.system('cls')
            print('Seus tapetes serão trocados!!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 5:
            menu()

        else:
            os.system('cls')
            print('Seu comando digitado é inválido')
            tela2()


def televisao():
    os.system('cls')
    cmd = int(input("""
    1 - Canais
    2 - Diminuir volume
    3- Aumentar volume
    4 - Ligar
    5 - Desligar
    6 - Voltar ao menu

    Digite o número que deseja: """))


    if cmd == 1:
        os.system('cls')
        print('Os seguintes canais estão disponíveis:')
        print('1. Disney Channel \n2. HBO \n3. Albion Online')
        input('Pressione ENTER para voltar ao menu Televisão')
        televisao()
    elif cmd == 2:
        os.system('cls')
        volume = int(input("Em quanto você deseja diminuir o volume? "))
        print('Volume diminuído em', volume)
        input('\nPressione ENTER para voltar ao menu Televisão')
        televisao()
    elif cmd == 3:
        os.system('cls')
        volume = int(input("Em quanto você deseja diminuir o volume? "))
        print('Volume aumentado em', volume)
        input('\nPressione ENTER para voltar ao menu Televisão')
        televisao()
    elif cmd == 4:
        os.system('cls')
        print('A televisão está sendo ligada')
        input('\nPressione ENTER para voltar ao menu Televisão')
        televisao()
    elif cmd == 5:
        os.system('cls')
        print('A televisão está sendo desligada')
        input('\nPressione ENTER para voltar ao menu Televisão')
        televisao()
    elif cmd == 6:
        tela3()
    else:
        os.system('cls')
        print("Você digitou um comando invalido")
        input('Pressione ENTER para voltar ao menu Televisão')
        televisao()


def persianas():
    os.system('cls')
    cmd = int(input("""
    1 - Subir persianas
    2 - Descer persianas
    3- Voltar ao menu
    Digite o número que deseja: """))

    if cmd == 1:
        os.system('cls')
        print('As persianas foram levantadas com sucesso')
        input('\nPressione ENTER para voltar ao menu Persianas')
        persianas()
    elif cmd == 2:
        os.system('cls')
        print('As persianas foram decidas com sucesso')
        input('\nPressione ENTER para voltar ao menu Persianas')
        persianas()
    elif cmd == 3:
        tela3()
    else:
        os.system('cls')
        print("Você digitou um comando invalido")
        input('Pressione ENTER para voltar ao menu Persianas')
        persianas()


def luzes():
    os.system('cls')
    cmd = int(input("""
    1 - Ligar luzes
    2 - Desligar luzes
    3 - Diminuir intensidade da luzes
    4 - Aumentar intensidade da luzes
    5 - Voltar ao menu

    Digite o número que deseja: """))

    if cmd == 1:
        os.system('cls')
        print('As luzes foram ligadas com sucesso')
        input('\nPressione ENTER para voltar ao menu luzes')
        luzes()
    elif cmd == 2:
        os.system('cls')
        print('As luzes foram desligadas com sucesso')
        input('\nPressione ENTER para voltar ao menu luzes')
        luzes()
    elif cmd == 3:
        os.system('cls')
        print('A intensidade das Luzes está moderada')
        input('\nPressione ENTER para voltar ao menu luzes')
        luzes()
    elif cmd == 4:
        os.system('cls')
        print('A intensidade das Luzes está alta')
        input('\nPressione ENTER para voltar ao menu luzes')
        luzes()
    elif cmd == 5:
        tela3()
    else:
        os.system('cls')
        print("Você digitou um comando invalido")
        input('Pressione ENTER para voltar ao menu luzes')
        luzes()

def temperatura():
    os.system('cls')
    cmd = int(input("""
    1 - Diminuir temperatura
    2 - Aumentar temperatura
    3- Voltar ao menu
    Digite o número que deseja: """))

    if cmd == 1:
        os.system('cls')
        print('A temperatura foi diminuída com sucesso')
        input('\nPressione ENTER para voltar ao menu temperatura')
        temperatura()
    elif cmd == 2:
        os.system('cls')
        print('A temperatura foi aumentada com sucesso')
        input('\nPressione ENTER para voltar ao menu temperatura')
        temperatura()
    elif cmd == 3:
        os.system('cls')
        tela3()
    else:
        os.system('cls')
        print("Você digitou um comando invalido")
        input('Pressione ENTER para voltar ao menu temperatura')
        temperatura()


def tela3():#Controle do Quarto
    os.system('cls')
    cmd = int(input("""
    1 - Televisão
    2 - Persianas
    3 - Luzes
    4 - Temperatura
    5 - Voltar ao menu

    Digite o número que deseja: """))


    if cmd == 1:
        televisao()
    elif cmd == 2:
        persianas()
    elif cmd == 3:
        luzes()
    elif cmd == 4:
        temperatura()
    elif cmd == 5:
        menu()
    else:
        os.system('cls')
        print("Você digitou um comando invalido, digite novamente uma das opções abaixo:")
        menu()



def tela4():
    os.system('cls')
    print('Pontos Turísticos:\n\n')
    print('1. Museu da História Natural \n2. Centro Cultural de Pajucara\n3. Praia do Francês\n4. Ponta Negra\n5. Praia do Gunga\n6. Museu do Theo Brandão')
    input('\n\nPressione ENTER para voltar ao Menu')
    menu()

def tela5():
    os.system('cls')
    print('Horários do hotel:')
    print('Entrada e saída permitidos a qualquer horário do dia\n Funcionamos 24/7\n\n')
    print('Horários das refeições:\n\n')
    print('1. Café da manhã: 7:00 - 10:30 \n2. Almoço: 11:00 - 13:30 \n3. Lanche da tarde: 15:00 - 16:30 \n4. Janta: 19:30 - 22:00 ')
    input('\n\nPressione ENTER para voltar ao Menu')
    menu()


def solicitarFuncionario():
    os.system('cls')
    cmd = int(input("""
        1 - Repor Frigobar
        2 - Recolher Lixo
        3 - Limpeza
        4 - Voltar ao menu

        Digite o número que deseja: """))

    if cmd == 1:
        os.system('cls')
        print('Em breve seu frigobar seráreposto. Funcionários à caminho!!')
        input('\n\nPressione ENTER para voltar aos serviços adicionais')
        menu()
    elif cmd == 2:
        os.system('cls')
        print('O lixo será recolhido em breve. Aguarde um momento!!')
        input('\n\nPressione ENTER para voltar aos serviços adicionais')
        menu()
    elif cmd == 3:
        os.system('cls')
        print('O serviço de limpeza está se dirigindo ao seu quarto!!')
        input('\n\nPressione ENTER para voltar aos serviços adicionais')
        menu()
    elif cmd == 4:
        menu()
    else:
        os.system('cls')
        print("Você digitou um comando invalido, digite novamente uma das opções abaixo:")
        menu()



def tela6():
    solicitarFuncionario()

menu()
