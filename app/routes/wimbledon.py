from fastapi import APIRouter, HTTPException, Query
from app.types.response import WimbledonResult
from app.services.mapper import wimbledon_data_source
import logging

router = APIRouter(prefix="/wimbledon")

logger = logging.getLogger("wimbledon")

@router.get("/", response_model=WimbledonResult)
async def get_wimbledon_final(year: int = Query(..., description="The year for which you want result")):
    result = wimbledon_data_source.get_final(year)
    if not result:
        logger.warning(f"No Wimbledon final data found for year {year}")
        raise HTTPException(status_code=404, detail=f"No Wimbledon final data found for year {year}")
    return result