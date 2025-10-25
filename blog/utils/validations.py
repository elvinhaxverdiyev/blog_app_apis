def check_password_length(password: str)-> bool:
    """
    Validates that the password length is between 4 and 10 characters.
    Returns True if valid, False otherwise.
    """
    return 4 <= len(password) <= 10


