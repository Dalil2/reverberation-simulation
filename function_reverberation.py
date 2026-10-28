import numpy as np
import librosa
import scipy.signal as signal
import soundfile as sf


def reverb(input_file, ir_file, output_file):
    """
    Apply reverb to an audio file using an impulse response.

    Arguments:
    input_file  : str -> path to the input audio file
    ir_file     : str -> path to the impulse response (IR) file
    output_file : str -> path to the output audio file

    Returns:
    x, h, y, sr -> input signal, impulse response, output signal, sampling rate
    """
    # Load the input signal
    x, sr = librosa.load(input_file, sr=None, mono=True)

    # Load the impulse response
    h, sr_h = librosa.load(ir_file, sr=None, mono=True)

    # Make sure both signals share the same sampling rate
    if sr != sr_h:
        print(f"Warning: sampling rates differ ({sr} vs {sr_h}), resampling h")
        h = librosa.resample(h, orig_sr=sr_h, target_sr=sr)

    # Convolution (computed via FFT)
    y = signal.fftconvolve(x, h)

    # Normalization
    y = y / np.max(np.abs(y))

    # Save the result
    sf.write(output_file, y, sr)

    print(f"File saved: {output_file}")

    return x, h, y, sr