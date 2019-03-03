from typing import DefaultDict

import cv2 as cv
import numpy as np

from autofocus.data.constants import PathOrStr
from autofocus.data.helpers import has_channels_equal


def record_is_grayscale(
    image: np.array, inpath: PathOrStr, log_dict: DefaultDict[str, dict]
) -> None:
    """
    Record whether image is grayscale.

    In this dataset, grayscale images have been saved as three-channel
    images with all three channels equal, so this function checks for
    equality across channels rather than the number of channels.

    Parameters
    ----------
    image
    inpath
        Image input path
    log_dict
        Dictionary of image metadata

    Side effect
    -----------
    Adds a "mean_brightness" items to log_dict[inpath]
    """
    is_grayscale = has_channels_equal(image)

    log_dict[inpath]["grayscale"] = int(is_grayscale)

    return image


def record_mean_brightness(
    image: np.array, inpath: PathOrStr, log_dict: DefaultDict[str, dict]
) -> np.array:
    """
    Record whether image is grayscale.

    In this dataset, grayscale images have been saved as three-channel
    images with all three channels equal, so this function checks for
    equality across channels rather than the number of channels.

    Parameters
    ----------
    image
    inpath
        Image input path
    log_dict
        Dictionary of image metadata

    Side effect
    -----------
    Adds a "mean_brightness" items to log_dict[inpath]
    """
    is_grayscale = has_channels_equal(image)

    if is_grayscale:
        image_gray = image
    else:
        image_gray = cv.cvtColor(src=image, code=cv.COLOR_RGB2GRAY)

    log_dict[inpath]["mean_brightness"] = image_gray.mean()

    return image
