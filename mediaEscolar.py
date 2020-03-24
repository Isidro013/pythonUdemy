print("Calcúlo de média escolar.")
print("")
nome = input("Escreva seu nome: ")
materia = input("Entre com o nome da matéria: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4
if media > 7:
    print("{}, sua nota na matéria {} foi {} e você está APROVADO!"
    .format(nome, materia, media))
else:
    print("{}, sua nota na matéria {} foi {} e você está REPROVADO"
    .format(nome, materia, media))
