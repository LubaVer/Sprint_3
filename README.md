# Тесты для приложения "Космический фастфуд"

## Локаторы
```
"//a[contains(text(), 'Зарегистрироваться')]" # Ссылка "Зарегистрироваться"
"//p[contains(text(),'Личный Кабинет')]" # Кнопка "Личный Кабинет"
"//input[@type = 'password']"  # Поле "Пароль"
"//div[contains(.,'Имя')]/input" # Поле 'Имя'
"//div[contains(.,'Email')]/input" # Поле 'Email'
"//button[contains(text(), 'Зарегистрироваться')]" # Кнопка "Зарегистрироваться" в форме регистрации
"//button[contains(text(),'Выход')]"  # Кнопка 'Выход'
"//h2[contains(text(), 'Вход')]"  # Заголовок 'Вход' в личном кабинете
"//a[contains(text(),'Профиль')]" # Ссылка "Профиль"
"//p[contains(text(), 'Конструктор')]"  # Кнопка 'Конструктор' на главной
"//button[contains(text(), 'Войти')]"  # Кнопка "Войти" на форме входа
"//a[contains(text(),'Войти')]" # Ссылка "Войти" в форме регистрации
"//a[contains(text(),'Восстановить пароль')]" # Ссылка 'Восстановить пароль'
"//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка "Войти в аккаунт" на главной
"//p[contains(text(), 'Некорректный пароль')]"  # подсказка об ошибке при вводе пароля 'Некорректный пароль'
"//button[contains(text(), 'Оформить заказ')]"  # Кнопка 'Оформить заказ' на главной
"//p[contains(text(),'Сыр с астероидной плесенью')]" # Карточка 'Сыр с астероидной плесенью'
"//p[contains(text(),'Флюоресцентная булка R2-D3')]" # Карточка 'Флюоресцентная булка R2-D3'
"//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]" # Карточка 'Мясо бессмертных моллюсков Protostomia
"//p[contains(text(),'Соус Spicy-X')]" # Карточка 'Соус Spicy-X'
"//h2[contains(text(),'Булки')]" # подзаголовок Булки
"//h2[contains(text(),'Соусы')]"  # подзаголовок Соусы
"//h2[contains(text(),'Начинки')]"  # подзаголовок Начинки
"//div[./span[contains(text(),'Булки')]]" # Кнопка Булки
"//div[./span[contains(text(),'Соусы')]]"  # Кнопка Соусы
"//div[./span[contains(text(),'Начинки')]]"  # Кнопка Начинки
```