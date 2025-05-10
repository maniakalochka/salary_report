import json
import os

from salary_report.output.console_output import ConsoleOutput
from salary_report.output.json_output import JSONOutput


def test_console_output_formatting(capsys):
    data = {"Design": [{"name": "Bob Smith", "hours": 150, "rate": 40, "payout": 6000}]}
    ConsoleOutput().save(data)
    captured = capsys.readouterr()
    assert "Bob Smith" in captured.out
    assert "$6000" in captured.out


def test_json_output_creates_file(tmp_path):
    data = {"Design": [{"name": "Bob Smith", "hours": 150, "rate": 40, "payout": 6000}]}
    json_output = JSONOutput()
    json_output.save(data, os.path.join(tmp_path, "report.json"))
    assert os.path.exists(os.path.join(tmp_path, "report.json"))
    with open(os.path.join(tmp_path, "report.json"), "r") as f:
        loaded_data = json.load(f)
        assert loaded_data == data
