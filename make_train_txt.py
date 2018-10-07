import math
import os

workdir = os.getcwd()

imgdir = 'imgs'
anndir = 'anns'
setdir = 'sets'

train_txt = open(os.path.join(workdir, setdir, 'train.txt'), 'w', encoding='utf8', newline='\n')

anns = [os.path.splitext(p)[0] for p in os.listdir(os.path.join(workdir, anndir))]

train_txt.write('\n'.join(anns))
train_txt.close()
