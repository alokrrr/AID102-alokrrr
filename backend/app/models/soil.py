# backend/app/models/soil.py

from pydantic import BaseModel, Field
from typing import Optional, Literal


class SoilData(BaseModel):
    pH: float = Field(..., ge=0.0, le=14.0, description="Soil pH value")
    nitrogen: Literal["low", "medium", "high"]
    potassium: Optional[Literal["low", "medium", "high"]] = None


class SoilAnalysisRequest(BaseModel):
    crop: Literal["wheat", "rice", "cotton"]
    soil_data: SoilData
