# backend/app/api/routes_soil.py

from fastapi import APIRouter, HTTPException
from app.services.soil_analysis import analyze_soil
from app.models.soil import SoilAnalysisRequest

router = APIRouter()


@router.post("/analyze-soil")
def analyze_soil_endpoint(payload: SoilAnalysisRequest):
    """
    API endpoint to analyze soil health using AI logic.
    """

    result = analyze_soil(
        crop=payload.crop,
        soil_data=payload.soil_data.dict()
    )

    if "error" in result:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return {
        "status": "success",
        "analysis": result
    }
