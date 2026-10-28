from function_reverberation import reverb
from function_signal_display import plot_signals

if __name__ == "__main__":
    # Files to process
    input_files = ["claps.wav"]
    ir_files = ["IR_forest.wav"]

    for input_file in input_files:
        for ir_file in ir_files:
            # Output file name
            output_file = f"{input_file.split('.')[0]}_with_{ir_file.split('.')[0]}.wav"

            # Apply the reverb and get the signals back
            x, h, y, sr = reverb(input_file, ir_file, output_file)

            # Plot the signals
            plot_signals(x, h, y, sr)
