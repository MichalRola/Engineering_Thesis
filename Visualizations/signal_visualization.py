import os
import matplotlib.pyplot as plt
import librosa
import ffmpeg_way
import numpy as np

SAMPLING_RATE = 44100


def create_waveform_signal_graph(load, save):
    intervals = ffmpeg_way.detect_silence(load, 1)
    audio_timeseries, sampling_rate = librosa.load(load, sr=SAMPLING_RATE, mono=True)
    signal = audio_timeseries[int(intervals[0][1] * SAMPLING_RATE): int(intervals[1][0] * SAMPLING_RATE)]
    t = len(signal) / sampling_rate
    time = np.linspace(0, t, len(signal))
    signal = signal / signal.max()
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, 'k-')
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.xlim(0, t)
    plt.ylim(-1, 1)
    plt.savefig(os.path.join(save, 'sygnal_po_obrobce.png'))
    plt.show()


if __name__ == "__main__":
    load_path = r'D:\Folders\_Engineering_Thesis\Papers\Images\sygnal_przed_obrobka.wav'
    save_path = r'D:\Folders\_Engineering_Thesis\Papers\Images'

    create_waveform_signal_graph(load_path, save_path)
