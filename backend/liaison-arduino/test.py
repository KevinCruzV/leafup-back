import pyfirmata
import time

port = '/dev/cu.usbserial-10'  # Windows (à adapter par rapport à votre ordinateur)
board = pyfirmata.Arduino(port)  # Permet d’ouvrir le port associer

temperature_pin = board.get_pin('a:0:A1')  # Permet d’initialiser la broche utilisée
iterator = pyfirmata.util.Iterator(board)  # Permet d’initialiser la liaison entre Python et Arduino
iterator.start()  # Démarrage de la connexion
temperature_pin.enable_reporting()  # Lecture des valeurs de la broche choisie

while temperature_pin.read() is None: var = None # Tant qu’il n’y a pas de valeurs

try:
    while True:  # Boucle infinie
        print("température entre 0 et 1 :", temperature_pin.read())  # On affiche les valeurs lues par la broche
        Celsius = ((temperature_pin.read() * 5 - 0.5) * 100)  # Transforme ces valeurs en Celsius
        print("température en Celsius :", (round(Celsius, 4)))  # Arrondit et affiche la température
        time.sleep(1)  # Fait une pause de 1 seconde entre deux mesures
except:
    temperature_pin.disable_reporting()  # Arrête la lecture de la broche
    board.exit()
