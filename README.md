# InterAE


## Instructions

1. Download the following [data](https://drive.google.com/drive/folders/12KufzgExIjQ-YtszCf4xYT56lpFSOZYx?usp=sharing) from google drive and add it to the `data_processing` directory.

2. If you do not want to process the data manually, and want to use either `data_more.npy` or `data_less.npy`, skip to step **4** and unzip the respective npy zipped file.

3. Follow the instructions in `Data Processing.ipynb` and change any parameters or folder paths where you see fit. Changing parameters is uneeded.

4. To train the model, open `Intermediate AutoEncoder.ipynb` and change any parameters where needed, then run the notebook.
    - If you want to use a pretrained model, run the importing cell and skip to the last cells in the notebook to import the model. Remember to change the path where the model is located

5. To generate visualizations on the testing dataset, run the **Generate Images** section and change the `SEED` to sample different *trios* from the testing dataset