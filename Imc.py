def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso Normal"
    elif 18.5 <= imc < 25:
        return "Peso Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau 1"
    elif 35 <= imc < 40:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3 ou Mórbida"

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificar_imc(imc)}")
