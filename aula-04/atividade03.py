vendas = float(input("Qual foi o valor das vendas esse mês? "))
salario = float(input("Qual o salário do funcionário? "))

if vendas >= 5000:
    salario = float(salario + 500)

elif vendas >= 3000:
    salario = float(salario + 250)

elif vendas < 3000:
    salario = float(salario)

print(f"O funcionário deve receber R${salario:.2f} esse mês.")