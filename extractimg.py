#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Extract Particles
# Purpose:     Extract frames from 3D tomography into 2D images
# Author:      Kui Xu
# Created:     04/08/2018
#
#-------------------------------------------------------------------------------

import mrcfile,sys
import numpy as np
from skimage import io
import argparse

arser = argparse.ArgumentParser()
parser.add_argument('--mrc', required=True, help='mrc file path')
parser.add_argument('--dir', default="001", help='Images/001')
parser.add_argument('--i', default=80,type=int, help='start index')
parser.add_argument('--j', default=140,type=int, help='end index')

args = parser.parse_args()

filename = args.mrc
outdir = "./Images/"+args.dir
i =args.i
j =args.j
if not os.path.exists(outdir):
    os.makedirs(outdir)
with mrcfile.open(filename) as mrc:
    s=mrc.data.shape
    data = (mrc.data - np.min(mrc.data))/(np.max(mrc.data)-np.min(mrc.data))
    print(filename, s)
    for k in range(i,j):
        img = np.zeros([s[0],s[2],3])
        img[:,:,0] = data[:,k,:]
        img[:,:,1] = data[:,k,:]
        img[:,:,2] = data[:,k,:]
        io.imsave(outdir+'/%03d.png'%(k),img)
        print(k)
