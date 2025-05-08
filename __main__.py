import argparse

from .output import print_report
from .parser import load_data
from .report.payout import PayoutReport


def main() -> None:
    parser = argparse.ArgumentParser(description="Salary report generator")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument("--report", required=True, help="Type of report to generate (e.g., payout)")
    args = parser.parse_args()

    data = []
    for file in args.files:
        data.extend(load_data(file))

    if args.report == "payout":
        report = PayoutReport().generate(data)
        print_report(report)
    else:
        raise ValueError(f"Unknown report type: {args.report}")


if __name__ == "__main__":
    main()
