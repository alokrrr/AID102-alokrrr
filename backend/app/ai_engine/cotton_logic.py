from app.ai_engine.risk_scoring import calculate_risk_score


def analyze_cotton_soil(pH: float, nitrogen_level: str) -> dict:
    result = {
        "crop": "Cotton",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": "",
        "decision_factors": {},
        "alerts": []
    }

    explanation_parts = []
    nutrient_deficiencies = []
    nutrient_excesses = []

    # =======================
    # STEP 1: pH Evaluation
    # =======================
    if pH < 6.0:
        pH_status = "severe"
        result["soil_status"] = "Acidic"

        explanation_parts.append(
            "Soil pH is low. Cotton prefers slightly neutral soil."
        )

        result["recommendations"].append(
            "Apply lime to improve soil pH before sowing."
        )

        result["decision_factors"]["pH"] = "High impact (cotton sensitive to acidity)"

        result["alerts"].append({
            "type": "Soil Acidity",
            "severity": "High",
            "message": "Acidic soil detected. pH correction is critical for cotton."
        })

    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"
        result["decision_factors"]["pH"] = "Normal"

    # =========================
    # STEP 2: Nitrogen Evaluation
    # =========================
    if nitrogen_level.lower() == "high":
        nutrient_excesses.append("nitrogen")

        explanation_parts.append(
            "Excess nitrogen can promote vegetative growth and increase pest risk."
        )

        result["recommendations"].append(
            "Reduce nitrogen application to avoid excessive vegetative growth."
        )

        result["decision_factors"]["Nitrogen"] = "High impact (excess nitrogen)"

        result["alerts"].append({
            "type": "Nitrogen Excess",
            "severity": "Medium",
            "message": "Excess nitrogen may increase pest and weed growth."
        })

    elif nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")

        explanation_parts.append(
            "Low nitrogen can reduce cotton yield."
        )

        result["recommendations"].append(
            "Apply nitrogen fertilizer in recommended quantities."
        )

        result["decision_factors"]["Nitrogen"] = "Medium impact (low nitrogen)"

    else:
        result["decision_factors"]["Nitrogen"] = "Normal"

    # =====================
    # STEP 3: Crop Sensitivity
    # =====================
    result["decision_factors"]["Crop Sensitivity"] = (
        "High (cotton sensitive to both nitrogen excess and deficiency)"
    )

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

    if not result["recommendations"]:
        result["recommendations"].append(
            "Soil conditions are suitable for cotton cultivation."
        )

    return result
