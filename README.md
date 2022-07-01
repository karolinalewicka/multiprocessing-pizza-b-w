# multiprocessing-pizza-b-w

Aplikacja wykorzystuje bibliotekę openCV, która zamienia zdjęcia z folderu ./photos na ich czarno-białe wersje w folderze ./output. Wywołując z konsoli program, użytkownik podaje liczbę procesów, na których ma on zadziałać (program przetwarza to za pomocą argparse). 

Program wywołuje się wołając "rm -rf output/ ; time python3 main.py [liczba procesów]", np. rm -rf output/ ; time python3 main.py 5.

Po wywołaniu, w konsoli pojawiają się statystyki dotyczące czasu operacji. 
