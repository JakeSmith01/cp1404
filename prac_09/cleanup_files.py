"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_string = ''
    for i, letter in enumerate(filename):
        if letter.islower():


    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

main()