print("Calculadora simples do 'Marcos'")

numero1 = float(input('Digite um número\n'))
numero2 = float(input('Digite outro número\n'))

tipo_da_multiplicacao = str(input('Digite aqui qual a multiplicação o sr deseja realizar\n'))

if(tipo_da_multiplicacao == "+"):
    valor = numero1 + numero2
    print("Resultado: ", valor)

elif(tipo_da_multiplicacao == "-"):
    valor = numero1 - numero2
    print("Resultado: ", valor)

elif(tipo_da_multiplicacao == "*"):
    valor = numero1 * numero2
    print("Resultado: ", valor)

elif(tipo_da_multiplicacao == "/"):
    valor = numero1 / numero2
    print("O Resultado: ", valor)

elif(tipo_da_multiplicacao == "%"):
    valor = numero1 % numero2
    print("O Resultado é: " , valor)

elif(tipo_da_multiplicacao == "**"):
    valor = numero1 ** numero2
    print("O Resultado é: ", valor)
