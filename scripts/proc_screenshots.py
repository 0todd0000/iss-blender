
import os,glob
from PIL import Image


def resize(fpath, quality=85, factor=0.6):
    with Image.open(fpath) as img:
        w   = int(img.width * factor)
        h   = int(img.height * factor)
        img = img.resize((w, h), Image.LANCZOS)
        img.save(fpath, "JPEG", quality=quality, optimize=True)


dir0   = os.path.expanduser('~/Desktop')
fpaths = sorted( glob.glob( os.path.join(dir0, 'Screenshot*.jpg') ) )
prefix = 'cf'
for i,fpath in enumerate(fpaths):
    fpath1 = os.path.join(dir0, f'{prefix}{i:02d}.jpg')
    os.rename(fpath, fpath1)
    resize(fpath1, factor=0.6)
    







