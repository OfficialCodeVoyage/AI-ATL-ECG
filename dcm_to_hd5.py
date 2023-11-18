import pydicom
import h5py
import delia as dl
import numpy as np


# Replace with your HDF5 file path
hdf_file_path = 'ecg_tracings.hdf5'
dcm_file_path = 'anonymous_ecg.dcm'

new_hdf_file_path = 'new_ecg_tracings'


def convert_dicom_to_hdf5(dicom_path, hdf5_path):
    ds = pydicom.dcmread(dicom_path)

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

                # Reshape the data and convert to float64
                waveform_data = waveform_data.reshape(num_recordings, num_samples_per_recording, num_leads).astype(np.float64)

                # Save the waveform data to HDF5
                with h5py.File(hdf5_path+str(i)+".hdf5", 'w') as hdf:
                    hdf.create_dataset('tracings', data=waveform_data)
                    print("created")
    else:
        raise ValueError("Waveform Sequence tag not found in DICOM file")

# Run the conversion
# convert_dicom_to_hdf5(dcm_file_path, new_hdf_file_path)



# Open the HDF5 file
with h5py.File('new_ecg_tracings1.hdf5', 'r') as file:
    # Access the 'tracings' dataset
    tracings = file['tracings']

    # Get basic information about the dataset
    shape = tracings.shape  # The shape of the dataset (dimensions and size)
    dtype = tracings.dtype  # Data type of the elements

    # Optionally, read a small part of the dataset
    # Reading only the first few entries to avoid loading large data into memory
    sample_data = tracings[:5]  # Adjust the number as needed

    # Print the information
    print("Shape of Dataset:", shape)
    print("Data Type of Dataset:", dtype)
    print("Sample Data (first few entries):", sample_data)

