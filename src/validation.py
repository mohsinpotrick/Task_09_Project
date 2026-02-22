def validate_input(user_input: dict):
    """
    Validate user inputs before prediction.
    Raises ValueError with helpful messages.
    """

    required_fields = [
        "age", "sex", "bmi", "children",
        "smoker", "region_northwest",
        "region_southeast", "region_southwest"
    ]

    for field in required_fields:
        if field not in user_input:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(user_input["age"], (int, float)):
        raise ValueError("Age must be numeric.")
    if not 18 <= user_input["age"] <= 100:
        raise ValueError("Age must be between 18 and 100.")

    if not 10 <= user_input["bmi"] <= 60:
        raise ValueError("BMI must be between 10 and 60.")

    if user_input["children"] < 0:
        raise ValueError("Children cannot be negative.")

    if user_input["smoker"] not in [0, 1]:
        raise ValueError("Smoker must be 0 (No) or 1 (Yes).")

    if user_input["sex"] not in [0, 1]:
        raise ValueError("Sex must be 0 or 1.")

    return True