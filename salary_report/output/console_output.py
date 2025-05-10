from .base import OutputFormat


class ConsoleOutput(OutputFormat):

    def save(self, data: dict, filepath: str | None = None) -> None:
        for dept, entries in data.items():
            print(dept)
            total_hours = total_payout = 0
            for entry in entries:
                print(f"-------------- {entry['name']:<20} {entry['hours']:<5}"
                      f"{int(entry['rate']):<5} ${int(entry['payout'])}")
                total_hours += entry["hours"]
                total_payout += entry["payout"]
            print(f"{'':<34}{total_hours:<10}${int(total_payout)}\n")
