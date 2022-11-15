
#Simulação de telas do protótipo por meio do terminal (esboço de código do protótipo de média fidelidade)
#Do lado esquerdo das opções da tela inicial, terá um pegueno widget ocupando 1/4 da tela inicial, mostrando ao hóspede os 
#principais avisos e eventos do hotel.
#Antes de exibir o menu, serão exibidas telas de apresentação e boas vindas, com um mascote no centro e balões de fala 
#no lado superior esquerdo do mesmo. Melhor vizulaização no protótipo do figma.




import os


def tutorial(nome,quarto):
    os.system('cls')
    print('\nPara prosseguir para a próxima tela, precione ENTER para continuar\n\n')
    input(f'Olá, boa Tarde!\nSeja bem vindo(a) {nome}, ao Serviço de Quarto virtual do Saint Patrick Grand Hotel!')
    input(f'Me chamo Fernando e serei seu assistente virtual durante sua estadia no quarto {quarto} do nosso hotel! (...)')
    os.system('cls')

    input('\nEste é seu canal de comunicação direto com os nossos funcionários do Hotel')

    input('Esse é o lugar onde você tem a possibilidade de solicitar\ntrocas de enxováis, conversar diretamente\n'
        'com um funcionário e utilizar nosso controle universal por exemplo. (...)')
    os.system('cls') 

    print('Esse é o lugar onde você tem a possibilidade de solicitar\ntrocas de enxováis, conversar diretamente',
        'com um funcionário e utilizar nosso controle universal por exemplo.')
    input('\nAqui também tem indicações de restaurantes parceiros do nosso hotel personalizados para você!')
    menu()

def menu(): #tela inicial
    os.system('cls')
    print('Menu principal')
    #O "widget do tempo" estará no seu modo minimizado no canto superior direito da tela inicial
    #que ao ser clicado, se expande e sobrepõe de maneira transparente a tela inicial (menu)
    cmd = int(input("""
    0 - Abrir Widget do Tempo 
    1 - Serviços de Quarto
    2 - Controle
    3 - Especialmente pra voçê
    4 - Conheça o Hotel
    5 - Ajuda
    
    Digite o número que deseja: """))
    if cmd == 0:
        widget_tempo()
    elif cmd == 1:
        servicos()
    elif cmd == 2:
        controle()
    elif cmd == 3:
        turismo()
    elif cmd == 4:
        info_hotel()
    elif cmd == 5:
        assistencia()
    else:
        os.system('cls')
        print("Você digitou um comando inválido, digite novamente uma das opções abaixo:")
        menu()

def servicos(): #Serviços de Quarto
    #No canto inferior da tela, terá o mascote e um balão de fala escrito: 
    #"Caso não encontre o que deseja, você pode conversar com um de nossos funcionários!"

    os.system('cls')
    print('Serviços de Quarto:\n')
    print('1.Solicitar um funcionário      2.Limpeza de Quarto')
    print('3.Troca de Enxoval              4.Chamar Assistência Técnica')
    print('5.Pedir Reposição de Frigobar   6.Converse com um funcionário')

    cmd = int(input('\n\nInira a opção que deseja ou pressione ENTER para voltar ao Menu: '))

    if cmd == 1:
        input('Um funcionário já está a caminho!')
    elif cmd == 2:
        input('A sua solicitação da limpeza do quarto já foi encaminhada')
    elif cmd == 3:
        enxoval()
    elif cmd == 4:
        input('A assistência já está a caminho do seu quarto!')
    elif cmd ==5:
        input('Sua solicitação de repor o frigobar já foi encaminhada')
    elif cmd ==6:
        input('Encaminhando você para o chat com um de nossos funcionários...')
        #Abrir uma nova tela com um chat com algum funcionário da recepção.
    else:
        menu()

def enxoval():#troca de enxovais
    while True:
        os.system('cls')
        print('Troca de Enxoval')
        cmd = int(input("""
        1 - Troca de Travesseiros
        2 - Solicitar troca de toalhas
        3 - Solicitar troca de roupas de cama
        4 - Solicitar troca de tapetes
        5 - Voltar ao menu

        Digite o número que deseja: """))
        
        #Qualquer pedido do enxoval será enviado diretamente ao sistema da recepção, já identificando o quarto
        if cmd == 1:#troca de travesseiros
            os.system('cls')
            qntd = int(input('Quantos travesseiros você deseja? '))
            print(f'Estamos encaminhando {qntd} travesseiros para o seu quarto!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 2:#troca de toalhas
            os.system('cls')
            qntd = int(input('Quantas toalhas você deseja? '))
            print(f'Estamos encaminhando {qntd} toalhas para o seu quarto!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 3:#troca de roupas de cama
            os.system('cls')
            qntd = int(input('Quantas roupas de cama você deseja? '))
            print(f'Estamos encaminhando {qntd} roupas de cama para o seu quarto!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 4:#troca de tapetes
            os.system('cls')
            qntd = int(input('Quantos tapetes você deseja? '))
            print(f'Estamos encaminhando {qntd} tapetes para o seu quarto!')
            input('\nPressione ENTER para voltar à Troca de enxovais')

        elif cmd == 5:
            menu()

        else:
            os.system('cls')
            print('Seu comando digitado é inválido')
            enxoval()


def controle():#Controle do Quarto
    os.system('cls')
    print('Controle do Quarto\n')
    cmd = int(input("""
    1 - Televisão
    2 - Persianas
    3 - Luzes
    4 - Ar Condicionado
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
        input("Você digitou um comando invalido, digite novamente uma das opções abaixo:")
        controle()

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
        print('1.Disney Channel \n2.HBO \n3.Discovery Channel \n4.Globo')
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
        controle()
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
        controle()
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
        controle()
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
        controle()
    else:
        os.system('cls')
        print("Você digitou um comando invalido")
        input('Pressione ENTER para voltar ao menu temperatura')
        temperatura()

def turismo(): #Especialmente pra você (Informações turísticas)
    os.system('cls')
    print('Especialmente Pra Você\n')
    print('1.Locais Próximos\n2.Conheça Nossos Parceiros\n3.Atividades Turísticas pra Você e Sua Família')
    #Cada tela das opções a cima terá informações claras e objetivas sobre a avaliação, localização e horário de
    # funcionamento. Além de preços dos pacotes de passeios turísticos.     

    input('\n\nPressione ENTER para voltar ao Menu')
    menu()

def info_hotel(): #Conheça o Hotel (info e avisos sobre o hotel)
    os.system('cls')
    print('Conheça o Hotel\n\n')
    print('Avisos Relevantes:\n\n1.Aviso1\n2.Aviso2') #exibir avisos relevantes sobre o hotel, opção personalizável.
    print('\nHorários do hotel:')
    print('\n-Entrada e saída permitidos a qualquer horário do dia\n')
    print('Horários das refeições:')
    print('\n1. Café da manhã: 7:00 - 10:30 \n2. Almoço: 11:00 - 13:30 \n3. Lanche da tarde: 15:00 - 16:30 \n4. Janta: 19:30 - 22:00 ')
    input('\n\nPressione ENTER para voltar ao Menu')
    menu()

def assistencia():
    os.system('cls')
    print('Ajuda')
    cmd = int(input("""
        1 - Chat com Funcionário
        2 - Emergência Médica
        3 - Como Funciona o Nosso Sistema
        4 - Voltar ao menu

        Digite o número que deseja: """))

    if cmd == 1:
        os.system('cls')
        print('Encaminhando você para o chat com um de nossos funcionários...')
        input('\n\nPressione ENTER para voltar ao menu de assistência')
        assistencia()
    elif cmd == 2:
        os.system('cls')
        print('Seu chamado emergêncial foi enviado para a recepção, não se preocupe \nprofissionais já estão a caminho')
        input('\n\nPressione ENTER para voltar ao menu de assistência')
        assistencia()
    elif cmd == 3:
        os.system('cls')
        input('\n\nPressione ENTER para rever o tutorial inicial')
        tutorial()
    elif cmd == 4:
        menu()
    else:
        os.system('cls')
        input("Você digitou um comando invalido, precione ENTER e digite novamente uma das opções válidas:")
        assistencia()

def widget_tempo():
    os.system('cls')
    print('Widget do Tempo\n')
    print('Precione ENTER quando quiser voltar ao menu\n\n')
    input('Maceió, Alagoas   | 18ºGraus'
        '\n08 de Novembro    | 18:40'
        '\nHoje irá chover!  | Previsão Semanal') #Ao lado mostrar tabelinha dos dias da semana e suas previsões temporais
    menu()


def dados_hospedes():
    clientes = open("siteProjetos/bancoDados.txt", "r") #Simulando a "leitura" de um banco de dados
    quartos = []
    nomes = []

    for line in clientes:
        quartos.append(line[0:2])
        nomes.append(line[4:30].rstrip())

    clientes.close()

    for i in range(len(quartos)):

        if quartos[i] == '02':
            dado_hospede = [nomes[i], quartos[i]]

    return dado_hospede



#O nome do hóspede assim como o número do quarto será puxado de um banco de dados do sistema do hotel.
#Esses dados podem ser usados para pedidos feitos no quarto e uma maior "afinidade" na interação com
#o cliente
hospede = dados_hospedes()[0]
quarto = dados_hospedes()[1]

tutorial(hospede, quarto)
menu()
