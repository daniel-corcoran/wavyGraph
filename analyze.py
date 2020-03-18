from scipy.io import wavfile
import numpy as np
fs, data = wavfile.read('Waltz-music-loop.wav')

data = data.astype(np.float32)
data= (data / np.max(np.abs(data)))
data -= np.mean(data)
def yield_data():
    for i in data:
        yield i
for i in data:
    data = np.abs(i)
