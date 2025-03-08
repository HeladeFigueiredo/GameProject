import sched
import time

def exibir_mensagem(mensagem):
    print(mensagem)

#Essa função agenda a execução de um evento repetitivo com base em um intervalo especificado
#O parâmetro scheculer é um objeto responsável por agendar eventos advindo da biblioteca sched
#Intervalo é o tempo em segundos entre a execução do evento
#Mensagem é a mensagem, né diva me ajuda ai
def agendar_evento(scheduler, intervalo, mensagem):
    #scheduler.enter() receber como parâmetros - delay, priority, action, argument=()
    #Essa função agenda o eventos

    #O parâmetro delay é o intervalo
    # Tempo em segundos que o evento deve esperar antes de ser executado

    #O parâmetro priority é o 1
    #Representa a prioridade do evento
    #Quanto menor o número, maior a prioridade

    #Parâmetro action é o agendar_evento
    #É uma função que será executada quando o evento for disparado
    # Aqui ela está sendo chamada recursivamente o que faz o evento se repetir

    #Parâmetro argument é o (scheduler, intervalo, mensagem)
    #É do tipo tupla e são os argumentos que serão passados na função action

    scheduler.enter(intervalo, 1, agendar_evento, (scheduler, intervalo, mensagem))
    exibir_mensagem(mensagem)

#Criação de uma instância do objeto scheduler
#Essa instância pode ser usada para agendar e executar tarefas no futuro

# Time.time é uma função que retorna o tempo atual em segundos desde 01/01/1970
#O scheduler usa para calcular o tempo  de execução dos eventos agendados

#Time.sleep é uma função que pausa a execução do programa por um tempo especificado
#O scheduler usa para esperar até que os eventos agendados sejam executados no momento correto

new_scheduler = sched.scheduler(time.time, time.sleep)

#Agendando um evento
agendar_evento(new_scheduler, 3, 'Essa é a mensagem agendada para cada 3 segundos')

print('Esperando para exibir as mensagens agendadas')

#Essa chamada executa todos os eventos agendados no scheduler de forma síncrona
#Verifica a lista de eventos agendados
#Aguarda o tempo agendado para o evento
#Executa os eventos na ordem respeitando o tempo e as prioridades
#Continua rodando até que todos os eventos tenham sido processados
new_scheduler.run()
