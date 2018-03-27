import os
import argparse
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
from PIL import ImageChops

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', action='store', type=str)
    parser.add_argument('--dilation', action='store', type=int, default=5)
    args = parser.parse_args()

    dir, fname = os.path.split(args.img)
    img_name, ext = os.path.splitext(fname)
    img_out_name = img_name + '_nurie' + ext

    print('File:{} is converted to {}'.format(fname, img_out_name))

    img_org = Image.open(args.img)
    img_gray = img_org.convert('L')  # Gray scale image
    img_gray_dilation = img_gray.filter(ImageFilter.MaxFilter(args.dilation))  # dilation
    img_diff = ImageChops.difference(img_gray, img_gray_dilation)  # diff(Edge image)
    img_diff_invert = ImageOps.invert(img_diff)

    img_diff_invert.show()
    img_diff_invert.save(img_out_name)

    # Memo: Below command generate similar image
    # ImageOps.invert(img_gray.filter(ImageFilter.FIND_EDGES))
