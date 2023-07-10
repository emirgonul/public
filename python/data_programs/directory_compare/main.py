import os
#TODO:1.update print feature
#2. update fixed directory paths to dynamic 

#directories
dir1 = "/Users/emir/Desktop/testfolder/t1"
dir2 = "/Users/emir/Desktop/testfolder/t2"


def list_files(path):
    #Returns a set of the names of all files in the given directory.

    return set(os.listdir(path))

def compare_directories(dir1, dir2):
    #compares two directories and returns lists of files that are the same
    #and files that are only in each directory.

    files1 = list_files(dir1)
    files2 = list_files(dir2)

    same_files = sorted(files1 & files2)
    only_dir1 = sorted(files1 - files2)
    only_dir2 = sorted(files2 - files1)

    return same_files, only_dir1, only_dir2


same_files, only_dir1, only_dir2 = compare_directories(dir1, dir2)

print("Same files:")
print(same_files)
print()

print(f"Files only in directory {dir1}:")
print(only_dir1)
print()

print(f"Files only in directory {dir2}:")
print(only_dir2)