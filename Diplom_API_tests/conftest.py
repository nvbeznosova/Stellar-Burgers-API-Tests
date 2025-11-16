import pytest
import random
import string

def random_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"

@pytest.fixture
def new_user():
    return {
        "email": random_email(),
        "password": "password123",
        "name": "Test User"
    }