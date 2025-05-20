import os
import logging
from utils.constants import Const

def aggregate_results(state):
    """
    Aggregates the analysis into final report and saves it to a text file.

    This function takes the pair comparisons, combines them into a single 
    report, and then saves this report to a text file in the specified output directory.

    Args:
        state (dict): The state containing the "summaries" key, which holds the individual 
                      summaries for each image pair. The report will be created using this data.

    Returns:
        dict: The updated state with the "final_report" key containing the aggregated report.

    Raises:
        OSError: If there is an issue creating the output directory or saving the report file.
    """
    report = "\n\n".join(state["summaries"])
    state["final_report"] = report

    # Save to a text file
    os.makedirs(Const.OUTPUT_PATH, exist_ok=True)
    output_path = os.path.join(Const.OUTPUT_PATH, Const.REPORT_FILE_NAME)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    logging.info(f"Analyses Report Saved Successfully in {output_path}")
    return state
