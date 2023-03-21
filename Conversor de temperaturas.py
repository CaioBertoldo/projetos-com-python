# Informar qual escala de temperatura o usuário irá usar

print('------------- CONVERSOR DE TEMPERATURAS ---------------')
print()

escala = input(""" Qual escala de temperatura você irá usar ?
a) Celsius (°C)
b) Fahrenheit (°F)
c) Kelvin (K)
d) Rankine (Ra)
Resposta:   """)



if escala == 'a' or escala == 'Celsius' or escala == '°C' :
    # Informar a temperatura em °C
    temp_C = float(input('Informe a temperatura em °C: '))

    # Mostrar a temperatura em Celsius
    print(f'A temperatura na unidade escolhida é: {temp_C}°C')

    # Converter de Celsius para as outras escalas
    celsius_fahrenheit = (temp_C * (9/5)) + 32
    celsius_kelvin = temp_C + 273.15
    celsius_rankine = (temp_C + 273.15) * (9/5)

    # Mostrar a temperatura de Celsius convertida nas outras escalas
    print('-' * 60)
    print(f'A temperatura {temp_C}°C em Fahrenheit é igual a {celsius_fahrenheit:.2f}°F')
    print(f'A temperatura {temp_C}°C em Kelvin é igual a {celsius_kelvin:.2f} K')
    print(f'A temperatura {temp_C}°C em Rankine é igual a {celsius_rankine:.2f}°Ra')

elif escala == 'b' or escala == 'Fahrenheit' or escala == '°F' or escala == 'F' or escala == 'f':
    # Informar a temperatura em °F
    temp_F = float(input('Informe a temperatura em °F: '))
    
    # Mostrar a temperatura em Fahrenheit
    print(f'A temperatura na unidade escolhida é {temp_F}°F') 

    # Converter para as outras escalas
    Fahrenheit_celsius = (temp_F - 32) * (5/9)
    Fahrenheit_kelvin = (temp_F - 32) * (5/9) + 273.15
    Fahrenheit_rankine = temp_F + 459.67

    # Mostrar a temperatura de Fahrenheit convertida para as outras escalas 
    print('-' * 60)
    print(f'A temperatura {temp_F}°F em Celsius é igual a {Fahrenheit_celsius:.2f}°C')
    print(f'A temperatura {temp_F}°F em Kelvin é igual a {Fahrenheit_kelvin:.2f} K')
    print(f'A temperatura {temp_F}°F em Rankine é igual a {Fahrenheit_rankine:.2f}°Ra')

elif escala == 'c' or escala == 'Kelvin' or escala == 'K' or escala == 'k':
    # Informar a temperatura em K
    temp_k = float(input("Informe a temperatura em K: "))

    # Mostrar a temperatura em Kelvin
    print(f'A temperatura na unidade escolhida é {temp_k} K')

    # Converter para as outras escalas
    kelvin_celsius = temp_k - 273.15
    kelvin_Fahrenheit = (temp_k - 273.15) * (9/5) + 32
    kelvin_rankine = temp_k * (9/5)

    # Mostrar a temperatura de Kelvin convertida para as outras escalas 
    print('-' * 60)
    print(f'A temperatura {temp_k} K em Celsius é igual a {kelvin_celsius:.2f}°C')
    print(f'A temperatutra {temp_k} K em Fahrenheit é igual a {kelvin_Fahrenheit:.2f}°F')
    print(f'A temperatura {temp_k} K em Rankine é igual a {kelvin_rankine:.2f}°Ra')

elif escala == 'd' or escala == 'Rankine' or escala == '°Ra' or escala == 'R' or escala == 'r':
    # Informar a temperatura em Rankine
    temp_R = float(input('Informe a temperatura em °Ra: '))

    # Mostrar a temperatura em Rankine
    print(f'A temperatura na unidade escolhida é {temp_R}°Ra')

    # Converter para as outras escalas 
    rankine_celsius = (temp_R - 491.67) * (5/9)
    rankine_Fahrenheit = temp_R - 459.67
    rankine_kelvin = temp_R * (5/9)

    # Mostrar a temperatura de Rankine convertida para as outras escalas
    print('-' * 60)
    print(f'A temperatura {temp_R}°Ra em Celsius é igual a {rankine_celsius:.2f}°C')
    print(f'A temperatura {temp_R}°Ra em Fahrenheit é igual a {rankine_Fahrenheit:.2f}°F')
    print(f'A temperatura {temp_R}°Ra em Kelvin é igual a {rankine_kelvin:.2f} K')

