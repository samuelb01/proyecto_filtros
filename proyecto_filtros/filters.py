# Funciones relacionadas con el filtrado

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

import matplotlib.pyplot as plt

import os

#import soundfile


PINK_NOISE = os.path.join("data", "pink_noise_mono_48khz_16bits.wav")
WHITE_NOISE = os.path.join("data", "white_noise_mono_48khz_16bits.wav")
NOMINAL_THIRDOCTAVE_FREC = [25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400,
                             500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000,
                               6300, 8000, 10000, 12500, 16000, 20000]
G =  10 ** (3/10)   # Octave frecuency ratio
FR = 1000


def cargarAudio(audio):
    # read(file) -> (rate: int, data: numpy array )
    fs, data = wavfile.read(audio)

    return fs, data


def calcMidFrecuencies(b, x): 
    # (b, x) -> fm

    fm = FR * (G ** (x/b))  # Exact mid-band frecuencies [array]

    return fm


def calcRMS(filtered_values):

    rms_values = []

    for filtered in filtered_values:
        rms = np.sqrt(np.mean(filtered**2))
        rms_values.append(rms)

    # rms_values = [np.sqrt(np.mean(filtered ** 2)) for filtered in filtered_values]

    return rms_values


def thirdOctaveFilter(audio):

    fs, signal_data = cargarAudio(audio)
    b = 3
    x = np.arange(-16, 14)  # No incluye el último valor
    fm = calcMidFrecuencies(b, x)  # Exact mid-band frecuencies [array]
    fl = fm * (G ** (-1/(2 * b)))
    fh = fm * (G ** (1/(2 * b)))

    N = 6   # Order of the filter
    band_levels = []   # Array con las bandas filtradas

    for f_low, f_High in zip(fl, fh):
        sos = butter(N, [f_low, f_High], 'bandpass', False, 'sos', fs)  # Second Order Sections

        filtered_signal = sosfilt(sos, signal_data)

        rms = np.sqrt(np.mean(filtered_signal**2))
        level = 20 * np.log10(rms)

        band_levels.append(level)


    # Graficar niveles por bandas con barras uniformes
    widths = np.array(fh) - np.array(fl)    # Calcular ancho de las barras en escala logarítmica
    plt.figure(figsize=(10, 6))
    plt.bar(fm, band_levels, width=widths, align='center', color='skyblue', edgecolor='black')
    plt.xscale('log')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Nivel (dB)')
    plt.title('Niveles por bandas de tercios de octava (sin normalizar)')

    # Personalizar el eje X para mostrar todas las frecuencias centrales
    plt.xticks(fm, labels=[f"{int(freq)} Hz" if freq >= 100 else f"{freq:.1f} Hz" for freq in NOMINAL_THIRDOCTAVE_FREC], rotation=90)

    # Agregar la cuadrícula
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()


thirdOctaveFilter(PINK_NOISE)
thirdOctaveFilter(WHITE_NOISE)

