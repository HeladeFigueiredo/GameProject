#Exemplo 1: apenas 1 condição
#Forma tradicional
list_pares_ao_quadrado = []

for num in range(10):
    if num % 2 == 0:
        list_pares_ao_quadrado.append(num*num)


#Usando List Comprehension
list_pares_ao_quadrado = [num*num for num in range(10) if num % 2 == 0]



#Exemplo 2: com 2 condições
#Forma tradicional
list_pares_ao_quadrado2 = []

for num in range(10):
    if num % 2 == 0:
        list_pares_ao_quadrado2.append(num*num)
    else:
        list_pares_ao_quadrado2.append('impar')

#Usando List Comprehension
list_pares_ao_quadrado = [num*num if num % 2 == 0 else 'impar' for num in range(10)]





