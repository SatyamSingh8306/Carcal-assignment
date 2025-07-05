from pydantic import BaseModel, Field
from typing import Optional

class WimbledonQuery(BaseModel):
    year : int = Field(description="The year for which you want result")


class WimbledonResult(BaseModel):
    year: int = Field(..., description="The year of the final match")
    champion: Optional[str] = Field(default=None, description="The champion of the tournament")
    runner_up: Optional[str] = Field(default=None, description="The runner-up of the tournament")
    score: Optional[str] = Field(default=None, description="The full scoreline of the final match")
    sets: int = Field(default=0, description="Total number of sets played in the final")
    tiebreak: bool = Field(default=False, description="Indicates whether a tiebreak occurred in any set")





# {
# "year": 2021,
# "champion": "Novak Djokovic",
# "runner_up": "Matteo Berrettini",
# "score": "6-7(4-7), 6–4, 6–4, 6–3",
# "sets": 4,
# "tiebreak": true
# }