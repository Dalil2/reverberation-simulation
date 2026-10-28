import matplotlib.pyplot as plt
import numpy as np


def plot_signals(x, h, y, sr):
    """
    Affiche les signaux audio : entrée, réponse impulsionnelle et sortie.
    
    Arguments :
    x  : array -> signal d'entrée
    h  : array -> réponse impulsionnelle
    y  : array -> signal de sortie
    sr : int -> fréquence d'échantillonnage
    """
    # Création du temps (en secondes)
    t_x = np.arange(len(x)) / sr
    t_h = np.arange(len(h)) / sr
    t_y = np.arange(len(y)) / sr
    
    # Création des sous-graphes
    plt.figure(figsize=(12, 6))

    # Signal d'entrée
    plt.subplot(3, 1, 1)
    plt.plot(t_x, x)
    plt.title("Signal d'entrée")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    
    # Réponse impulsionnelle
    plt.subplot(3, 1, 2)
    plt.plot(t_h, h)
    plt.title("Réponse impulsionnelle")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    
    # Signal de sortie
    plt.subplot(3, 1, 3)
    plt.plot(t_y, y)
    plt.title("Signal de sortie après réverbération")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    
    # Affichage des graphes
    plt.tight_layout()
    plt.show()