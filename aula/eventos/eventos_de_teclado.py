import keyboard

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN: #se o meu tipo de evento for do tipo tecla pressionada
        print(f'A tecla pressionada foi: {event.name}')
        if event.name == 'a': #Captura qual tecla foi teclada
            print('Foi teclado a letra A de amor S2')


keyboard.on_press(on_key_event) #Quando uma tecla for pressionada, chame essa função
# Isso é um hook (gancho) - quando uma função chama outra função

#O código a seguir é para manter o programa executando para capturar o evento de teclado indefinidamente
try:
    while True:
        pass
except KeyboardInterrupt: #pode ser causado com CTRL + F2
    print('Programa terminado')