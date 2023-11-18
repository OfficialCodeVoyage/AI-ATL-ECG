import automatic_ecg_diagnosis_master.predict as predict

data = predict.make_prediction(path_to_hdf5 = "new_ecg_tracings1.hdf5", 
                                path_to_model = "./automatic_ecg_diagnosis_master/model/model.hdf5")

print(data)