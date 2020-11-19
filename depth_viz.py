import logging
import os

import click
import imageio
from mayavi import mlab
import numpy as np

from vinci.cv.utils import remap_gray_image, im_scale_fixed_ar, show_cv2_image
from vinci.utils import pickle_thing, unpickle_thing


from vinci.log import LoggerNameAdapter
import vinci.log as vlog
vlog.basic_logging_config()

LOGGER_NAME = __name__ # or whatever
logger = LoggerNameAdapter(logging.getLogger(LOGGER_NAME))

@click.group()
@vlog.simple_verbosity_option(LOGGER_NAME)
def cli():
    """This function is necessary for the click CLI to work."""

@cli.command()
@click.option('--depth', type=str, default='output/ireland_dingle.png', 
    help='the depth image')
def go(
        depth: str,
    ):
    depth_file = depth

    if depth_file.endswith('.png'):
        depth = imageio.imread(depth_file)
    elif depth_file.endswith('.npy'):
        depth = np.load(depth_file)

    depth = remap_gray_image(depth) * 255

    # depth = cv2.resize(depth, (150, 100), interpolation=cv2.INTER_AREA)


    h, w = depth.shape
    y = np.arange(h)
    x = np.arange(w)

    x_m, y_m = np.meshgrid(x, y)

    mlab.clf()


    # see: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html?highlight=contour_surf#mesh
    mlab.mesh(-1*x_m, y_m, depth)

    def set_camera():
        f = mlab.gcf()
        camera = f.scene.camera
        camera.position = [-1597.8292121100346, 629.2231636956069, 5714.597119236536]
        camera.focal_point = [-719.5, 1279.5, 127.5]
        camera.view_angle = 30.0
        camera.view_up = [0.02378529603150923, -0.9934363629671287, -0.11188589020666041]
        camera.clipping_range = [4875.298234059459, 6735.995771914646]
    set_camera()

    mlab.show()
    # mlab.view()
    # import ipdb
    # ipdb.set_trace()

    # view the file with: $ ctmviewer shape.obj
    # note won't have color map
    mlab.savefig("shape.png")


if __name__ == '__main__':
    cli()