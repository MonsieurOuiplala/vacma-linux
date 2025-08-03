# vacma-linux

**Veille Automatique à Contrôle de Maintien d'Appui**

# Lancer
Exécuter ``vacma.py``

Ctrl gauche = confirmation vigilance

# Configuration (dans le script)
duree_max_appui=5    # Seuil maintien touche (en secondes)

duree_inactivite=20  # Seuil inactivité (en secondes)

duree_alarme=5       # Délai verrouillage (en secondes)

# Fonctionnalités

- Double seuil : appui long OU inactivité → alerte
- Bip sonore + notification non intrusive
- Verrouillage automatique de l'écran si non-réponse

# Fonctionne avec...

Langage : Python 3  
Dépendances : pynput, notify2

# Notes

Si les notifications ne fonctionnent pas :
``sudo apt install python3-notify2 pulseaudio-utils``

Vous pouvez personnaliser la notification sonore en modifiant jouer_bip()
