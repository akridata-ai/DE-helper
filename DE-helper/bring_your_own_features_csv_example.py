"""
Code snippet to demonstrate code to save a csv file used by Bring-Your-Own-Features

Data Explorer (DE) allows the user to process their images with their own Featurizer,
save the feature vector per image in a csv file, and ingest the csv instead of processing the image.

Below is a code snippet that demonstrate csv file creation:
    1. Header, as required by DE - for details, see: https://docs.akridata.ai/docs/prep-external-features
    2. A line per image, with comma separated values following: <path to file name>,<file index>,<features>
        - file name and path
        - file index (0 for image, frame index for a video) - 0 for both images in the example below
        - feature vector
"""


def update_csv(path_csv: str, line: str):
    """Append the line to the csv file"""
    with open(path_csv, "a") as file_handler:
        file_handler.write(line)
    return


def main():
    """
        1. Write the header.
           Change the number of features in your own example from the below 3

        2. Write two example lines:
           - Image names are "image_1.jpg" and "image_2.jpg"
           - Both lines have image index 0, as always the case in separate images.
             It is expected to be a running frame index when processing a video file.
           - Feature vectors are:
                 line 1 for image_1: 1.0,2.0,3.0
                 line 2 for image_2: 6.0,7.0,8.0
    """

    path_csv: str = "my_features.csv"
    update_csv(path_csv, f"file_path(string),frame_idx_in_file(int),features(float[3])" + "\n")
    update_csv(path_csv, f"image_1.jpg,0,1.0,2.0,3.0" + "\n")
    update_csv(path_csv, f"image_2.jpg,0,6.0,7.0,8.0" + "\n")
    return


if __name__ == '__main__':
    main()
