import os
import pandas as pd
from utils import clean_data, compare_prices

def main(input_file):
    # Step 1: Clean the data
    internal_data = clean_data(input_file)
    if internal_data is None:
        return

    # Step 2: Compare prices
    insights = compare_prices(internal_data)

    # Step 3: Save report
    report_path = "report.md"
    with open(report_path, "w") as report:
        report.write("# Price Comparison Insights\n")
        report.write(insights.to_markdown(index=False))
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analysis.py <path_to_csv>")
    else:
        main(sys.argv[1])
