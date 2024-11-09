# Funciones relacionadas con el filtrado

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

import os

#import soundfile

#import matplotlib

PINK_NOISE = os.path.join("data", "pink_noise.wav")
G =  10 ** (3/10)   # Octave frecuency ratio
FR = 1000

def cargarAudio(audio):
    # read(file) -> (rate: int, data: numpy array )
    signal = wavfile.read(audio)

    return signal


def calcMidFrecuencies(b, x): 
    # (b, x) -> fm

    fm = FR * (G ** (x/b))  # Exact mid-band frecuencies [array]

    return fm

def thirdOctaveFilter():

    fs, signal_data = cargarAudio(PINK_NOISE)
    b = 3
    x = np.arange(-16, 14)  # No incluye el último valor
    fm = calcMidFrecuencies(b, x)  # Exact mid-band frecuencies [array]
    fl = fm * (G ** (-1/(2 * b)))
    fh = fm * (G ** (1/(2 * b)))

    N = 6   # Order of the filter
    filtered_signals = np.array([])

    for f_low, f_High in zip(fl, fh):

        sos = butter(N, [f_low, f_High], 'bandpass', False, 'sos', fs)
        filtered_signals =np.append(filtered_signals, sosfilt(sos, signal_data))

    # print(sos)

    print(filtered_signals)

cargarAudio(PINK_NOISE)
thirdOctaveFilter()
