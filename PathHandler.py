import os


class PathHandler:
    def __init__(self, input_folder, output_folder):
        self._folder_input = input_folder
        self._folder_output = output_folder
        self._input_file_names = self.find_input_files()
        self._input_file_paths = self.calc_input_file_paths()
        self._training_set_paths = self.calc_training_set_paths()
        self._testing_set_paths = self.calc_testing_set_paths()

    def find_input_files(self):
        file_names = []
        for file in os.listdir(self._folder_input):
            if file.endswith(".csv"):
                file_names.append(file)

        return file_names

    def calc_input_file_paths(self):
        file_paths = []
        for file in self._input_file_names:
            file_paths.append(os.path.join(self._folder_input, file))

        return file_paths

    def calc_testing_set_paths(self):
        file_paths = []
        for file in self._input_file_names:
            file_paths.append(os.path.join(self._folder_output, file)[:-4] + '_test.csv')

        return file_paths

    def calc_training_set_paths(self):
        file_paths = []
        for file in self._input_file_names:
            file_paths.append(os.path.join(self._folder_output, file)[:-4] + '_training.csv')

        return file_paths

    def get_num_files(self):
        return len(self._input_file_names)

    def get_input_file_paths(self):
        return self._input_file_paths

    def get_training_set_paths(self):
        return self._training_set_paths

    def get_testing_set_paths(self):
        return self._testing_set_paths
