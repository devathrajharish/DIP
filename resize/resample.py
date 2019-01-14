import numpy as np
import math
from resize import interpolation

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):

        w1 = image.shape[0]
        h1 = image.shape[1]
        w2 = int(fx * w1)
        h2 = int(fy * h1)
        output_image = np.zeros((w2, h2), np.uint8)
        for i in range(w2):
            for j in range(h2):
             px = round((i * (w1 -1)) / (w2 - 1))
             py = round((j * (h1 -1)) / (h2 - 1))
             output_image[i][j] = image[px][py]

        return output_image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        width, height = image.shape[:2]
        nw = int(width * fx)
        nh = int(height * fy)
        new_img = np.zeros((nw, nh), np.uint8)
        inter = interpolation.interpolation()
        for i in range(nw):
            for j in range(nh):
                ii = int(np.floor((i * (image.shape[0]-1))/(nw - 1)))
                jj = int(np.floor((j * (image.shape[1]-1))/(nh - 1)))

                # All four corner pixels copied as it is
                if (ii == 0 and jj == 0) or \
                        (ii == 0 and jj == image.shape[1] - 1) or \
                        (ii == image.shape[0] - 1 and jj == 0) or \
                        (ii == image.shape[0] - 1 and jj == image.shape[1] - 1):
                    new_img[i][j] = image[ii][jj]

                # Linear interpolation along left and right edges
                elif ii == 0 or ii == image.shape[0] - 1:
                    new_img[i][j] = inter.linear_interpolation([jj - 1, image[ii][jj - 1]], [jj + 1, image[ii][jj + 1]], jj)

                # Linear interpolation along top and bottom edges
                elif jj == 0 or jj == image.shape[1] - 1:
                    new_img[i][j] = inter.linear_interpolation([ii - 1, image[ii - 1][jj]],  [ii + 1, image[ii + 1][jj]], ii)

                else:

                    q11i, q11j = ii - 1, jj - 1
                    q12i, q12j = ii - 1, jj + 1
                    q21i, q21j = ii + 1, jj - 1
                    q22i, q22j = ii + 1, jj + 1

                    point_a = [q11i, q11j, image[q11i][q11j]]
                    point_b = [q12i, q12j, image[q12i][q12j]]
                    point_c = [q21i, q21j, image[q21i][q21j]]
                    point_d = [q22i, q22j, image[q22i][q22j]]
                    unknown = [ii, jj]

                    new_img[i][j] = inter.bilinear_interpolation(point_a, point_b, point_c, point_d, unknown)

        return new_img

