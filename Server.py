import pyttsx3
import socket
import sys


engine = pyttsx3.init()

def sys_voice():
    """
    setup for voice welcome message
    """
    voices  = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say("Welcome to  the world of Friends")
    engine.runAndWait()

def socket_creation():
    try:
          s = socket.socket()
          engine.say('Socket created')
          engine.runAndWait()
    except socket.error as err:
         engine.say('Something goes wrong tring again')
         print('Retrying...')
         socket_creation()
         

          

def main():
      sys_voice()
      socket_creation()
main()