import re

def email_valido(email):
    """Valida que el email tenga un formato correcto."""
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)