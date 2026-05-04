
FORMULAS = {
    "default": "0.6*revenue + 0.3*ctr + 0.1*engagement - 0.2*latency",
    "growth":  "0.4*revenue + 0.4*ctr + 0.2*new_users",
    "profit":  "1.0*revenue - 0.5*cost"
}

def get_formula(name="default"):
    return FORMULAS.get(name, FORMULAS["default"])

def set_formula(name, expr):
    FORMULAS[name] = expr
