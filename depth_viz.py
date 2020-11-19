import os
# import cv2
import imageio
from mayavi import mlab
import numpy as np

from vinci.cv.utils import remap_gray_image, im_scale_fixed_ar, show_cv2_image
from vinci.utils import pickle_thing, unpickle_thing

depth = imageio.imread('output/ireland_dingle.png')

depth = remap_gray_image(depth) * 255

# # grab the first image
# img = images[0,:,:,:]
# img = np.moveaxis(img,[0,1,2],[2,1,0])
# depth = depths[0,:,:]
# depth = np.swapaxes(depth,0,1)

# # depth = cv2.cvtColor(depth, cv2.COLOR_BGR2GRAY)

# print("np.min(depth)")
# print(np.min(depth))
# print("np.max(depth)")
# print(np.max(depth))
# depth2 = remap_gray_image(depth, min_bias=0)
# # flip the depth to match 3d inpainting
# depth = 1 - depth
# # depth = depth * 100

# # crop, because there's a border around the image
# border_size = 10
# depth = depth[border_size:-border_size, border_size:-border_size]
# img = img[border_size:-border_size, border_size:-border_size]


# np.save('nyu_depth.npy', depth)

# depth = depth * 255
# cv2.imwrite('make3d_depth.png', depth)
# cv2.imwrite('make3d_image.jpg', img)

# show_cv2_image(depth)

# import ipdb
# ipdb.set_trace()
# depth = remap_gray_image(depth)

# depth = cv2.resize(depth, (150, 100), interpolation=cv2.INTER_AREA)


h, w = depth.shape
y = np.arange(h)
x = np.arange(w)

x_m, y_m = np.meshgrid(x, y)

mlab.clf()

# see: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html?highlight=contour_surf#mesh
mlab.mesh(-1*x_m, y_m, -1*depth)
mlab.show()

# view the file with: $ ctmviewer shape.obj
# note won't have color map
# mlab.savefig("shape.obj")
