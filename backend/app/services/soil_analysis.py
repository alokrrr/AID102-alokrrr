# backend/app/services/soil_analysis.py

from app.ai_engine.wheat_logic import analyze_wheat_soil
from app.ai_engine.rice_logic import analyze_rice_soil
from app.ai_engine.cotton_logic import analyze_cotton_soil


def analyze_soil(crop: str, soil_data: dict) -> dict:
    crop = crop.lower()

    pH = soil_data.get("pH")
    nitrogen = soil_data.get("nitrogen")
    potassium = soil_data.get("potassium")

    if crop == "wheat":
        return analyze_wheat_soil(
            pH=pH,
            nitrogen_level=nitrogen
        )

    elif crop == "rice":
        if potassium is None:
            return {"error": "Potassium value is required for rice analysis"}
        return analyze_rice_soil(
            pH=pH,
            nitrogen_level=nitrogen,
            potassium_level=potassium
        )

    elif crop == "cotton":
        if potassium is None:
            return {"error": "Potassium value is required for cotton analysis"}
        return analyze_cotton_soil(
            pH=pH,
            nitrogen_level=nitrogen,
            potassium_level=potassium
        )

    return {"error": f"Crop '{crop}' is not supported"}
