import datetime

def log_action(action_name: str):
    """
    Decorador para registrar acciones en la consola.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Acción: {action_name}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator