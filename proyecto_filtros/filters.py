# Funciones relacionadas con el filtrado

import numpy as np
import scipy
from scipy.io import wavfile
from scipy.signal import butter

import os

#import soundfile

#import matplotlib

PINK_NOISE = os.path.join("data", "pink_noise.wav")
G =  10 ** (3/10)   # Octave frecuency ratio
FR = 1000

def cargarAudio(audio):
    # read(file) -> (rate: int, data: numpy array )
    signal = wavfile.read(audio)
    print(signal[0])

    return signal


def calcularFrecuenciasCentrales(b, x): 
    # (b, x) -> fm

    fm = FR * (G ** (x/b))  # Exact mid-band frecuencies [array]

    return fm

def thirdOctaveFilter():

    signal = cargarAudio(PINK_NOISE)
    b = 3
    x = np.arange(-16, 14)  # No incluye el último valor
    fm = calcularFrecuenciasCentrales(b, x)  # Exact mid-band frecuencies [array]
    
    sos = butter(N, Wn, 'bandpass', False, 'sos', )



cargarAudio(PINK_NOISE)
