import os
import shutil


def png_to_txt(pngs: list):
    txts = []
    for png in pngs:
        txt = png.split('.')[0] + '.txt'
        txts.append(txt)
    return txts


def file_copy(source_file: str, dest_dir: str):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    try:
        shutil.copy(source_file, dest_dir)
    except:
        raise('Unable to copy the file: %s to target directory: %s'.format(source_file, dest_dir))


def split_data(source_dir: str, target_dir: str, train_rate=0.7, val_rate=0.9):

    img_source_dir = source_dir + '/images'
    txt_source_dir = source_dir + '/annotations_txt'
    img_target_dir = target_dir + '/images'
    txt_target_dir = target_dir + '/labels'

    # split module
    files = os.listdir(img_source_dir)
    train_files = files[:int((train_rate * len(files) - 1))]
    val_files = files[int((train_rate * len(files))):int((val_rate * len(files) - 1))]
    test_files = files[int((val_rate * len(files))):]

    train_labels = png_to_txt(train_files)
    val_labels = png_to_txt(val_files)
    test_labels = png_to_txt(test_files)

    for train_file in train_files:
        source = img_source_dir + '/' + train_file
        target = img_target_dir + '/train'
        file_copy(source, target)

    for val_file in val_files:
        source = img_source_dir + '/' + val_file
        target = img_target_dir + '/val'
        file_copy(source, target)

    for test_file in test_files:
        source = img_source_dir + '/' + test_file
        target = img_target_dir + '/test'
        file_copy(source, target)

    for train_label in train_labels:
        source = txt_source_dir + '/' + train_label
        target = txt_target_dir + '/train'
        file_copy(source, target)

    for val_label in val_labels:
        source = txt_source_dir + '/' + val_label
        target = txt_target_dir + '/val'
        file_copy(source, target)

    for test_label in test_labels:
        source = txt_source_dir + '/' + test_label
        target = txt_target_dir + '/test'
        file_copy(source, target)


if __name__ == '__main__':
    in_dir = '..'
    out_dir = '../datasets'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    split_data(in_dir, out_dir)
