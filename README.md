# Multiprocessing Pizza B&W

The application uses the openCV library to convert photos from the ./photos folder to their black and white versions in the ./output folder. When calling the program from the console, the user specifies the number of processes on which it should operate using argparse.

The program is called by typing "rm -rf output/ ; time python3 main.py [number of processes]", e.g. rm -rf output/ ; time python3 main.py 5.

After calling the program, statistics regarding the operation time appear in the console.
