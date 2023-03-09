tipo = input("Digite o tipo de número que deseja imprimir (Par ou impar): ")
for i in range(1,11):
    tipo = tipo.upper()
    if tipo == "par" and i%2==0:
        print(i)
    elif tipo == "impar" and i%2!=0:
        print(!)