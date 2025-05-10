import argparse

from .output import console_output, json_output
from .parser import load_data
from .report.payout import PayoutReport

REPORTS = {"payout": PayoutReport}


def main() -> None:
    parser = argparse.ArgumentParser(description="Salary report generator")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument(
        "--report", required=True, help="Type of report to generate (e.g., payout)"
    )
    parser.add_argument("--output", default="report.json", help="Path to JSON output file")
    args = parser.parse_args()

    data = []
    for file in args.files:
        data.extend(load_data(file))
    report_cls = REPORTS.get(args.report)
    if not report_cls:
        raise ValueError(f"Unknown report type: {args.report}")
    report_instance = report_cls()
    report_data = report_instance.generate(data)

    console_output.ConsoleOutput().save(report_data)
    json_output.JSONOutput().save(report_data, "report.json")


if __name__ == "__main__":
    main()
