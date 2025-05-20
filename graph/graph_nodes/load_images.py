import os
from PIL import Image
import logging
from utils.constants import Const


def load_images(state):
    """
    Loads predefined pairs of images from the specified directory and appends them to the state.

    This function looks for image files in the format:
        - pair1imageA.png, pair1imageB.png
        - pair2imageA.png, pair2imageB.png
        - ...
    
    The base path is defined in `Const.IMAGES_BASE_PATH`. It raises an error if any image file is missing
    or fails to load.

    Args:
        state (dict): The current state of the workflow.

    Returns:
        dict: Updated state containing a list of image pairs under the key 'image_pairs'.

    Raises:
        FileNotFoundError: If any expected image file is not found.
        RuntimeError: If an image cannot be loaded successfully.
    """
    image_pairs = []
    base_path = Const.IMAGES_BASE_PATH

    for i in range(1, 5):
        imgA_path = os.path.join(base_path, f"pair{i}imageA.png")
        imgB_path = os.path.join(base_path, f"pair{i}imageB.png")

        # Check if files exist
        if not os.path.exists(imgA_path) or not os.path.exists(imgB_path):
            raise FileNotFoundError(f"Missing image: {imgA_path} or {imgB_path}")

        try:
            imgA = Image.open(imgA_path)
            imgB = Image.open(imgB_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load images for pair {i}: {e}")

        image_pairs.append((imgA, imgB))

    logging.info(f"[load_images] Loaded {len(image_pairs)} image pairs")
    state["image_pairs"] = image_pairs
    return state
