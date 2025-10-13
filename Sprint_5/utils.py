import random
import string

def generate_email(name="nadia_beznosova_31"):
    """
    Генерирует уникальный email для теста регистрации.
    По умолчанию использует указанное имя и случайные 3 цифры.
    """
    random_digits = random.randint(100, 999)  # три случайные цифры
    return f"{name}_{random_digits}@yandex.ru"

def generate_password(length=8, use_special_chars=True):
    """
    Генерирует случайный пароль.
    length - длина пароля (по умолчанию 8)
    use_special_chars - добавлять ли специальные символы
    """
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += "!@#$%^&*"
    return ''.join(random.choices(chars, k=length))