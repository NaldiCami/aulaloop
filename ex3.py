numeroSecreto = 42 
tentativa = 1

while tentativa <=3:
    palpite = int(input("Adivinhe o número secreto"))
    if palpite == numeroSecreto:
        print("parabéns, você não é burro")
        break 
else:
    if palpite > numeroSecreto:
        print("Parabéns vc não é burro")
    else:
        if palpite > numeroSecreto:
            print("O número secreto é menor do que ", palpite)
        else:
            print("o número secreto é maior do que ", palpite)
    tentativa += 1 
    
    if tentativa > 3:
        print("Suas tentativas acabaram, vc é burro")