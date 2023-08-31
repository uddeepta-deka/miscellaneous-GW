import numpy as np
import matplotlib.pyplot as plt

# Parameters for the pulse profile
period = 1.0  # Period of the pulsar in seconds
pulse_duration = 0.1  # Duration of the pulse in seconds
sampling_rate = 1000  # Number of samples per second
pulse_std = pulse_duration / 4  # Standard deviation of the Gaussian pulse

n_profiles = 5
# Generate time axis
t = np.linspace(0,n_profiles* period, int(n_profiles*period * sampling_rate), endpoint=False)

# Generate pulse profile
pulse_profile = np.exp(-0.5 * ((t % period - 0.5 * period) / pulse_std) ** 2)
pulse_fold = np.exp(-0.5 * ((t[200:1000]%period - 0.5* period)/pulse_std)**2)
# Plotting
plt.figure(figsize=(8, 3))
plt.plot(t, pulse_profile, c='#fca311',ls='--', label='model')
plt.plot(t[200:1000], pulse_fold, c='r')
plt.plot(t[-701:-1], pulse_fold[:-100], c='r', label='folded pulse at session i')
plt.xlabel('Time of arrival')
plt.ylabel('Intensity')
plt.xticks([])
plt.yticks([])
plt.legend(frameon=False, loc='best')
plt.savefig('psr.png',transparent=True, bbox_inches='tight', dpi=200)
plt.show()

