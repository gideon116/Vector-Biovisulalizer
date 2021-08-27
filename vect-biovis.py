from vpython import *
import numpy as np
from PIL import Image
import plotly.graph_objects as go


def open_image(resolution, imm):
    img = imm
    fast_x = []
    fast_y = []
    fast_z = []

    for i in range(1, 74):

        img.seek(i)

        img1 = img.resize((int(resolution), int(resolution)))
        rgb_im = img1.convert('RGB')
        data = np.insert(np.transpose(np.nonzero(np.sum(np.asarray(rgb_im, dtype="int32"), axis=2))), 2, i, axis=1)

        if data is not []:
            for n in data:
                fast_x.append(n[0])
                fast_y.append(n[1])
                fast_z.append(n[2])

    return fast_x, fast_y, fast_z

x, y, z = open_image(200, Image.open("./AICS-13-part12/2017_06_28_lamin/AICS-13/AICS-13_1256.ome_struct_segmentation.tiff"))
x=np.asarray(x)
y=np.asarray(y)
z=np.asarray(z)
scene2 = canvas(title='Biov',
                center=vector(x[int(len(x)/2)],y[int(len(y)/2)],z[int(len(z)/2)]), background=color.black,
                width=1650, height=700, range=500)

for i in range(len(z)):
    ball = points(pos=vector(x[i], y[i], z[i]), radius=10, canvas=scene2, shininess=0)



