from typing import Optional, Dict, Any

wimbledon_finals = {
    2021: {
        "champion": "Novak Djokovic",
        "runner_up": "Matteo Berrettini",
        "score": "6–7(4–7), 6–4, 6–4, 6–3",
        "sets": 4,
        "tiebreak": True
    },
    2022: {
        "champion": "Novak Djokovic",
        "runner_up": "Nick Kyrgios",
        "score": "4–6, 6–3, 6–4, 7–6(7–3)",
        "sets": 4,
        "tiebreak": True
    }
    # Add more years...
}

"""Connection for Databse"""
class WimbledonDataSource:
    """Stub for a real data source (DB/API)."""
    def get_final(self, year: int) -> Optional[Dict[str, Any]]:
        # TODO: Replace with DB/API call
        return wimbledon_finals.get(year)

# Singleton instance for use in routes
wimbledon_data_source = WimbledonDataSource()