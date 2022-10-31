import os

import numpy as np
import cv2 as cv


def read_image(image_path):
    """Read an image.

    Args:
        image_path (str): Path to the image.

    Returns:
        numpy.ndarray: Image.
    """

    return cv.imread(image_path)


def prep_image(image):
    """Preprocess an image converting it to grayscale.

    Args:
        image (numpy.ndarray): Image to preprocess.

    Returns:
        numpy.ndarray: Preprocessed image.
    """

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray


def show_image(image, window_name='image'):
    """Show an image.

    Args:
        image (numpy.ndarray): Image to show.
        window_name (str, optional): Name of the window. Defaults to 'image'.
    """

    cv.imshow(window_name, image)
    cv.waitKey(0)
    cv.destroyAllWindows()


sudoku_image_path = 'img/Sudoku_1_original.png'
sudoku_image = read_image(sudoku_image_path)
sudoku_image = prep_image(sudoku_image)
show_image(sudoku_image)
