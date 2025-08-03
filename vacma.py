import time
from pynput import keyboard
import threading
import subprocess
import notify2
import os

duree_max_appui=5
duree_inactivite=20
duree_alarme=5
ctrl_appuye=False
dernier_appui=time.time()
alarme_active=False
notify2.init("VACMA")

def jouer_bip():
    os.system('paplay /usr/share/sounds/freedesktop/stereo/dialog-warning.oga')
    os.system('paplay /usr/share/sounds/freedesktop/stereo/device-added.oga')
    os.system('paplay /usr/share/sounds/freedesktop/stereo/device-removed.oga')
def verrouiller_ecran():subprocess.run(["loginctl","lock-session"])
def afficher_notification(message):
    notify2.Notification("VACMA",message).show()
    jouer_bip()
def quand_touche_pressee(touche):
    global ctrl_appuye,dernier_appui,alarme_active
    if touche==keyboard.Key.ctrl_l:
        ctrl_appuye=True
        dernier_appui=time.time()
        if alarme_active:alarme_active=False
def quand_touche_relachee(touche):
    global ctrl_appuye
    if touche==keyboard.Key.ctrl_l:ctrl_appuye=False
def surveiller_vigilance():
    global ctrl_appuye,dernier_appui,alarme_active
    while True:
        temps_actuel=time.time()
        duree_appui=temps_actuel-dernier_appui
        if ctrl_appuye and duree_appui>duree_max_appui and not alarme_active:
            afficher_notification("Relâchez Ctrl gauche !")
            alarme_active=True
            time.sleep(duree_alarme)
            if ctrl_appuye and (time.time()-dernier_appui>duree_max_appui):verrouiller_ecran()
        elif not ctrl_appuye and duree_appui>duree_inactivite and not alarme_active:
            afficher_notification("Appuyez sur Ctrl gauche !")
            alarme_active=True
            time.sleep(duree_alarme)
            if not ctrl_appuye and (time.time()-dernier_appui>duree_inactivite):verrouiller_ecran()
        time.sleep(0.1)

listener=keyboard.Listener(on_press=quand_touche_pressee,on_release=quand_touche_relachee)
listener.start()
thread_vigilance=threading.Thread(target=surveiller_vigilance,daemon=True)
thread_vigilance.start()
print("VACMA active - Ctrl gauche pour confirmer, Ctrl+C pour quitter.")

try:
    while True:time.sleep(1)
except KeyboardInterrupt:listener.stop()
