import os
import shutil


def count_files(path):
    number_of_files = 0
    for file_number in range(10):
        for file_name in os.listdir(path):
            if "(" + str(file_number) + ")" in file_name:
                number_of_files += 1
    return number_of_files


def copy_images(root, species_name, save, number_of_images):
    path = os.path.join(root, species_name)
    counter = 0

    for file_number in range(10):
        if counter >= number_of_images:
            break
        for file_name in os.listdir(path):
            if counter >= number_of_images:
                break
            if "(" + str(file_number) + ")" in file_name:
                counter += 1
                shutil.copyfile(os.path.join(path, file_name), os.path.join(save, file_name))


def check_and_copy(load, save, number_of_images):
    for root, dirs, files in os.walk(load):
        for folder in dirs:
            if count_files(os.path.join(root, folder)) > number_of_images:
                copy_images(root, folder, os.path.join(save, folder), number_of_images)


if __name__ == "__main__":
    number_of_examples = 150
    load_path = r"D:\Folders\_Engineering_ThesisV2\testing_data\spectrograms\Slaney"
    save_path = r"D:\Folders\_Engineering_ThesisV2\testing_data\check\Slaney"

    try:
        os.mkdir(save_path)
    except OSError:
        print(save_path + " folder already exists.")

    for root, dirs, files in os.walk(load_path):
        for dirname in dirs:
            try:
                os.mkdir(os.path.join(save_path, dirname))
            except OSError:
                print(dirname + " folder already exists.")
    #
    # check_and_copy(load_path, save_path, number_of_examples)
    #
    species = ["CommonBlackbird", "CommonChiffchaff", "CommonCrane", "EurasianWren", "GreatSpottedWoodpecker", "GreatTit", "RedCrossbill", "SongThrush"]
    for root, dirs, files in os.walk(load_path):
        for folder in dirs:
            if folder in species:
                copy_images(root, folder, os.path.join(save_path, folder), 30)