import cv2
import os
import argparse
from multiprocessing import Pool


path = "./output"
input = "./photos"


def create_output_dir():
    if not os.path.exists(path):
        os.makedirs(path)


def convert_to_gray(file):
    gray_img = cv2.imread(f"./photos/{file}", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f"./output/{file}", gray_img)


def main():
    create_output_dir()
    filenames = os.listdir(input)
    my_parser = argparse.ArgumentParser(description="how many CPU is used")

    my_parser.add_argument("cpu", type=int, help="number of CPU")

    parsed_args = my_parser.parse_args()

    with Pool(parsed_args.cpu) as p:
        p.map(convert_to_gray, filenames)


if __name__ == "__main__":
    main()
