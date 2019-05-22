import argparse
from PathHandler import PathHandler
from Splitter import Splitter

num_passed = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', help='The path of the Petri Net file.', type=str)
    parser.add_argument('output_path', help='The path of the event log.', type=str)

    args = parser.parse_args()

    ph = PathHandler(args.input_path, args.output_path)
    splitter = Splitter(0.8)

    input_paths = ph.get_input_file_paths()
    training_paths = ph.get_training_set_paths()
    test_paths = ph.get_testing_set_paths()

    for i in range(ph.get_num_files()):
        splitter.split(input_paths[i])
        splitter.save_training_set(training_paths[i])
        splitter.save_testing_set(test_paths[i])

