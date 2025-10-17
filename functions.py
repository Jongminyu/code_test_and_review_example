def add(a, b):
    """Add two numbers."""
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b
def power(a,b):
    return a**b

def multiple(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        print("오류: 0으로 나눌 수 없습니다.")
        return None
    else: 
        return a / b