import pyttsx3
import socket


engine = pyttsx3.init()

def sys_voice():
    """
    setup for voice welcome message
    """
    voices  = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say("Welcome to the chat bros")
    engine.runAndWait()
    

def socket_creation():
    try:
          global s
          s = socket.socket()
          engine.say('Socket created')
          engine.runAndWait()
    except socket.error as er:
         engine.say('Something goes wrong trying again')
         print('Retrying...')
         socket_creation()

def binding():
     try:
          global host          
          global port
          host = "localhost"
          port = 9999
          s.bind((host,port))
          engine.say('binding port ')
          engine.runAndWait()
          print('Binding ...')
          s.listen(5)
     except socket.error as er:
          engine.say('binding error, trying again')
          engine.runAndWait()
          print('Trying again...')
          binding()

def accepting():
     try:
          # Here connection is a client socket
          connection,address = s.accept()
          print(f'Connection done IP {address[0]} Port {address[1]} ')
          engine.say(f'Connection done')
          engine.runAndWait()
          sending_data(connection)
     except socket.error as er:
          engine.say('Something goes wrong while accepting connection')
          engine.runAndWait()
          accepting()
      

def sending_data(connection):
     try:
          while True:
               text = input()
               if text == 'exit':
                    connection.close()
                    engine.say('exiting thank you')
                    raise SystemExit('thank you ')
               if len(str.encode(text)) > 0:
                    connection.send(str.encode(text))
               print(connection.recv(1024).decode())
     except socket.error as er:
          engine.say('Error in sending message ')
          print(str(er))
          engine.runAndWait()

          
          


          

def main():
      sys_voice()
      socket_creation()
      binding()
      accepting()
main()