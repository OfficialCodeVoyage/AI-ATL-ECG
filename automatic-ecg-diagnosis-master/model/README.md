# Pre-trained deep neural network models for ECG automatic abnormality detection

Contain the pre-trained models of the deep neural networks described on the paper:
"Automatic diagnosis of the 12-lead ECG using a deep neural network".
 https://www.nature.com/articles/s41467-020-15432-4.

Companion python scripts are available in:
https://github.com/antonior92/automatic-ecg-diagnosis

--------

Citation:
```
Ribeiro, A.H., Ribeiro, M.H., Paixão, G.M.M. et al. Automatic diagnosis of the 12-lead ECG using a deep neural network.
Nat Commun 11, 1760 (2020). https://doi.org/10.1038/s41467-020-15432-4
```

Bibtex:
```
@article{ribeiro_automatic_2020,
  title = {Automatic Diagnosis of the 12-Lead {{ECG}} Using a Deep Neural Network},
  author = {Ribeiro, Ant{\^o}nio H. and Ribeiro, Manoel Horta and Paix{\~a}o, Gabriela M. M. and Oliveira, Derick M. and Gomes, Paulo R. and Canazart, J{\'e}ssica A. and Ferreira, Milton P. S. and Andersson, Carl R. and Macfarlane, Peter W. and Meira Jr., Wagner and Sch{\"o}n, Thomas B. and Ribeiro, Antonio Luiz P.},
  year = {2020},
  volume = {11},
  pages = {1760},
  doi = {https://doi.org/10.1038/s41467-020-15432-4},
  journal = {Nature Communications},
  number = {1}
}
```
-----

All files are in the format `.hdf5` and can be read using
```python
from keras.models import load_model
from keras.optimizers import Adam
model = load_model(args.model, compile=False)
model.compile(loss='binary_crossentropy', optimizer=Adam())
```
The model take as input tensors with dimension `(batch_size, 4096, 12)` where 4096 are samples of the ecg signal 
(sampled during, approximately, 10s at 400Hz) from 12 different leads. All signal are represented as
32 bits floating point numbers at the scale 1e-4V: so if the signal is in V it should be multiplied by 
1000 before feeding it to the neural network model.  In the last dimension, the ECG leads are ordered in
the following order: `{DI, DII, DIII, AVL, AVF, AVR, V1, V2, V3, V4, V5, V6}`.
 
 
The neural network yield an output with dimension `(batch_size, 6)`. Each entry correspond to probability between 0 and 1
on the giving exam. It does that for 6 different ECGs abnormalities: (in that order)
- 1st degree AV block (1dAVb);
- right bundle branch block (RBBB);
- left bundle branch block (LBBB);
- sinus bradycardia (SB);
- atrial fibrillation (AF); and,
- sinus tachycardia (ST).
These abnormalities are not mutually exclusive and the probabilities outputs of the model does not necessarely sums to 1.

## Folder content

- The main model used along the paper is the one named `model.hdf5`. 

- In order to show the stability of the method we also train 10 different neural networks
with the same architecture and configuration but with different
initial seeds. These models are saved as `other_seeds/model_[1-10].hdf5`. The main 
model `model.hdf5` correspond to  `other_seeds/model_6.hdf5` which is the one with 
micro average precision imediatly above the median value.

- Finally, to assess the effect of how we structure our problem, we have considered alternative
scenarios where we use 90\%-5\%-5\% splits, stratified randomly, by patient or in chronological order. 
The models trained in these scenarios are saved in the folder `other_splits/`.
