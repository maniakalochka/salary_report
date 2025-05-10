import sys

import pytest

from salary_report.__main__ import main


def test_main_execution(monkeypatch) -> None:
    test_file = "data/data1.csv"
    monkeypatch.setattr(sys, "argv", ["main", test_file, "--report", "payout"])
    main()


def test_invalid_report(monkeypatch):
    monkeypatch.setattr(
        sys, "argv", ["main", "data/data1.csv", "--report", "invalid_report"]
    )
    with pytest.raises(ValueError, match="Unknown report type: invalid_report"):
        main()
