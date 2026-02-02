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
        "alerts": [],
        "confidence": None,
        "confidence_reason": ""
    }

    explanation_parts = []
    nutrient_deficiencies = []
    nutrient_excesses = []

    # =======================
    # STEP 1: pH Evaluation
    # =======================
    result["decision_flow"].append("Evaluated soil pH level")

    if pH < 5.5:
        pH_status = "severe"
        result["soil_status"] = "Acidic"

        explanation_parts.append(
            "Soil pH is too low. Acidic soil reduces nutrient availability for wheat."
        )

        result["recommendations"].append(
            "Apply lime to correct soil acidity before adding fertilizers."
        )

        result["decision_factors"]["pH"] = "High impact (acidic soil)"

        result["alerts"].append({
            "type": "Soil Acidity",
            "severity": "High",
            "message": "Soil is acidic. Lime application is required before fertilization."
        })

        result["decision_flow"].append("Detected acidic soil condition")

    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"
        result["decision_factors"]["pH"] = "Normal"

    # =========================
    # STEP 2: Nitrogen Evaluation
    # =========================
    result["decision_flow"].append("Evaluated nitrogen availability")

    if nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")

        explanation_parts.append(
            "Nitrogen level is low. Wheat requires nitrogen for healthy vegetative growth."
        )

        result["recommendations"].append(
            "Apply nitrogen fertilizer (urea) in split doses."
        )

        result["decision_factors"]["Nitrogen"] = "Medium impact (low nitrogen)"

        result["alerts"].append({
            "type": "Nitrogen Deficiency",
            "severity": "Medium",
            "message": "Low nitrogen detected. Apply nitrogen fertilizer appropriately."
        })

        result["decision_flow"].append("Detected nitrogen deficiency")

    else:
        result["decision_factors"]["Nitrogen"] = "Normal"

    # =====================
    # STEP 3: Crop Sensitivity
    # =====================
    result["decision_factors"]["Crop Sensitivity"] = (
        "High (wheat sensitive to acidic soil and nitrogen deficiency)"
    )

    # =====================
    # STEP 4: Risk Scoring
    # =====================
    result["decision_flow"].append(
        "Calculated overall soil risk using combined stress factors"
    )

    risk = calculate_risk_score(
        pH_status=pH_status,
        nutrient_deficiencies=nutrient_deficiencies,
        nutrient_excesses=nutrient_excesses
    )

    result["risk_level"] = risk["risk_level"]
    result["explanation"] = " ".join(explanation_parts)

    if not result["recommendations"]:
        result["recommendations"].append(
            "Soil conditions are suitable for wheat cultivation."
        )

    # =====================
    # STEP 5: Confidence Scoring
    # =====================
    confidence = 1.0
    confidence_reasons = []

    if pH_status == "severe":
        confidence -= 0.2
        confidence_reasons.append("Severe soil acidity increases uncertainty")

    if nutrient_deficiencies or nutrient_excesses:
        confidence -= 0.1
        confidence_reasons.append("Nutrient imbalance affects prediction certainty")

    confidence = max(0.5, round(confidence, 2))
    result["confidence"] = confidence

    if confidence_reasons:
        result["confidence_reason"] = "; ".join(confidence_reasons)
    else:
        result["confidence_reason"] = "High confidence based on stable soil conditions"

    return result
