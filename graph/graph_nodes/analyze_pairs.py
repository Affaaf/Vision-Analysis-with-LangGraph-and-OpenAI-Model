import os
import openai
from dotenv import load_dotenv
from utils.util import pil_to_base64
from utils.constants import Const

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# 🔹 Node 2: Analyze differences with GPT-4o
def analyze_pair(state):
    """
    Analyzes the differences between pairs of images using GPT-4o.

    This function takes pairs of images from the provided state, converts them to base64 format,
    and sends the images to the GPT-4o model for analysis. The model compares the images and 
    generates a summary of the differences between them.

    Args:
        state (dict): The state containing the image pairs to be analyzed. The key "image_pairs" 
                      should contain a list of image pairs to be processed.

    Returns:
        dict: The updated state containing the summaries of the image comparisons under the 
              key "summaries".
    
    Raises:
        KeyError: If the "image_pairs" key is not found in the provided state.
    """
    if "image_pairs" not in state:
        raise KeyError("[analyze_pair] image_pairs not found in state!")
    
    summaries = []
    for idx, (imgA, imgB) in enumerate(state["image_pairs"], 1):
        imgA_b64 = pil_to_base64(imgA)
        imgB_b64 = pil_to_base64(imgB)

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": Const.PROMPT
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{imgA_b64}",
                    },
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{imgB_b64}",
                    },
                    },
                ],
                }
            ],
            max_tokens=300,
        )
        summary = response.choices[0].message.content
        summaries.append(f"Pair {idx}: {summary}")
    state["summaries"] = summaries
    return state