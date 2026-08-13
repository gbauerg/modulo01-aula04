#recebe tempo de casa, salario, setor e calcula novo salario
#setor A +3 anos 18% reajuste
#resto 9%
#valor do aumento, percentual de reajuste e salario final

tempo = int(input("Qual o tempo de casa do funcionário? "))
salario = float(input("Qual o salário atual dele? "))
setor = input("Qual o setor do funcionário? ").upper()

if setor == "A" and tempo >=3:
    aumento = salario*0.18
    reajuste = "18%"

else:
    aumento = salario*0.09
    reajuste = "9%"


salario_final = salario + aumento

print(f"O aumento foi de R${aumento:.2f}.")
print(f"O salário a receber dele é R${salario_final}.")
print(f"O aumento foi de {salario_final-salario}, equivalente a {reajuste}.")

