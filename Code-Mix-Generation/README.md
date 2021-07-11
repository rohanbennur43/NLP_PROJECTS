# Code Mix Generation (Project)

*Multilinguals_1394*


*Rohan Bennur(PES12018017198)*


### How to execute the code

There are different jupyter notebook files in the src directory for different models.

To open any jupyter notebook file,

```python
$ cd src
$ jupyter notebook model<N>.ipynb
```

where, N is the model ID as mentioned below,

N = 1 : Baseline model

N = 2 : Improved model 1 (using unk tokens)

N = 3 : Improved model 2 (using language information)

N = 4 : Improved model 3 (using both language information and unk tokens)

Some variables will have to be set in the jupyter notebook file before running the cells

**Dataset path**: File path which contains the dataset (separate for train and test set)

**Model path**: File path where you want to store the model instance

Outputs are in the folder /outputs.

> Outputs of corresponding models are in /outputs/model_id

File that was used to create datasets is in /utils/create_datasets.py
