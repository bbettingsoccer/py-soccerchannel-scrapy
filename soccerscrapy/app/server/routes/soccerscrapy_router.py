from fastapi import APIRouter, Body

from soccerscrapy.app.server.model.scrapyplan_model import ScrapyplanModel
from soccerscrapy.app.server.service.soccerscrapyplan_service import SoccerScrapyPlanService

router = APIRouter()


@router.post("/scrapy/planner/", response_description="Match retrieved")
async def post(data: ScrapyplanModel = Body(...)):
    try:
        service = SoccerScrapyPlanService(data)
        service.scrapyPlanFacade()
        return "Success"
    except Exception as e:
        print("Error ", e)
