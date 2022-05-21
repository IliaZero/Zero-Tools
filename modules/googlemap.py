from pyngrok import ngrok
import os

def generate():
    domain = ngrok.connect()
    print('Take This Domain to Your Target  ===>',domain)
    os.system("php -S localhost:80")
    input()
