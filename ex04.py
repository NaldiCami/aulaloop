tentativa = 0

while tentativa < 3:
    senha = input("Digite a senha:")
    if senha == "seha123":
        print("Acesso concedido!")
        break
    else: 
        print("Senha incorreta. Tente novamente.")
        tentativa += 1
else:
    print("Você excedeu o número máximo de tantativa.")