#Projeto Final (Avaliação do 4º BIMESTRE)

print ("Olá caro estudante! Apresento-lhe esse OA que irá te ajudar na área de notação científica em matemática!\n")
print ("Mas antes, você sabe o que é um OA?")
escolha = str(input("(S para sim e N para não) "))
print()

if escolha == 'S': print ("Ah, legal. Então vamos direto ao conteúdo!\n")

else:
    print(''' Um Objeto de aprendizagem (OA) é uma unidade de instrução/ensino reutilizável. 
        De acordo com o Learning Objects Metadata Workgroup, objetos de aprendizagem
        podem ser definidos por "qualquer entidade, digital ou não digital, que possa ser
        utilizada, reutilizada ou referenciada durante o aprendizado suportado por tecnologias".\n''')
    print(" Depois dessa breve explicação, vamos ao conteúdo!\n")
    
proximo = str(input("(Digite C para continuar) "))

print(" \nO que é uma notação científica? ")
print('''Notação científica é uma maneira de representar números de forma simplificada.
    Pode ser utilizado para abreviar tanto números muito grandes, como números muito
    pequenos. O segredo para resolver uma notação científica é traduzir o número para uma
    potência de base 10 (10^x).''')
print("______________________________\n")

proximo = str(input("(Digite C para continuar) "))

print("______________________________\n")
print(" Como transformar um número em notação científica? ") #print("******************")
print("\nSiga os seguintes passos:\n")
print('''1- Escreva o número na forma decimal. Só um algarismo diferente de 0 deve ficar
    antes da vírgula, ou seja, deve ser um número real entre 1 e 10.
    2- Conte quantas casas decimais a vírgula andou.
    3- Coloque esse número de casas como expoente do 10. É preciso ter atenção
    quando se anda com a vírgula: se o número diminuir, o expoente será positivo. Se o
    número aumentar, o expoente será negativo.
    Para entender melhor, veja o exemplo com o número 18000000:
    1- Levar a vírgula entre os números 1 e 8, para ficar com um número entre 1 e 10.
    2- Contar quantas casas decimais a vírgula foi mexida para chegar nessa posição. Nesse
    exemplo foram 7 casas.
    3- Colocar o número 7 como potência de 10.
    Esse é resultado do número 18000 escrito como notação científica:
    18000000 = 1,8 . 10^7.\n''')
print("Segue uma tabela abaixo com mais exemplos: ")
print('''
    ---------------------
    |10^1= | 10 |
    ---------------------
    |10^2= | 100 |
    ---------------------
    |10^3= | 1000 |
    ---------------------
    |10^4= | 10000 |
    ---------------------
    |10^5= | 100000 |
    ---------------------
    |10^6= | 1000000 |
    ---------------------
    |10^7= | 10000000 |
    ---------------------
    |10^8= | 100000000 |
    ---------------------
    |10^9= | 1000000000 |
    ---------------------
    |10^10=| 10000000000|
    --------------------- ''')
print("Seguindo o exemplo acima, faça duas notações para fixar o assunto: \n")

matriz = [[0, 0], [0, 0]]

for l in range(0,2):
    for c in range(0,2): matriz[l][c] = str(input("Digite um valor para a posição [{l}, {c}]: "))
    print('-='*30)
for l in range(0,2):
    for c in range(0,2):
        print(f'[{matriz[l][c]:^5}]', end='')
print()
print("\nQuer fazer mais duas notações? \n")
r = str(input("(S para sim e N para não) ")).upper()
if r =='S':
    while r == 'S':
        matriz = [[0, 0], [0, 0]]
    for l in range(0,2):
        for c in range(0,2):
            matriz[l][c] = str(input("Digite um valor para a posição [{l}, {c}]: "))
            print('-='*30)
    for l in range(0,2):
        for c in range(0,2):
            print(f'[{matriz[l][c]:^5}]', end= '')
            print("\nQuer fazer mais duas notações? \n")
            r = str(input("(S para sim e N para não) ")).upper()
else:
    print()
    print('''\n\nAh, legal, chegamos ao final desse OA! \nQuaisquer dúvida que venha a surgir,
    entre em contato para que possamos sanar.''')
    texto = 'Projeto desenvolvido por Cayo Henrique. Instituto Federal de ALagoas.'
    print ('\n\n', texto[0:40])
    print ('\n', texto[40], texto[50], texto[61], texto[62])
    print ("\n\nContato: \n\n Email: inst.ifal.edu.br\n Telefone: (82) 9 9999-0000")