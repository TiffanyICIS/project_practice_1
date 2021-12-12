import soundfile as sf
import math
import matplotlib.pyplot as plotter
from scipy.fft import fft, ifft, rfft, irfft
import numpy as np

filter_frequency_response = [(-0.00108333*x**2 + 0.2525*x - 19.9167) for x in range(0, 100)]
filter_frequency_response += [(2.491*math.cos(0.00377014*x) - 7.53082) for x in range(101, 1000)]
filter_frequency_response += [(-4.65389 - (1/(0.000206691*x))) for x in range(1001, 22051)]
# filter_db = []
# for x in filter_frequency_response:
#     if x == 0:
#         filter_db += [-120]
#     else:
#         if 20*math.log(x, 10) < -120:
#             filter_db += [-120]
#         else:
#             filter_db += [20*math.log(x, 10)]
plotter.title("График 1: Амплитудно-частотная характеристика фильтра для примера")
plotter.xscale("log")
plotter.xlabel("Частота, Гц")
plotter.ylabel("Коэффициент передачи")
plotter.plot(filter_frequency_response)
plotter.show()

ir = irfft(filter_frequency_response)
ir_windowed = ir[:len(ir)//2]
ir_scaled = [x*2 for x in ir_windowed]
plotter.xscale("log")
plotter.plot(ir_windowed)
plotter.show()

# mean = 0
# std = 1
# num_samples = 200000
# samples = np.random.normal(mean, std, size=num_samples)
# plotter.plot(samples)
# plotter.show()

samples1, _ = sf.read('C:\\Users\\super\\Downloads\\soundfile.wav')
samples = np.ravel(samples1)
sv = np.convolve(ir_scaled, samples, mode='full')
plotter.xscale("linear")
plotter.plot(sv)
plotter.show()
sf.write('filtered_sine.wav', sv, 44100)
