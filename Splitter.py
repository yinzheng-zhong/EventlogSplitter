import pandas as pd
import numpy as np


class Splitter:
    def __init__(self, percent_training, seed=0):
        self.seed = seed
        self.percent_training = percent_training

        self.testing = None
        self.training = None

    def split(self, path):
        data = pd.read_csv(path, index_col=False, low_memory=False)

        ids = data['Case_ID'].unique()
        num_ids = len(ids)
        np.random.seed(self.seed)

        sub_set_index = np.random.choice(num_ids, int(num_ids * self.percent_training), replace=False)

        match = data['Case_ID'].isin(ids[sub_set_index])
        self.training = data[match]
        self.testing = data[~match]

    def save_training_set(self, path):
        self.training.to_csv(path, index=False)

    def save_testing_set(self, path):
        self.testing.to_csv(path, index=False)
