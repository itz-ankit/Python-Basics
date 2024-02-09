import pygame
import pyaudio
import wave

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = "recorded_voice.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Start recording
print("Recording...")

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=1024)
frames = []

for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
    data = stream.read(1024)
    frames.append(data)

# Stop recording
print("Finished recording.")

stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

# Play back the recorded audio (as a simple example)

pygame.mixer.init()
pygame.mixer.music.load(OUTPUT_FILENAME)
pygame.mixer.music.play()

input("Press Enter to exit...")

# Clean up
pygame.mixer.quit()
