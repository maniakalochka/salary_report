from salary_report.report.payout import PayoutReport


def test_payout_grouping_and_calculation():
    data = [
        {"name": "Alice", "department": "HR", "hours_worked": 160, "hourly_rate": 50},
        {"name": "Bob", "department": "HR", "hours_worked": 100, "hourly_rate": 40},
        {"name": "Carol", "department": "Dev", "hours_worked": 120, "hourly_rate": 60},
    ]

    report = PayoutReport().generate(data)

    assert set(report.keys()) == {"HR", "Dev"}
    assert report["HR"][0]["name"] == "Alice"
    assert report["HR"][0]["payout"] == 8000
    assert report["HR"][1]["payout"] == 4000
    assert report["Dev"][0]["payout"] == 7200
