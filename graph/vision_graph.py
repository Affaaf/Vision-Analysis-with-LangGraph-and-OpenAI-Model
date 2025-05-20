from langgraph.graph import StateGraph, END
from graph.graph_nodes.base import States
from graph.graph_nodes.load_images import load_images
from graph.graph_nodes.analyze_pairs import analyze_pair
from graph.graph_nodes.aggregate_result import aggregate_results


def VisionGraphs():
    """
    Creates and compiles a state graph for analyzing image pairs and generating a report.

    This function builds a state graph that handles the following steps:
    1. Load images (`load_images`).
    2. Analyze differences between image pairs (`analyze_pair`).
    3. Aggregate and save the results (`aggregate_results`).

    The graph is constructed using the `StateGraph` class, where nodes are added for each step,
    and edges are defined to link the process flow. The entry point is set to the `load_images` node.

    Returns:
        StateGraph: A compiled state graph ready to be executed.
    """
    builder = StateGraph(States.ImageState)
    builder.add_node("load_images", load_images)
    builder.add_node("analyze_pair", analyze_pair)
    builder.add_node("aggregate_results", aggregate_results)

    builder.set_entry_point("load_images")
    builder.add_edge("load_images", "analyze_pair")
    builder.add_edge("analyze_pair", "aggregate_results")
    builder.add_edge("aggregate_results", END)

    return builder.compile()
