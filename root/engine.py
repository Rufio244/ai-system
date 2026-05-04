import math

SAFE_FUNCS = {
    "log": lambda x: math.log(max(x, 1e-9)),
    "exp": math.exp,
    "sqrt": math.sqrt,
    "max": max,
    "min": min,
}

def evaluate(expr: str, context: dict):
    # จำกัด namespace เพื่อความปลอดภัย
    env = {}
    env.update(SAFE_FUNCS)
    env.update(context)
    return eval(expr, {"__builtins__": {}}, env)
