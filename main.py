import logging
from graph.vision_graph import VisionGraphs
from graph.graph_visualizations.graph_visualization import visualize_graph


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    """
    Main entry point for executing the vision graph analysis and visualizing the graph.

    This function does the following:
    1. Initializes the state and sets up the VisionGraphs pipeline.
    2. Visualizes the vision graph and saves it as an image.
    3. Executes the vision graph, performing analysis on image pairs.
    4. Logs the final analysis report.
    """
    initial_state = {}
    graph = VisionGraphs()

    # Visualize and save the graph as an image
    visualize_graph()

    # Execute the graph
    final_state = graph.invoke(initial_state)
    logging.info("=== CHANGE REPORT ===\n")
    logging.info(final_state["final_report"])
