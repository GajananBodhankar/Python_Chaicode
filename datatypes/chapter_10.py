# decorators=========================================================
from functools import wraps

def my_decorator(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function runs", args, kwargs)
        result = func(*args, **kwargs)
        print("After function runs", result)
        return result
    return wrapper;

@my_decorator
def greet(name):
    print("Hello I am a decorator", name)

greet("Gajanan")
print("name is ", greet.__name__)