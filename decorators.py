from models import ContactError, PhoneFormatError

def handle_input_error(error_message: str = "Invalid input."):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError, ContactError, PhoneFormatError) as e:
                if hasattr(e, "message"):
                    return f"{error_message}\nError: {e.message}"
                return error_message
        return wrapper
    return decorator
