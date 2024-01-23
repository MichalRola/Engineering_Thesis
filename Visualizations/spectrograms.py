import os
import matplotlib.pyplot as plt
import librosa
import ffmpeg_way
import numpy as np

SAMPLING_RATE = 44100


def create_spectrograms(load, save):
    intervals = ffmpeg_way.detect_silence(load, 1)
    audio_timeseries, sampling_rate = librosa.load(load, sr=SAMPLING_RATE, mono=True)
    signal = audio_timeseries[int(intervals[0][1] * SAMPLING_RATE): int(intervals[1][0] * SAMPLING_RATE)]

    melspectrogram = librosa.feature.melspectrogram(y=signal, sr=sampling_rate, htk=0)
    melspectrogram = librosa.power_to_db(melspectrogram)
    plt.imsave(os.path.join(save, "Slaney.png"), melspectrogram, cmap='gray')

    melspectrogram = librosa.feature.melspectrogram(y=signal, sr=sampling_rate, htk=1)
    melspectrogram = librosa.power_to_db(melspectrogram)
    plt.imsave(os.path.join(save, "HTK.png"), melspectrogram, cmap='gray')

    spectrogram = librosa.stft(signal)
    spectrogram = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
    plt.imsave(os.path.join(save, "control.png"), spectrogram, cmap='gray')


if __name__ == "__main__":
    load_path = r"D:\Folders\_Engineering_Thesis\Papers\Images\sygnal_przed_obrobka.wav"
    save_path = r"D:\Folders\_Engineering_Thesis\Papers\Images"

    create_spectrograms(load_path, save_path)
