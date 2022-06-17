import cv2
import os, sys
import argparse
from multiprocessing import Process


path = './output'
input = "./photos"

def create_output_dir():
    if not os.path.exists(path):
        os.makedirs(path)




def convert_to_gray(file):
    gray_img = cv2.imread(f'./photos/{file}', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'./output/{file}', gray_img)


def main():
    create_output_dir()
    filenames = os.listdir(input)
    my_parser = argparse.ArgumentParser(description='how many CPU is used')

    my_parser.add_argument('cpu',
                         type=int,
                         help='number of CPU')

    parsed_args = my_parser.parse_args()



    if parsed_args.cpu > 1:
        print(parsed_args.cpu)
    else:
        for file in filenames:
            convert_to_gray(file)

    # # if multi cpu
    # # pool, map
    # if parsed_args.multi_CPU > 1:
    #     p = Process(target=convert_to_gray, args=(parsed_args,))
    #     p.start()
    #     p.join()
    # else:
    #     for file in filenames:
    #         convert_to_gray(file)


if __name__ == "__main__":
    main()