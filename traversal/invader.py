# recursive function to make folder discovery
import os


def main():
    for item in recursive_folder_walk(os.getcwd()):
        print(item)


def recursive_folder_walk(initial_dir):
    listing = []

    for item in os.listdir():
        if os.path.isdir(item):
            os.chdir(item)
            listing = listing + recursive_folder_walk(os.getcwd())
        else:
            listing.append((os.getcwd()+'\\'+item))

    os.chdir('../')
    return listing


if __name__ == '__main__':
    main()
