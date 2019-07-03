import numpy as np
import matplotlib.pyplot as plt

t = np.arange(128)


sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])

print("hàm này biến đổi mảng 1 chiều thành chuỗi fourier: " + "\n", sp)

print("hàm này biến đổi mảng 1 chiều thành chuỗi fourier nhưng đưa về chu kì: " + "\n", freq)
