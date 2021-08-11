#Exercícios:
#1. Armazene uma frase dentro de uma variável e depois exiba a mesma na tela.
frase= "tente fazer esses exercícios"
print("O professor falou" , frase)

#2. Exiba uma mensagem de boas vindas para o usuário de acordo com o valor digitado.
nome  = input ("Digite seu nome")
print("Olá {}, seja bem-vindo!".format(nome))

#3. Crie um script onde exiba o nome da pessoa, e sua data de aniversário formatada.
nome= input("Qual seu nome?")
dia_Nasc= input ("Dia em que nasceu?")
mes_Nasc= input ("Mês em que nasceu?")
ano_Nasc= input ("Ano em que nasceu?")
print("Seu nome é {}, e você nasceu em {}/{}/{} ".format(nome, dia_Nasc, mes_Nasc, ano_Nasc))

#4. Crie um programa que leia dois números e mostre a soma entre eles.
n_Um= int(input("Digite um número"))
n_Dois= int(input("Digite outro número"))
r_Soma= n_Um + n_Dois
print("O resultado da soma de {} + {} é igual a {}".format(n_Um, n_Dois, r_Soma))

#5. Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc.
valor= input("Digite algo")
print("O tipo primitivo desse dado é")
print("Só tem espaços?", valor .isspace())
print("É um número?", valor  .isnumeric())
print("É uma letra?", valor .isalpha())
print("É alfanumérico?", valor .isalnum())
print("É uma letra maiúscula?", valor .isupper())
print("É uma letra minúscula?", valor .islower())
print("É um título?", valor .istitle())

#6. Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo.
numero= int(input ("Digite um número inteiro"))
antecessor= numero - 1
sucessor= numero + 1
print("O número digitado foi {}, seu antecessor é o {}, e seu sucessor é o {}." . format(numero, antecessor, sucessor))

#7. Leia um número, mostre seu dobro, triplo, e raíz quadrada.
numero= int(input("Digite um número inteiro"))
dobro= numero + numero
triplo= numero + numero + numero
raiz_Quadrada= pow(numero, 1/2)
print("O número digitado foi {}, seu dobro é {}, seu triplo {}, e sua raíz quadrada é {}.".format(numero, dobro, triplo, raiz_Quadrada))

#8. Desenvolva um programa que receba duas notas de um aluno e calcule sua média.
nota1= int(input("Digite sua primeira nota"))
nota2= int(input("digite sua segunda nota"))
media= (nota1 + nota2)/2
print("Sua primeira nota foi {}, e sua segunda nota foi {}, a média das duas é {}".format(nota1, nota2, media))

#9. Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.
metros= int(input("Digite um valor em metros, para ser convertido em centímetros e milímitros"))
centimetros= metros * 100
milimitros=  metros * 1000
print("{} metros são {} centímetros e {} milímitros".format(metros, centimetros, milimitros))

#10. Faça um programa que leia um valor, e mostre a sua tabuada do 1 ao 10 na tela.
numero= int(input("De que número você quer a tabuada?"))
n1= numero * 1
n2= numero * 2
n3= numero * 3
n4= numero * 4
n5= numero * 5
n6= numero * 6
n7= numero * 7
n8= numero * 8
n9= numero * 9
n10= numero * 10
print("Essa é a tabuada do {}".format(numero))
print("1 * {} ={}".format(numero, n1))
print("2 * {} ={}".format(numero, n2))
print("3 * {} ={}".format(numero, n3))
print("4 * {} ={}".format(numero, n4))
print("5 * {} ={}".format(numero, n5))
print("6 * {} ={}".format(numero, n6))
print("7 * {} ={}".format(numero, n7))
print("8 * {} ={}".format(numero, n8))
print("9 * {} ={}".format(numero, n9))
print("10 * {} ={}".format(numero, n10))
