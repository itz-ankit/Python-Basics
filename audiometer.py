import numpy as np
import pyaudio

# Constants
sample_rate = 44100  # Samples per second
duration = 1.0       # Duration in seconds
amplitude = 0.5      # Amplitude (0.0 to 1.0)
frequency = 1000     # Frequency in Hz

# Generate the audio signal
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=sample_rate,
    output=True
)

# Play the audio
stream.write(audio_signal.tobytes())

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()
