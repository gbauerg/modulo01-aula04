#solicita população, de acordo com o bonus, dá um extra.

pontos = int(input("Quantos pontos você obteve até agora? "))

if pontos >= 100:
    pontos = pontos+10
elif pontos >=50:
    pontos = pontos+5
else:
    pontos = pontos

print(f"Você fez {pontos} pontos!")