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


filename=sys.argv[0]
dirname=sys.argv[1]
outdir="./Images/"+dirname
if not os.path.exists(outdir):
    os.makedirs(outdir)
with mrcfile.open(filename) as mrc:
    s=mrc.data.shape
    data = (mrc.data - np.min(mrc.data))/(np.max(mrc.data)-np.min(mrc.data))
    print(filename, s)
    for i in range(80,140):
        img = np.zeros([s[0],s[2],3])
        img[:,:,0] = data[:,i,:]
        img[:,:,1] = data[:,i,:]
        img[:,:,2] = data[:,i,:]
        io.imsave(outdir+'/%03d.png'%(i),img)
        print(i)
