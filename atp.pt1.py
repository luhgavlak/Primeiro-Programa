'1'#Cadastro
def obter_limite():
    nome = print('Olá! Bem-Vindo a 747 Aviation. Sou a Luisa Gavlak Vilares Cordeiro e vou te auxiliar hoje.\n')
    print('Primeiramente, você precisa responder algumas perguntas breves:')
    cargo = input('\nQual é a sua ocupação atual? ')
    salario = input('\nQual é o seu salário líquido? R$')
    while (float(salario)) <= 0:
        print('\033[31mInsira um salário válido maior do que zero.\033[m')
        salario = input('\nQual é o seu salário líquido? R$')
        if (float(salario)) > 0:
            pass
    nascimento = input('\nQual é o seu ano de nascimento? ')
    while (int(nascimento) <= 1920 or int(nascimento) > 2020):
        print('\033[31mInsira um ano de nascimento compreendido entre 1921 e 2020.\033[m')
        nascimento = input('\nQual é o seu ano de nascimento? ')
        if (int(nascimento) >= 1920 or int(nascimento) < 2020):
            pass
    print('\nOcupação: ', cargo)
    print('\nSalário: R$', salario)
    print('\nAno de nascimento: ', nascimento)

    # Idade apx
    from datetime import datetime
    hoje = datetime.now()
    ano = hoje.strftime("%Y")
    global idade
    idade = (int(ano) - int(nascimento))
    print('A sua idade aproximada é {}'.format(idade), 'anos \n')

    # Limite de gasto
    global credito
    credito = (int(idade) / 1000) * (float(salario)) + 100
    print('\nO seu limite de crédito disponível para compras na loja é igual a {} reais\n'.format(int(credito)))


def verificar_produto():
    # Itens
    def linha():
        print(('-') * 54)

    linha()
    print('Catálogo de produtos disponíveis na loja 747 Aviation')
    linha()

    lista = ['* Material para PP, R$300', '* Material para PC, R$350', '* Material para PLA, R$500',
             '* Material para CMS, R$150', '* Carta WAC, R$26',
             '* Carta IAC, R$35', '* Computador de voo, R$350', '* CIV, R$50', '* Maquete Boeing 747, R$400',
             '* Painel MPC Boeing 737 NG, R$2800']
    for itens in lista:
        print(itens)

    produtos = ['Material para PP', 'Material para PC', 'Material para PLA', 'Material para CMS', 'Carta WAC',
                'Carta IAC', 'Computador de voo', 'CIV',
                'Maquete Boeing 747', 'Painel MPC Boeing 737 NG']

    # Compra
    contador = 1
    valor_total = 0
    lbldesc = 0
    qtd_produtos = input('\nInforme a quantidade de produtos que você deseja comprar: ')
    while (int(qtd_produtos)) <= 0:
        print('\033[31mInforme um valor válido maior que zero.\033[m')
        qtd_produtos = input('\nInforme a quantidade de produtos que você deseja comprar: ')
        if (int(qtd_produtos)) > 0:
            pass


    while (int(contador) <= int(qtd_produtos)):
        produto = str(input('\nDigite o nome do produto que você deseja comprar: '))

        if produto in produtos:
            valor = input('Informe o preço do produto escolhido: R$')
            while (float(valor) <= 0):
                print('\033[31mValor inválido.\033[m')
                valor = input('Informe o preço do produto escolhido: R$')
                if (float(valor) > 0):
                    pass
            valor_total = (float(valor_total)) + (float(valor))
            limite = (int(credito)) - (float(valor_total))
            if limite < 0:
                print('\033[31mBloqueado para compra. O valor total do(s) produto(s) escolhido(s) está acima do crédito informado.\033[m')
                contador = (int(qtd_produtos))
                exit()
            else:
                print('O seu limite de crédito atualizado é de R$', limite)
            contador = contador + 1
        else:
            print('\033[31mO produto não consta no catálogo da loja.\033[m')

    if (float(valor_total) <= 0.6 * int(credito) + 1):
        print('Liberado!')
        lbldesc = 1
    elif (float(valor_total) > 0.6 * int(credito) + 1 and float(valor_total) < 0.9 * int(credito) + 1):
        print('Liberado para parcelar em até 2 vezes')
        lblbdesc = 1
    elif (float(valor_total) > 0.9 * int(credito) + 1 and float(valor_total) < int(credito) + 1):
        print('Liberado para parcelar em até 3 vezes')
        lbldesc = 1
    else:
        print('\033[31mBloqueado para compra. O valor total do(s) produto(s) escolhido(s) está acima do crédito informado.\033[m')
        lbldesc = 0
        

    #Desconto
    nome = 'Luisa Gavlak Vilares Cordeiro'
    qtd_letras = len(nome)
    primeiro_nome = (nome.split()[0])
    qtd_primeiro_nome = len(primeiro_nome)


    if lbldesc != 0:
        if (float(valor_total)) >= qtd_letras and (float(valor_total)) >= (int(idade)):
            print('\n\033[32mVocê tem um cupom de desconto liberado\033[m')
            valor_desconto = float(valor_total) * int(qtd_primeiro_nome) / 100
            novo_valor = float(valor_total) - float(valor_desconto)
            print('\nO valor com desconto é igual a R$', novo_valor)
    else:
        pass

obter_limite()
verificar_produto()
