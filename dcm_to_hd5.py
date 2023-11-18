import pydicom
import h5py
import delia as dl

def dicom_to_hdf5(dicom_file_path, hdf5_file_path):
    # Read the DICOM file
    ds = pydicom.dcmread(dicom_file_path)

    # Process the DICOM data as needed (this is a basic example)
    # Extracting ECG waveform data - modify this based on your DICOM file structure
    # Assuming the ECG data is stored in a specific tag, replace 'tag' with the correct DICOM tag
    ecg_data = ds.get('tag')

    # Convert the data to HDF5 format using delia
    dl.to_hdf5(ecg_data, hdf5_file_path)

# Example usage
dicom_file_path = 'anonymous_ecg.dcm'
hdf5_file_path = 'output_ecg.h5'
dicom_to_hdf5(dicom_file_path, hdf5_file_path)
