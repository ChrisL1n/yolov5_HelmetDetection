import os
import xml.etree.ElementTree as ET
import glob
import cv2


def size_get(input_file: str):
    image = cv2.imread(input_file)
    w = image.shape[1]
    h = image.shape[0]
    return w, h


def xml_to_txt(indir: str, outdir: str, image_dir: str):
    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations) + '*.xml')
    for i, file in enumerate(annotations):
        image_file = file.split('.')[0] + '.png'
        image_path = image_dir + '//' + image_file
        w, h = size_get(image_path)
        file_save = file.split('.')[0] + '.txt'
        file_txt = outdir + "\\" + file_save
        f_w = open(file_txt, 'w')
        # actual parsing
        in_file = open(file)
        tree = ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            current = list()
            name = obj.find('name').text
            if name == 'with_mask':
                name_cls = '0'
            else:
                name_cls = '1'
            xmlbox = obj.find('bndbox')
            xn = xmlbox.find('xmin').text
            xx = xmlbox.find('xmax').text
            yn = xmlbox.find('ymin').text
            yx = xmlbox.find('ymax').text
            xmid_f = '%.6f' % ((int(xx) + int(xn)) / 2 / w)
            wid_f = '%.6f' % ((int(xx) - int(xn)) / w)
            ymid_f = '%.6f' % ((int(yn) + int(yx)) / 2 / h)
            hei_f = '%.6f' % ((int(yx) - int(yn)) / h)
            f_w.write(name_cls + ' ' + xmid_f + ' ' + ymid_f + ' ' + wid_f + ' ' + hei_f + '\n')


if __name__ == '__main__':
    input_dir = '../annotations'
    output_dir = '../annotations_txt'
    image_dir = '..//images'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    xml_to_txt(input_dir, output_dir, image_dir)
