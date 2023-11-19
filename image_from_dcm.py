import pydicom
import matplotlib.pyplot as plt
import numpy as np

def generate_waveform(file_path):
    # Read the DICOM file
    ds = pydicom.dcmread(file_path)


    if (0x5400, 0x0100) in ds:
        waveform_sequence = ds[0x5400, 0x0100]
        i = 0
        for waveform in waveform_sequence:
            i += 1
            if (0x5400, 0x1010) in waveform:
                binary_waveform_data = waveform[0x5400, 0x1010].value

                # Convert binary data to int16
                waveform_data = np.frombuffer(binary_waveform_data, dtype=np.int16)

                # New reshape logic: Assuming each ECG recording has 4096 samples per lead
                num_leads = 12
                num_samples_per_recording = 4096
                total_samples = num_samples_per_recording * num_leads

                # Ensure that the total number of samples is a multiple of total_samples
                num_recordings = len(waveform_data) // total_samples
                waveform_data = waveform_data[:num_recordings * total_samples]
                waveform_data = waveform_data.reshape(num_recordings, num_samples_per_recording, num_leads).astype(np.float64)
                return waveform_data
    else:
        print("No ECG waveform data found in the DICOM file.")

    

def plot_ecg(waveform_data, num_leads=12, num_samples_per_recording=4096):
    # Assuming you want to plot the first recording
    recording_index = 0

    # Create a figure with subplots for each lead
    fig, axes = plt.subplots(num_leads, 1, figsize=(10, 2 * num_leads))

    for i in range(num_leads):
        # Plot each lead in a different subplot
        axes[i].plot(waveform_data[recording_index, :, i])
        axes[i].set_title(f'Lead {i+1}')
        axes[i].set_xlabel('Sample')
        axes[i].set_ylabel('Amplitude')

    plt.tight_layout()
    plt.show()


# Replace with the path to your DICOM file
#waveform = generate_waveform("anonymous_ecg.dcm")
#plot_ecg(waveform)
