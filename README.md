Проект предназначен для тестирования сайта https://stellarburgers.nomoreparties.site/

Используются библиотеки: 
    selenium.webdriver для взаимодейтсвия с браузером
    string и random для генерации пароля

Описание тестов:
    test_registration_valid_credentials - позитивный, на регистрацию
    test_registration_with_too_short_password - негативный, пароль 5 символов

    test_login_from_home_page - позитивный, логинимся с главной странице
    test_login_from_account_page - позитивный, логинимся со страницы личного кабинета
    test_login_from_registration_page - позитивный, логинимся со страницы регистрации
    test_login_from_password_recovery_page - позитивный, логинимся со страницы восстановления пароля

    test_logout_from_account - позитивный, выходим из профиля пользователя

    test_open_account - проверяем содержание страницы профиля

    test_open_constructor_click_on_button - открытие конструктора по клику на соответсвующую кнопку
    test_open_constructor_click_on_logo - открытие конструктора по клику на логотип
    test_go_to_section_sauce - проверяем переход по разделам конструктора
    test_go_to_section_filling - проверяем переход по разделам конструктора
    test_go_to_section_bun - проверяем переход по разделам конструктора