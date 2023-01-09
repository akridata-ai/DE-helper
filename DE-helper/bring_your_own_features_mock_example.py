"""
Create a catalog (csv file) as an example of Bring-Your-Own-Features

CSV format file can be found in:
https://docs.akridata.ai/docs/prep-external-features
and is expected to be:
<path to file name>,<file index>,<features>

Notes
 - file index is always 0 for images
 - modify parameters in:
    get_params()
"""

import numpy as np
import os
import typing as typ


def update_csv(path_csv: str, line: str):
    """Add line to the csv file"""
    with open(path_csv, 'a') as file_handler:
        file_handler.write(line)
    return


def add_comma(input_string: str) -> str:
    """Add comma to the string"""
    return input_string + ","


def create_csv_header(path_csv: str, feature_length: int):
    """Create the base header for the csv file"""
    line = f"file_path(string),frame_idx_in_file(int),features(float[{str(feature_length)}])" + "\n"
    update_csv(path_csv, line)
    return


def process_files(path_csv: str, list_files: list, feature_size: int):
    """
    INPUT:
        path_csv: str - the path to the csv
        list_files: list - the list of files
        feature_size: int - the size of the feature vector
    """
    num_files = len(list_files)
    for ind_file, current_file in enumerate(list_files):
        # the mock (random) values as feature values:
        val = np.random.rand(feature_size)

        # the line for the current file: file name, image index (0 for images), feature values
        line = \
            add_comma(current_file) + \
            add_comma("0") + \
            ",".join([str(v) for v in val]) + \
            "\n"

        # write values to the csv:
        update_csv(path_csv, line)
        print(f"{ind_file + 1} / {num_files} processed")
    return


def get_params() -> typ.Tuple[str, str, int]:
    # where the images are:
    path_images: str = ""  # ADD PATH HERE

    # where to create the csv file:
    path_csv: str = "feature.csv"

    # number of random values for feature vector:
    feature_size: int = 128

    # set the random seed for consistent output:
    np.random.seed(17)

    return \
        path_images, \
        path_csv, \
        feature_size


def main():
    """
    1. Get all the images in the provided path
    2. Create a csv file with a row per file with mock (random) features
    """

    # the params:
    path_images, path_csv, feature_size = get_params()

    # a list of the files:
    list_files = sorted(os.listdir(path_images))

    # csv header:
    create_csv_header(path_csv, feature_size)

    # process each file and update the csv
    process_files(path_csv, list_files, feature_size)

    return


if __name__ == '__main__':
    main()
