from app.ai_engine.risk_scoring import calculate_risk_score


def analyze_rice_soil(pH: float, nitrogen_level: str) -> dict:
    result = {
        "crop": "Rice",
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
    if pH < 5.5:
        pH_status = "severe"
        result["soil_status"] = "Acidic"

        explanation_parts.append(
            "Soil pH is low. Rice tolerates acidity but extreme acidity reduces yield."
        )

        result["recommendations"].append(
            "Apply lime gradually to improve soil pH."
        )

        result["decision_factors"]["pH"] = "Medium impact (acidic but rice-tolerant)"

        result["alerts"].append({
            "type": "Soil Acidity",
            "severity": "Medium",
            "message": "Soil is acidic. Controlled pH correction is recommended."
        })

    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"
        result["decision_factors"]["pH"] = "Normal"

    # =========================
    # STEP 2: Nitrogen Evaluation
    # =========================
    if nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")

        explanation_parts.append(
            "Nitrogen level is low. Rice is a nitrogen-intensive crop."
        )

        result["recommendations"].append(
            "Apply nitrogen fertilizer in split doses during growth stages."
        )

        result["decision_factors"]["Nitrogen"] = "High impact (rice is nitrogen-hungry)"

        result["alerts"].append({
            "type": "Nitrogen Deficiency",
            "severity": "High",
            "message": "Low nitrogen detected. Immediate nitrogen supplementation required."
        })

    else:
        result["decision_factors"]["Nitrogen"] = "Normal"

    # =====================
    # STEP 3: Crop Sensitivity
    # =====================
    result["decision_factors"]["Crop Sensitivity"] = (
        "High (rice requires consistent nitrogen supply)"
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
            "Soil conditions are suitable for rice cultivation."
        )

    return result
