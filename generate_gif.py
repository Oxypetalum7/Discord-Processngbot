import glob
import os

from PIL import Image


def generate_image():
    os.chdir('sketch')
    files = sorted(glob.glob('*.png'))
    images = list(map(lambda file: Image.open(file), files))
    images[0].save('out.gif', save_all=True, append_images=images[1:], optimize=False, duration=250, loop=0)
    print('Generated.')
    for p in glob.glob('*.png'):
        if os.path.isfile(p):
            os.remove(p)
    os.chdir('../')
