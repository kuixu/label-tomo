#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Plot tomo particles
# Purpose:     Plot tomo particles with scale to (nm)
# Author:      Kui Xu
# Created:     06/08/2018
#
#-------------------------------------------------------------------------------

import glob,os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

dirname='001'
scale = 0.7088
filelist = glob.glob(os.path.join('Labels/'+dirname, '*.txt'))
xyz=[]
for (i, fname) in enumerate(filelist):
    z=int(fname.replace('Labels/'+dirname+"/","").replace(".txt",""))
    with open(fname,"r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line=line.strip().split()
            xyz.append([int(line[0]),int(line[1]),z])
center_box=np.array(xyz)
x=center_box[:,0] * scale
y=center_box[:,2] * scale

print("point num:", len(x))
name ="plot-"+dirname
csv = np.vstack((x,y)).T;
np.savetxt(name+".cvs", csv,delimiter=',')


ylim = 200 * scale
#print(xyz)

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(x, y, '.')
#ax.set_title('NMS, p<0.3, iou<0.7, num:'+str(len(center_box)))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax.set_xlabel('X position (nm)', fontsize=20)
ax.set_ylabel('Z position (nm)', fontsize=20)
ax.set_ylim(20, 100)
#ax.legend(..., fontsize=20)
#plt.show()
fig.savefig(name+".pdf")
