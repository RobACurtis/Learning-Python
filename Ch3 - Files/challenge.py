# make a program to make a new directory with a txt file in it
# the txt file needs to have all the names of the files listed and the bytes of all of them
# define a function
# use listdir() to return a list containing the names of the entries in the directory given by path
# use mkdir() to create a directory for the new .txt file

import os
from os import path

def main():
  src = path.realpath("challenge.py")
  root_dir, tail = path.split(src)
  list = os.listdir(root_dir)

  os.mkdir("results")
  myfile = open("./results/results.txt", "w+")
  bytes = 0
  for x in list:
    if os.path.isfile(x):
      bytes += os.path.getsize(x)
  myfile.write('Total bytecount: ' + str(bytes) + '\n')
  myfile.write('Files list: \n')
  myfile.write('---------------- \n')

  for x in list:
    if os.path.isfile(x):
        myfile.write(x + '\n')


  myfile.close()

if __name__ == "__main__":
    main()
