
class Locators:
    register_button_link = "//a[contains(text(), 'Зарегистрироваться')]" # Ссылка "Зарегистрироваться"
    personal_acc_button = "//p[contains(text(),'Личный Кабинет')]" # Кнопка "Личный Кабинет"
    password_reg = "//input[@type = 'password']"  # Поле "Пароль"
    name_reg = "//div[contains(.,'Имя')]/input" # Поле 'Имя'
    email_reg = "//div[contains(.,'Email')]/input" # Поле 'Email'
    register_button = "//button[contains(text(), 'Зарегистрироваться')]" # Кнопка "Зарегистрироваться" в форме регистрации
    exit_button = "//button[contains(text(),'Выход')]"  # Кнопка 'Выход'
    enter_header_in_personal_acc = "//h2[contains(text(), 'Вход')]"  # Заголовок 'Вход' в личном кабинете
    profile_link = "//a[contains(text(),'Профиль')]" # Ссылка "Профиль"
    constructor_button = "//p[contains(text(), 'Конструктор')]"  # Кнопка 'Конструктор' на главной
    enter_button = "//button[contains(text(), 'Войти')]"  # Кнопка "Войти" на форме входа
    enter_link = "//a[contains(text(),'Войти')]" # Ссылка "Войти" в форме регистрации
    restore_password_link = "//a[contains(text(),'Восстановить пароль')]" # Ссылка 'Восстановить пароль'
    enter_acc_button = "//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка "Войти в аккаунт" на главной
    incorrect_password_hint = "//p[contains(text(), 'Некорректный пароль')]"  # подсказка об ошибке при вводе пароля 'Некорректный пароль'
    place_order_button = "//button[contains(text(), 'Оформить заказ')]"  # Кнопка 'Оформить заказ' на главной
    card_cheese = "//p[contains(text(),'Сыр с астероидной плесенью')]" # Карточка 'Сыр с астероидной плесенью'
    card_bulka = "//p[contains(text(),'Флюоресцентная булка R2-D3')]" # Карточка 'Флюоресцентная булка R2-D3'
    card_meat = "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]" # Карточка 'Мясо бессмертных моллюсков Protostomia
    card_sous = "//p[contains(text(),'Соус Spicy-X')]" # Карточка 'Соус Spicy-X'
    bulki_header = "//h2[contains(text(),'Булки')]" # подзаголовок Булки
    sous_header = "//h2[contains(text(),'Соусы')]"  # подзаголовок Соусы
    nachinki_header = "//h2[contains(text(),'Начинки')]"  # подзаголовок Начинки
    bulki_button = "//div[./span[contains(text(),'Булки')]]" # Кнопка Булки
    sous_button = "//div[./span[contains(text(),'Соусы')]]"  # Кнопка Соусы
    nachinki_button = "//div[./span[contains(text(),'Начинки')]]"  # Кнопка Начинки

