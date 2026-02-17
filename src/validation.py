def validate_input(user_input: dict):
    """
    Validate user inputs before prediction.
    Raises ValueError if invalid.
    """

    if user_input["age"] < 18 or user_input["age"] > 100:
        raise ValueError("Age must be between 18 and 100.")

    if user_input["bmi"] < 10 or user_input["bmi"] > 60:
        raise ValueError("BMI must be between 10 and 60.")

    if user_input["children"] < 0:
        raise ValueError("Children cannot be negative.")

    if user_input["smoker"] not in [0, 1]:
        raise ValueError("Smoker must be 0 or 1.")

    return True