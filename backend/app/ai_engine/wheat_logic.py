from unittest import result
from app.ai_engine.risk_scoring import calculate_risk_score


def analyze_wheat_soil(pH: float, nitrogen_level: str) -> dict:
    result = {
        "crop": "Wheat",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": "",
        "decision_factors": {},
        "decision_flow": [],
        "alerts": []
    }


    explanation_parts = []
    nutrient_deficiencies = []
    nutrient_excesses = []

    # =======================
    # STEP 1: pH Evaluation
    # =======================
    if pH < 5.5:
        pH_status = "severe"
        result["soil_status"] = "Acidic"

        explanation_parts.append(
            "Soil pH is too low. Acidic soil reduces nutrient availability for wheat."
        )

        result["recommendations"].append(
            "Apply lime to correct soil acidity before adding fertilizers."
        )

        # Explainable AI factor
        result["decision_factors"]["pH"] = "High impact (acidic soil)"

        # Alert
        result["alerts"].append({
            "type": "Soil Acidity",
            "severity": "High",
            "message": "Soil is acidic. Lime application is required before fertilization."
        })

    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"
        result["decision_factors"]["pH"] = "Normal"
        result["decision_flow"].append("Evaluated soil pH level")

        if pH < 5.5:
            result["decision_flow"].append("Detected acidic soil condition")


    # =========================
    # STEP 2: Nitrogen Evaluation
    # =========================
    if nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")

        explanation_parts.append(
            "Nitrogen level is low. Wheat requires nitrogen for healthy vegetative growth."
        )

        result["decision_factors"]["Nitrogen"] = "Medium impact (low nitrogen)"

        if pH_status == "normal":
            result["recommendations"].append(
                "Apply nitrogen fertilizer (urea) in split doses."
            )

        # Alert
        result["alerts"].append({
            "type": "Nitrogen Deficiency",
            "severity": "Medium",
            "message": "Low nitrogen detected. Apply nitrogen fertilizer appropriately."
        })

    else:
        result["decision_factors"]["Nitrogen"] = "Normal"
        result["decision_flow"].append("Evaluated nitrogen availability")

        if nitrogen_level.lower() == "low":
            result["decision_flow"].append("Detected nitrogen deficiency")


    # =====================
    # STEP 3: Crop Sensitivity
    # =====================
    result["decision_factors"]["Crop Sensitivity"] = (
        "High (wheat is sensitive to acidic soil and nitrogen deficiency)"
    )
    result["decision_flow"].append("Calculated overall soil risk using combined stress factors")

    # =====================
    # STEP 4: Risk Scoring
    # =====================
    risk = calculate_risk_score(
        pH_status=pH_status,
        nutrient_deficiencies=nutrient_deficiencies,
        nutrient_excesses=nutrient_excesses
    )

    result["risk_level"] = risk["risk_level"]
    result["explanation"] = " ".join(explanation_parts)

    # =====================
    # STEP 5: Default Safe Case
    # =====================
    if not result["recommendations"]:
        result["recommendations"].append(
            "Soil conditions are suitable for wheat cultivation."
        )

    return result
