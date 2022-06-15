import time

estoque = {'Coxinha': '20 unidades', 'Croassaint': '10 unidades', 'Pão de queijo': '30 unidades',
           'Pão de batata': '15 unidades', 'Torta de frango c/ catupiry': '5 unidades'}

def Visualizar(): #primeira função
    print(estoque)
    print('Espere 3 segundos para voltar ao menu')
    time.sleep(3.0)


def Procurar(): #segunda função
    p = input('Digite o nome do produto pelo o qual você busca: ')
    print(estoque.get(p, "Produto não cadastrado"))
    print('Você voltará ao menu principal em 3 segundos')
    time.sleep(3.0)


def Adicionar(): #terceira função
    p = input('Digite o produto que sera cadastrado: ')
    q = input('Digite a quantidade do produto que sera cadastrado: ')
    estoque[p] = q
    print('Cadastro realizado com sucesso! \n', estoque)
    print('Você voltará ao menu principal em 3 segundos')
    time.sleep(3.0)


def alterar(): #quarta função
    qtd = input('Digite o nome do prudoto você deseja alterar a quantidade: ')
    if qtd in estoque:
        newqtd = input('Digite a quantidade restante: ')
        estoque[qtd] = newqtd
        print('Quantidade alterada com sucesso \n')
        print('Você voltará ao menu principal em 3 segundos')
        time.sleep(3.0)


def pedido(): #quinta função

    print(estoque)
    op = 0
    conta = 0
    pedido = []
    while (op != ""):
        op = str(input("Aperte enter para finalizar \n O que você deseja?"))
        if op == '1':
            pedido.append("Coxinha")
            conta += 2.0
        if op == '2':
            pedido.append("Croassaint")
            conta += 3.5
        if op == '3':
            pedido.append("Pão de queijo")
            conta += 2.5
        if op == '4':
            pedido.append("Pão de batata")
            conta += 2.5
        if op == '5':
            pedido.append("Torta de frango c/ catupiry")
            conta += 4.0

    print(pedido, "Valor total:", 'R$',conta)
    print('Você voltará ao menu principal em 3 segundos')
    time.sleep(3.0)


def endereco(): #sexta função
    rua = str(input("Qual o nome da sua rua? "))
    num = str(input("Qual o numero? "))
    if rua and num != rua and num:
        print("Sua compra será entregue na rua", rua, "Nº", num, "em 30 minutos")
    else:
        print("Endereço invalido")
        print("Você voltará ao menu principal em 3 segundos")
    time.sleep(3.0)


def feedback(): #sétima função
    print("Que nota você da para nosso atendimento?" '\n'
          "5 - Excelente" '\n'
          "4 - Muito bom" '\n'
          "3 - Bom"       '\n'
          "2 - Ruim"      '\n'
          "1 - Pessimo"   '\n'
          )

    quali = 0
    quali < 6
    quali = int(input("Qual o numero? "))

    if quali == 5:
        print("Obriago pelo feedback!!")
    elif quali == 4:
        print("Agradecemos pela preferencia!")
    elif quali == 3:
        print("Obrigado pela resposta. Vamos melhorar ainda mais nosso serviço!")
    elif quali == 2:
        print("Desculpa se não atendemos as suas expectativas ):")
    elif quali == 1:
        print("Vamos melhorar nosso serviço!!")
    print("Você voltará ao menu principal em 3 segundos")
    time.sleep(3.0)

def sair(): #oitava função
    ""


e = 0

while e != 8:
    e = float(input(
            '\n'
            'Selecione a opção desejada: \n'
            '\n'

            'Visualizar estoque                    1 \n'
            'Procurar no estoque                   2 \n'
            'Adicionar produto                     3 \n'
            'Alterar quantidade do produto         4 \n'
            'Pedido para entregar                  5 \n'      
            'Endereço para entrega                 6 \n'
            'Feedback da compra                    7 \n'
            'Sair                                  8 \n'
            '\n'))

    if e == 1:
            Visualizar()

    elif e == 2:
            Procurar()

    elif e == 3:
            Adicionar()

    elif e == 4:
            alterar()

    elif e == 5:
            pedido()

    elif e == 6:
            endereco()

    elif e == 7:
            feedback()

    elif e == 8:
            sair()


