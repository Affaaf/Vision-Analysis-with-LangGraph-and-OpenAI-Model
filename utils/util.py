import base64
from io import BytesIO
from PIL import Image


def pil_to_base64(image: Image.Image) -> str:
    buffer = BytesIO()
    image.save(buffer, format="png")
    return base64.b64encode(buffer.getvalue()).decode()
