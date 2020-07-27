# prog que calcula a hora aula 

print('+==+'*25)
print()
print('''Seja Bem-vindo(a) ao HORAULA, sua calculadora de hora/aula!
Antes de começarmos leia as instruções de uso:
     (1) - Digite os valores pedidos, aperte enter e espere novas instruções
     (2) - Digite apenas valores inteiros 
           ex: 5,75 você digitará apenas 5
     (3) - Atenção ao que se pede!! Insira horas no lugar de horas e minutos no lugar de minutos!!!
     ''')
print ()
print('+==+'*25)

print ('Insira a quantidade de horas e de minutos dados no mês: ')
horas = int (input('Horas: '))
minutos = int (input('Minutos: '))
print ('Quanto você recebe por hora aula?')
valor = (int (input('R$ ')))
print ('Quantos minutos dura sua hora aula?')
horaula = int (input('Minutos: '))

conversaoParaMinutos = (60*horas) + minutos
conversaoParaUnidadesAula = conversaoParaMinutos/horaula
totalReceber = conversaoParaUnidadesAula * valor

print('+==+'*25)
print()
print (f'Você tem que receber R${totalReceber}')
print()
print('+==+'*25)
