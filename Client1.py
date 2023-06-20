import pyttsx3
import socket

engine = pyttsx3.init()
def sys_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say('Welcome to the chat bros')
    engine.runAndWait()


def socket_creating():
    global s
    try:
        s = socket.socket()
        engine.say('sockit created ')
        engine.runAndWait()
    except socket.error as er:
        engine.say('Something goes wrong retrying...')
        engine.runAndWait()
        print('Something goes wrong ' + str(er))
        socket_creating()

def connecting_server():
    try:
        s.connect(('localhost',9999))
        engine.say('Connection completed')
        engine.runAndWait()
    except socket.error as er:
        engine.say('Error in connection')
        engine.runAndWait()
        print('Error in Connection' + str(er))

def sending_data():
    while True:
        text = input()
        if text == 'exit':
            s.close()
            engine.say('Exiting, thank you')
            engine.runAndWait()
            raise SystemExit('All done thank you')
        s.send(str.encode(text))
        print(s.recv(1024).decode('utf-8'))

def main():
    sys_voice()
    socket_creating()
    connecting_server()
    sending_data()

main()