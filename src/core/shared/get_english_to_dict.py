import ast

def get_english(v):
    if isinstance(v, dict):
        return v.get('english', '').title()
    if isinstance(v, str):
        try:
            d = ast.literal_eval(v)
            return d.get('english', '').title()
        except:
            return None
    return None