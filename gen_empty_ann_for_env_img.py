import math
import os
from pascal_voc_io import PascalVocWriter
import imageio

workdir = os.getcwd()
# workdir = r'D:\DeepLearningProject\datasets\konohana_dataset\_ep10'

imgdir = 'imgs'
anndir = 'anns'
setdir = 'sets'

imgs_basename_fullname = [[os.path.splitext(p)[0], p] for p in os.listdir(os.path.join(workdir, imgdir))]
anns_basename = set([os.path.splitext(p)[0] for p in os.listdir(os.path.join(workdir, anndir))])

need_del_id = []

for i, k in enumerate(imgs_basename_fullname):
    if k[0] in anns_basename:
        need_del_id.append(i)

for i in sorted(need_del_id)[::-1]:
    del imgs_basename_fullname[i]

print('Need process ' + str(len(imgs_basename_fullname)) + ' files')

for basename_fullname in imgs_basename_fullname:
    basename, fullname = basename_fullname
    print(fullname)

    img = imageio.imread(os.path.join(workdir, imgdir, fullname))

    w = PascalVocWriter(imgdir, fullname, img.shape)
    w.save(os.path.join(workdir, anndir, basename+'.xml'))

print('complete')