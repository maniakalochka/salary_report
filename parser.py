from typing import Any


def normalize_column_name(name: str) -> str:
    name = name.lower().strip()
    if name in ("rate", "salary"):
        return "hourly_rate"
    return name


def load_data(filepath: str) -> list[Any]:
    with open(filepath, 'r') as file:
        lines = file.readlines()
    headers = [normalize_column_name(h.strip()) for h in lines[0].split(",")]
    rows = []

    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        row = dict(zip(headers, values))
        row["hourly_rate"] = float(row["hourly_rate"])  # type: ignore
        row["hours_worked"] = int(row["hours_worked"])  # type: ignore
        rows.append(row)
    return rows
