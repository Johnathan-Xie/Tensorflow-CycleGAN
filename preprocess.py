from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed

# load all images in a directory into memory
def load_images(path, size=(256,256)):
    data_list = list()
    # enumerate filenames in directory, assume all are images
    for filename in listdir(path):
        # load and resize the image
        pixels = load_img(path + filename, target_size=size)
        # convert to numpy array
        pixels = img_to_array(pixels)
        # store
        data_list.append(pixels)
    return asarray(data_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_path', type=str, help='path to dataset folder')
    parser.add_argument('--img_size', type=str, help='''img_dims formatted as "dim1 dim2"''')
    parser.add_argument('--out_file', type=str, help='processed dataset path')
    opt= = parser.parse_args()
    
    path = opt.folder_path
    dims = (int(i) for i in opt.img_size.split())
    out_file = opt.out_file
    
    dataA1 = load_images(path + 'trainA/', size=dims)
    print('Loaded dataA: ', dataA.shape)
    
    dataB1 = load_images(path + 'trainB/', size=dims)
    print('Loaded dataB: ', dataB.shape)

    savez_compressed(out_file, dataA, dataB)
    print('Saved dataset: ', out_file)
