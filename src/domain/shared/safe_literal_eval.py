import ast
def safe_literal_eval(x, default):
    """Garante que literal_eval não quebre e retorna default se falhar."""
    if isinstance(x, (dict, list)):
        return x
    if isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except Exception:
            return default
    return default