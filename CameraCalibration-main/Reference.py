import cv2
import numpy as np
import glob

# Load camera intrinsic parameters from calibration
#K = np.array([[1.14702331e+03, 0, 8.96065561e+02],
              #[0, 1.17412309e+03, 5.15706737e+02],
              #[0, 0, 1]])

K = np.array([[916.96292712, 0, 880.53070418],
              [0, 958.85773014, 542.8427698],
              [0, 0, 1]])

# Load camera extrinsic parameters from calibration
R = np.array([[-0.1074216 ],
              [ 0.17005636],
              [-0.24077069]])

t = np.array([[-1.65793151],
              [-3.07144717],
              [14.21431669]])

# Generate set of reference points in world coordinates
ref_points = np.array([
                       [1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]])


# Project reference points onto image plane
image_points, _ = cv2.projectPoints(ref_points, R, t, K, None, None, None, None)
cv2.projectPoints()

images = glob.glob('images/*.png')

for image in images:

    img = cv2.imread(image)

    # Draw reference frame axes in image
    x_axis = tuple(map(int, image_points[1].ravel()))
    y_axis = tuple(map(int, image_points[2].ravel()))
    z_axis = tuple(map(int, image_points[3].ravel()))
    cv2.line(img, tuple(
        map(int, image_points[0].ravel())), x_axis, (255, 0, 0), 2)
    cv2.line(img, tuple(
        map(int, image_points[0].ravel())), y_axis, (0, 255, 0), 2)
    cv2.line(img, tuple(
        map(int, image_points[0].ravel())), z_axis, (0, 0, 255), 2)

    # Display image with reference frame
    cv2.imshow('Reference Frame', img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
