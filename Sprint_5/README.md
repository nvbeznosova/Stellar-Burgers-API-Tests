# Проект: Тестирование Stellar Burgers

## Описание

Проект содержит автоматические тесты сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site/) с использованием Selenium и pytest.

Тесты покрывают следующие функции:

1. **Регистрация**
   - Успешная регистрация нового пользователя
   - Ошибка при вводе некорректного пароля

2. **Вход**
   - Вход через кнопку «Войти в аккаунт» на главной
   - Вход через форму регистрации и восстановления пароля

3. **Личный кабинет**
   - Переход в личный кабинет
   - Переход в конструктор через кнопку «Конструктор» и логотип
   - Выход из аккаунта

4. **Конструктор**
   - Проверка переходов между разделами: «Булки», «Соусы», «Начинки»

5. **Структура проекта**

my_first_vscode_project/
├── .vscode/
├── .venv/
├── Sprint_5/
│ ├── tests/
│ │ ├── conftest.py
│ │ ├── test_constructor.py
│ │ ├── test_login.py
│ │ ├── test_personal_account.py
│ │ └── test_registration.py
│ ├── locators/
│ │ ├── constructor_page_locators.py
│ │ ├── login_page_locators.py
│ │ ├── personal_account_locators.py
│ │ └── registration_page_locators.py
│ └── utils.py
├── README.md
└── .gitignore

6. **Как запускать тесты**

1. Активировать виртуальное окружение:

```bash
source .venv/bin/activate

2. Запустить тест через pytest:
pytest Sprint_5/tests/

Все тесты автономны: открывают браузер Chrome, выполняют проверку и закрывают браузер с помощью driver.quit().

7. **Генерация логинов и паролей**
from utils import generate_email, generate_password

email = generate_email()
password = generate_password()

8. **Требования**
Python 3.13+
Selenium
Webdriver Manager
pytest
Google Chrome