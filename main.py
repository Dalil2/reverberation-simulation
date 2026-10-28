from fonction_reverberation import reverb
from fonction_affichage import plot_signals

if __name__ == "__main__":
    # Liste des fichiers à traiter
    input_files = ["miaou.wav"]
    ir_files = ["IR2.wav"]
    
    for input_file in input_files:
        for ir_file in ir_files:
            # Nom du fichier de sortie
            output_file = f"{input_file.split('.')[0]}_with_{ir_file.split('.')[0]}.wav"
            
            # Appliquer la réverbération et récupérer les signaux
            x, h, y, sr = reverb(input_file, ir_file, output_file)
            
            # Afficher les signaux
            plot_signals(x, h, y, sr)