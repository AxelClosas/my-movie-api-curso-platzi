from jwt import encode, decode


def create_token(data: dict) -> str:
    """Función que genera un token

    Args:
        data (dict): Datos a tokenizar

    Returns:
        str: Token
    """
    token: str = encode(payload=data, key="my_secrete_key", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    """Función para validar el token

    Args:
        token (str): Token

    Returns:
        dict: Datos en formato diccionario
    """
    data: dict = decode(token, key="my_secrete_key", algorithms=["HS256"])
    return data
