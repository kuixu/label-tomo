Label-Tomo
===============

Code for labeling tomo particle center in images  and plotting figures.

**Screenshot:**
![Label Tool](./screenshot.png)

Data Organization
-----------------
LabelTool  
|  
|--main.py   *#  code for labeling*  
|--plot.py   *#  code for the plotting*  
|--extractimg.py   *#  code for extracting image from tomography*  
|  
|--Images/   *# direcotry containing the images to be labeled*  
|  
|--Labels/   *# direcotry for the labeling results*  
|  
|--Examples/  *# direcotry for the example bboxes*  

Environment
----------
- python 2.7
- python PIL (Pillow)
- matplotlib

Run
-------
### 1.Extracting Imge plane from \*.mrc file into Images\/001 folder
$ python extractimg.py xxx.mrc 001

### 2. Label particles
$ python main.py

### 3.Plotting
$ python plot.py 001

