import sys

# --- DADOS GERAIS ---
movies = ["Titanic", "Thor", "Pânico", "Barbie", "Oppenheimer"]
preco_pipoca = 10

def menu_principal():
    print("Sistema de Autoatendimento: CineMaster 3000\n")
    return input("""Caso queira comprar um ingresso, digite 1.
Caso queira validar um ingresso comprado em outra plataforma, digite 2: """)

def identificacao():
    global name, age
    name = input("Para iniciar seu cadastro, digite seu nome completo: ").strip().title()
    try:
        age = int(input("Digite sua idade: "))
        print("Cadastro realizado com sucesso!\n")
    except ValueError:
        print("[ERRO] Utilize apenas números para a idade.")
        sys.exit()

def escolha_filme():
    global pick
    print("--- LISTA DE FILMES EM CARTAZ ---")
    for mv in movies:
        print(f"- {mv}")
    print() 

    while True:
        pick = input("Para qual sessão deseja adquirir ingresso? ").title().strip()
        pick = pick.replace("Panico", "Pânico") 

        if pick not in movies:
            print("Erro: Filme não encontrado. Verifique a grafia e tente novamente.")
        elif pick == "Pânico" and age < 18:
            print("Classificação indicativa não permitida. Escolha outro filme.")
        else:
            print(f"Sucesso! Ingresso para {pick} adicionado ao carrinho.")
            break

def escolha_lanche():
    global tem_pipoca
    tem_pipoca = False 

    while True:
        pipoca = input("\nVocê deseja acrescentar pipoca (R$ 10.00)? [S]/[N]: ").lower().strip()
        
        if pipoca in ("s", "sim"):
            tem_pipoca = True
            print("Pipoca adicionada!")
            break
        elif pipoca in ("n", "não", "nao"):
            print("Sem pipoca.")
            break
        else:
            print("Opção inválida.")

def calcular_total():
    global ingresso, lanche, total

    ingresso = 0
    if age < 18:
        ingresso = 15.50
    else:
        ingresso = 30
    
    lanche = 0
    if tem_pipoca:
        lanche = preco_pipoca

    total = ingresso + lanche

def pagamento():
    global total, pay, pagamento_aprovado, numero_cartao

    print(f"\n------ PAGAMENTO --------")
    print(f"Subtotal da compra: R$ {total:.2f}")
    
    pay = input("Escolha a forma de pagamento (PIX, Boleto ou Cartão): ").lower().strip()
    pagamento_aprovado = False 

    if pay in ("pix", "boleto"):
        sys_out = input("""
        Sistema fora de área: somente pagamentos via Cartão de Crédito estão disponíveis.
        Deseja continuar? [S/N]: """).lower().strip()
        
        if sys_out in ("s", "sim"):
            print(f"\nO valor atual é R$ {total:.2f}")
            print("Como pedido de desculpas, liberamos um cupom de 10% de desconto!")
            
            while True:
                cupom = input("Para validá-lo, digite 'CINEMA10': ").upper().strip()
                if cupom == "CINEMA10":
                    print("Cupom validado com sucesso!\n")
                    total = total * 0.90
                    pay = "cartão"
                    break
                else:
                    print("Cupom inválido.")
        else:
            print("Operação cancelada.")
            sys.exit()

    if pay in ("cartão", "cartao"):
        print("Pagamento no cartão selecionado.")
        titular = input("Digite o nome do titular: ").strip().upper()
        
        while True:
            numero_cartao = input("Insira os 16 dígitos do cartão (apenas números): ")
            if len(numero_cartao) == 16 and numero_cartao.isdigit():
                validade = input("Data de validade: ")
                cvv = input("CVV: ")
                break
            else: 
                print("Número inválido. Tente novamente.")
        
        pagamento_aprovado = True

def recibo():
    if pagamento_aprovado:
        digito_cartao = numero_cartao[-4:]
        
        print("\nFinalizando......")
        print("...................\n")
        
        # Note que colei o texto na esquerda, ignorando a indentação do def
        print(f"""========================================
           CINEMASTER 3000
         Comprovante de Venda
========================================
 CLIENTE: {name}
 FILME:   {pick}
----------------------------------------
DESCRIÇÃO:
1x Ingresso ....... R$ {ingresso:.2f}
1x Pipoca ......... R$ {lanche:.2f}
----------------------------------------
VALOR TOTAL ....... R$ {total:.2f}

PAGAMENTO:
Cartão de Crédito: ****.****.{digito_cartao}
Status: APROVADO
========================================""")

def validar_ingresso():
    while True: 
        code = input(
            "Por favor, insira o código presente no voucher digital que você recebeu, sem traço. Ex: A7X202 "
        ).strip().upper()
        if len(code) == 6:
            print("Código validado com sucesso!")
            break
        else:
            print("Código inválido. Tente novamente.")

# ==========================
# PROGRAMA PRINCIPAL
# ==========================

acess = menu_principal()

if acess == "1":
    identificacao()
    escolha_filme()
    escolha_lanche()
    calcular_total()
    pagamento()
    recibo()

elif acess == "2":
    validar_ingresso()
