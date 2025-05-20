import os
import logging
from graph.vision_graph import VisionGraphs


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def visualize_graph(output_dir: str = "graph/graph_visualizations/image") -> str:
    """
    Visualizes the vision graph and saves the generated image to the specified directory.

    Args:
        output_dir (str): The directory where the generated graph image will be saved. 
                          Defaults to "graph/graph_visualizations/image".

    Returns:
        str: The path to the saved graph image file.
    
    """
    graph = VisionGraphs()
    graph_image = graph.get_graph().draw_mermaid_png()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "vision_graph.png")
    with open(output_path, "wb") as f:
        f.write(graph_image)

    logger.info(f"Graph visualization saved to: {output_path}")
    return output_path
