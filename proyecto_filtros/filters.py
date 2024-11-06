# Funciones relacionadas con el filtrado

import numpy as np
import scipy
import scipy.io
import scipy.signal
#import soundfile

#import matplotlib


def cargarAudio():
    signal = scipy.io.wavfile.read('../data/pink_noise.wav')
    print(type(signal))


cargarAudio()