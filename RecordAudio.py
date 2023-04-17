import pyaudio
import lameenc
import wave
import io

# Record audio
def record_audio(seconds):
    RATE = 44100
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return b''.join(frames)

# Save audio as MP3
def save_audio_as_mp3(audio_data, file_name):
    RATE = 44100
    CHANNELS = 1

    # Convert audio data to MP3
    encoder = lameenc.Encoder()
    encoder.set_in_sample_rate(RATE)
    encoder.set_channels(CHANNELS)
    encoder.set_bit_rate(128)
    encoder.set_quality(2)  # 2-highest, 7-fastest
    mp3_data = encoder.encode(audio_data) + encoder.flush()

    # Save MP3 data to a file
    with open(file_name, 'wb') as f:
        f.write(mp3_data)

# Main function
def main():
    audio_data = record_audio(5)
    save_audio_as_mp3(audio_data, 'output.mp3')

if __name__ == '__main__':
    main()

