#calcular media bimestral dos alunos (teste e prova)
#criar algoritmo que solicite as duas notas, calcule a media e de o resultado final

nota_teste = float(input("Qual a nota do teste? "))
nota_prova = float(input("Qual a nota da prova? "))

calc_media = float(nota_teste + nota_prova)/2

print(f"A média bimestral do aluno é {calc_media:.2f}.")