import os
import tempfile

import pytest

from salary_report.parser import load_data, normalize_column_name

CSV_VARIANTS = [
    ("hourly_rate", "60"),
    ("rate", "70"),
    ("salary", "50")
]


@pytest.mark.parametrize("rate_col, rate_val", CSV_VARIANTS)
def test_load_data_with_different_column_names(rate_col, rate_val):
    csv_content = f"id, email, name, department, hours_worked, {rate_col}\n" \
                        f"1, robert@example.com, Robert Smith, Marketing, 160, {rate_val}\n"
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file.write(csv_content)
        temp_file_path = temp_file.name
    try:
        data = load_data(temp_file_path)
        assert len(data) == 1
        entry = data[0]
        assert entry["name"] == "Robert Smith"
        assert entry["department"] == "Marketing"
        assert entry["hours_worked"] == 160
        assert entry["hourly_rate"] == float(rate_val)
    finally:
        os.remove(temp_file_path)


def test_load_data_multiple_rows():
    csv_content = """id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
"""

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write(csv_content)
        tmp_path = tmp.name

    try:
        data = load_data(tmp_path)
        assert len(data) == 2
        assert data[0]["name"] == "Alice Johnson"
        assert data[1]["name"] == "Bob Smith"
    finally:
        os.remove(tmp_path)