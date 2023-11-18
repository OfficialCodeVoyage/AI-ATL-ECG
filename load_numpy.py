import numpy as np
np.set_printoptions(suppress=True)
result = np.load("AI-ATL-ECG/automatic-ecg-diagnosis-master/dnn_predicts/other_seeds/model_1.npy")
print(result.shape)
print(np.max(result))