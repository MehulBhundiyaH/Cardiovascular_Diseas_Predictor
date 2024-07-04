# # # Code for Signal_view and Simple Denoise



# # import serial
# # import time
# # import matplotlib.pyplot as plt
# # import numpy as np

# # # Establish serial connection
# # ser = serial.Serial('COM9', 9600)  # Change 'COM5' to the appropriate port and 9600 to the baud rate of your device

# # # Define list to store data
# # data_list = []

# # try:
# #     while True:
# #         # Read data from serial port
# #         line = ser.readline().decode().strip()
        
# #         # Check if the line is not empty
# #         if line:
# #             try:
# #                 data_point = int(line)
# #                 data_list.append(data_point)
# #                 print("Received:", data_point)
# #             except ValueError:
# #                 print("Invalid data received:", line)

# # except KeyboardInterrupt:
# #     print("Interrupted")

# # finally:
# #     # Close serial port
# #     ser.close()

# # # Print the collected data
# # data_list = np.array(data_list)

# # def moving_average_filter(data, window_size):
# #     """Apply moving average filter to the data."""
# #     cumsum = np.cumsum(data, dtype=float)
# #     cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
# #     return cumsum[window_size - 1:] / window_size

# # # Generate example audio data (replace this with your actual data)
# # # For demonstration purposes, we generate a sine wave with added noise
# # t = np.linspace(0, 1, len(data_list))

# # # Apply moving average filter
# # window_size = 50
# # denoised_data = moving_average_filter(data_list, window_size)

# # # Plot original and denoised data
# # plt.figure(figsize=(10, 6))
# # plt.plot(t, data_list, label='Original Audio')
# # plt.plot(t[window_size - 1:], denoised_data, label='Denoised Audio')
# # plt.title('Original vs. Denoised Audio')
# # plt.xlabel('Time')
# # plt.ylabel('Amplitude')
# # plt.legend()
# # plt.show()






# import serial
# import time
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.io.wavfile import write


# # Establish serial connection
# ser = serial.Serial('COM9', 9600)  # Change 'COM5' to the appropriate port and 9600 to the baud rate of your device

# # Define list to store data
# data_list = []

# try:
#     while True:
#         # Read data from serial port
#         line = ser.readline().decode().strip()
        
#         # Check if the line is not empty
#         if line:
#             try:
#                 data_point = int(line)
#                 data_list.append(data_point)
#                 print("Received:", data_point)
#             except ValueError:
#                 print("Invalid data received:", line)

# except KeyboardInterrupt:
#     print("Interrupted")

# finally:
#     # Close serial port
#     ser.close()

# # Convert the collected data to a NumPy array
# data_array = np.array(data_list)

# # Print the collected data array
# print("Data Array:", data_array)

# # Define function to apply moving average filter
# def moving_average_filter(data, window_size):
#     """Apply moving average filter to the data."""
#     cumsum = np.cumsum(data, dtype=float)
#     cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
#     return cumsum[window_size - 1:] / window_size

# # Generate example audio data (replace this with your actual data)
# # For demonstration purposes, we generate a sine wave with added noise
# t = np.linspace(0, 1, len(data_array))

# # Apply moving average filter
# window_size = 50
# denoised_data = moving_average_filter(data_array, window_size)

# # Plot original and denoised data
# plt.figure(figsize=(10, 6))
# plt.plot(t, data_array, label='Original Audio')
# plt.plot(t[window_size - 1:], denoised_data, label='Denoised Audio')
# plt.title('Original vs. Denoised Audio')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()


# sample_rate=16000
# write('output.wav',sample_rate,data_array)




# import serial
# import time
# import librosa
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.io.wavfile import write


# # Establish serial connection
# ser = serial.Serial('COM9', 9600)  # Change 'COM5' to the appropriate port and 9600 to the baud rate of your device

# # Define list to store data
# data_list = []

# try:
#     while True:
#         # Read data from serial port
#         line = ser.readline().decode().strip()
        
#         # Check if the line is not empty
#         if line:
#             try:
#                 data_point = int(line)
#                 data_list.append(data_point)
#                 print("Received:", data_point)
#             except ValueError:
#                 print("Invalid data received:", line)

# except KeyboardInterrupt:
#     print("Interrupted")

# finally:
#     # Close serial port
#     ser.close()

# # Convert the collected data to a NumPy array
# data_array = np.array(data_list)

# # Print the collected data array
# print("Data Array:", data_array)

# # Define function to apply moving average filter
# def moving_average_filter(data, window_size):
#     """Apply moving average filter to the data."""
#     cumsum = np.cumsum(data, dtype=float)
#     cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
#     return cumsum[window_size - 1:] / window_size

# # Apply moving average filter
# window_size = 50
# denoised_data = moving_average_filter(data_array, window_size)

# # Save denoised audio data as .wav file
# sampling_rate = 44100  # You can adjust this according to your sampling rate

# # Calculate time array based on original data length and sampling rate
# t = np.arange(len(data_array)) / sampling_rate
# print(len(data_array))
# write("denoised_audio.wav", sampling_rate, denoised_data.astype(np.int16))

# # Plot original and denoised data
# plt.figure(figsize=(10, 6))
# plt.plot(t, data_array, label='Original Audio')
# plt.plot(t[window_size - 1:], denoised_data, label='Denoised Audio')
# plt.title('Original vs. Denoised Audio')
# plt.xlabel('Time (seconds)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()









# import serial
# import time
# import librosa
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.io.wavfile import write


# # Establish serial connection
# ser = serial.Serial('COM9', 9600)  # Change 'COM5' to the appropriate port and 9600 to the baud rate of your device

# # Define list to store data
# data_list = []

# try:
#     while True:
#         # Read data from serial port
#         line = ser.readline().decode().strip()
        
#         # Check if the line is not empty
#         if line:
#             try:
#                 data_point = int(line)
#                 data_list.append(data_point)
#                 print("Received:", data_point)
#             except ValueError:
#                 print("Invalid data received:", line)

# except KeyboardInterrupt:
#     print("Interrupted")

# finally:
#     # Close serial port
#     ser.close()

# # Convert the collected data to a NumPy array
# data_array = np.array(data_list)

# # Print the collected data array
# print("Data Array:", data_array)

# # Define function to apply moving average filter
# def moving_average_filter(data, window_size):
#     """Apply moving average filter to the data."""
#     cumsum = np.cumsum(data, dtype=float)
#     cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
#     return cumsum[window_size - 1:] / window_size

# # Apply moving average filter
# window_size = 50
# denoised_data = moving_average_filter(data_array, window_size)

# # Save denoised audio data as .wav file
# sampling_rate = 44100  # You can adjust this according to your sampling rate

# # Calculate time array based on original data length and sampling rate
# t = np.arange(len(data_array)) / sampling_rate
# print(len(data_array))
# write("denoised_audio.wav", sampling_rate, denoised_data.astype(np.int16))

# # Plot original and denoised data
# plt.figure(figsize=(10, 6))
# plt.plot(t, data_array, label='Original Audio')
# plt.plot(t[window_size - 1:], denoised_data, label='Denoised Audio')
# plt.title('Original vs. Denoised Audio')
# plt.xlabel('Time (seconds)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()


# noisy_audio,sr=librosa.load('denoised_audio.wav',sr=None)
# noisy_spectrum=np.abs(librosa.stft(noisy_audio))
# noisy_spectrum=np.mean(noisy_spectrum,axis=1)
# alpha=2
# clean_spectrum=np.maximum(noisy_spectrum-(alpha*noisy_spectrum),0)
# clean_audio=librosa.istft(clean_spectrum)
# librosa.output.write_wav('cleaned_audio.wav',clean_audio,sr)


# import serial
# import wave
# import time
# import librosa
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.io import wavfile
# from scipy.io.wavfile import write


# # Establish serial connection
# ser = serial.Serial('COM9', 9600)  # Change 'COM5' to the appropriate port and 9600 to the baud rate of your device

# # Define list to store data
# data_list = []

# try:
#     while True:
#         # Read data from serial port
#         line = ser.readline().decode().strip()
        
#         # Check if the line is not empty
#         if line:
#             try:
#                 data_point = int(line)
#                 data_list.append(data_point)
#                 print("Received:", data_point)
#             except ValueError:
#                 print("Invalid data received:", line)

# except KeyboardInterrupt:
#     print("Interrupted")

# finally:
#     # Close serial port
#     ser.close()

# # Convert the collected data to a NumPy array
# data_array = np.array(data_list)

# # Define function to apply moving average filter
# def moving_average_filter(data, window_size):
#     """Apply moving average filter to the data."""
#     cumsum = np.cumsum(data, dtype=float)
#     cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
#     return cumsum[window_size - 1:] / window_size

# # Apply moving average filter
# window_size = 50
# denoised_data = moving_average_filter(data_array, window_size)

# # Save denoised audio data as .wav file
# sampling_rate = 44100  # You can adjust this according to your sampling rate
# t = np.arange(len(data_array)) / sampling_rate
# write("denoised_audio.wav", sampling_rate, denoised_data.astype(np.int16))

# # Plot original and denoised data
# plt.figure(figsize=(10, 6))
# plt.plot(t, data_array, label='Original Audio')
# plt.plot(t[window_size - 1:], denoised_data, label='Denoised Audio')
# plt.title('Original vs. Denoised Audio')
# plt.xlabel('Time (seconds)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()

# ... (moving average filtering) ...






import serial
import wave
import pyaudio
import time
import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write


# Establish serial connection
ser = serial.Serial('COM9', 9600)  # Change 'COM5' to the appropriate port and 9600 to the baud rate of your device

# Define list to store data
data_list = []

try:
    while True:
        # Read data from serial port
        line = ser.readline().decode().strip()
        
        # Check if the line is not empty
        if line:
            try:
                data_point = int(line)
                data_list.append(data_point)
                print("Received:", data_point)
            except ValueError:
                print("Invalid data received:", line)

except KeyboardInterrupt:
    print("Interrupted")

finally:
    # Close serial port
    ser.close()

# Convert the collected data to a NumPy array
data_array = np.array(data_list)

# Define function to apply moving average filter
def moving_average_filter(data, window_size):
    """Apply moving average filter to the data."""
    cumsum = np.cumsum(data, dtype=float)
    cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
    return cumsum[window_size - 1:] / window_size

# Apply moving average filter
window_size = 50
denoised_data = moving_average_filter(data_array, window_size)
sampling_rate = 44000
# Calculate the total time duration of the recording
total_time = len(data_array) / sampling_rate

# Save denoised audio data as .wav file
  # You can adjust this according to your sampling rate
t = np.linspace(0, total_time, len(data_array))  # Generate time axis based on total recording time
write("denoised_audio.wav", sampling_rate, denoised_data.astype(np.int16))

# Plot original and denoised data
plt.figure(figsize=(10, 6))
plt.plot(t, data_array, label='Original Audio')
plt.plot(t[window_size - 1:], denoised_data, label='Denoised Audio')
plt.title('Original vs. Denoised Audio')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()





# noisy_spectrum=np.abs(librosa.stft(data_array))
# noise_spectrum=np.mean(noisy_spectrum,axis=1)
# alpha=2.0
# clean_spectrum=np.maximum(noisy_spectrum-alpha*noise_spectrum,0)
# clean_audio=librosa.
import librosa
import numpy as np
# Load noisy audio
noisy_audio, sr = librosa.load('denoised_audio.wav',
sr=None)
# Calculate magnitude spectrum
noisy_spectrum = np.abs(librosa.stft(noisy_audio))
# Calculate noise profile
noise_spectrum= np.mean(noisy_spectrum, axis=1)
# Perform spectral subtrac
alpha =2.0 #Scaling facto: for noise subtraction
clean_spectrum = np.maximum(noisy_spectrum - alpha * noise_spectrum, 0)
# Synthesize clean audio
clean_audio = librosa.istft(clean_spectrum)
# Save the clean audio to a file
librosa.output.write_wav('clean_audio.wav', clean_audio, sr)


# def play_audio(data, sample_rate):
#     p = pyaudio.PyAudio()

#     # Open audio stream (adjust channels and format as needed)
#     stream = p.open(
#         rate=sample_rate,
#         channels=1,
#         format=pyaudio.paInt16,
#         output=True,
#     )

#     # Convert data to bytes (ensure data type is appropriate for format)
#     audio_data = data.astype(np.int16).tobytes()

#     # Write data to audio stream in chunks
#     chunk = 1024  # Adjust chunk size as needed (smaller for lower latency)
#     for i in range(0, len(audio_data), chunk):
#         stream.write(audio_data[i:i + chunk])

#     # Close stream and terminate PyAudio
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
# # Assuming your data is stored in the NumPy array `your_audio_data`
# # and your original sample rate is `original_sample_rate`
# play_audio(data_array, sampling_rate)
