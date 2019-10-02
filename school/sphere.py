import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import cos, sqrt

def z(x, y, c):
    pts = []
    
    for _y in y:
        for _x in x:
            yc = _y-c
            xc = _x-c
            z_sq = r*r - xc*xc - yc*yc
            if z_sq > 0:
                pts.append([_x, _y, sqrt(z_sq)])

    return np.array(pts)

def normals(pts, c):
    n = []

    for x, y, z in pts:
        tmp_n = [(x-c)/z, (y-c)/z, 1]
        norm = sqrt(tmp_n[0]*tmp_n[0] + tmp_n[1]*tmp_n[1] + 1)
        n.append([tmp_n[0]/norm, tmp_n[1]/norm, 1/norm])
    return np.array(n)


def dot_product(normals, pts, img):
    for idx, (nx, ny, nz) in enumerate(normals):
        dot = nx * I[0] + ny * I[1] + nz * I[2]
        img[(int)(pts[idx, 1]), (int)(pts[idx, 0])] = dot
    return img
                
r = 50 # radius
I = (0.2, 1, 0.98)

col = 240
row = 240
img = np.zeros((row, col))
c = col/2

x = np.linspace(0, col, col, endpoint=False)
y = np.linspace(0, row, row, endpoint=False)
pts = z(x, y, c)


normals = normals(pts, c)



dot_product(normals, pts, img)

plt.imshow(img)
plt.show()

