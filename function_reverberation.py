import numpy as np
import librosa
import scipy.signal as signal
import soundfile as sf

def reverb(input_file, ir_file, output_file):
    """
    Applique une réverbération à un fichier audio à partir d'une réponse impulsionnelle.
    
    Arguments :
    input_file : str -> chemin du fichier audio d'entrée
    ir_file    : str -> chemin du fichier IR
    output_file: str -> chemin du fichier audio de sortie
    """
    # Chargement du signal d'entrée
    x, sr = librosa.load(input_file, sr=None, mono=True)
    
    # Chargement de la réponse impulsionnelle
    h, sr_h = librosa.load(ir_file, sr=None, mono=True)
    
    # Vérification des fréquences d'échantillonnage
    if sr != sr_h:
        print(f"Attention : les fréquences sont différentes ({sr} vs {sr_h}), on adapte h")
        h = librosa.resample(h, orig_sr=sr_h, target_sr=sr)
    
    # Convolution
    y = signal.fftconvolve(x, h)
    
    # Normalisation
    y = y / np.max(np.abs(y))
    
    # Sauvegarde du résultat
    sf.write(output_file, y, sr)
    
    print(f"Fichier généré : {output_file}")

    return x, h, y, sr