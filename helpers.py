import random
import string

def random_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"