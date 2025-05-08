from collections import defaultdict
from typing import Any

from .base import BaseReport


class PayoutReport(BaseReport):
    def generate(self, data) -> dict[Any, list[Any]]:
        result = defaultdict(list)
        for row in data:
            payout = row["hourly_rate"] * row["hours_worked"]
            result[row["department"]].append({
                "name": row["name"],
                "hours": row["hours_worked"],
                "rate": row["hourly_rate"],
                "payout": payout
            })
        return dict(result)
