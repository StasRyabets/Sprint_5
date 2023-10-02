# fields
name_field = "//label[text()='Имя']/following-sibling::input[@type='text']"
email_field = "//label[text()='Email']/following-sibling::input[@type='text']"
password_field = "//label[text()='Пароль']/following-sibling::input[@type='password']"

# buttons
reg_button = "//button[text()='Зарегистрироваться']"
constructor_button = '//p[text()="Конструктор"]'
sauce_button = "//div[contains(span, 'Соусы')]"
filling_button = "//div[contains(span, 'Начинки')]"
bun_button = "//div[contains(span, 'Булки')]"
account_button = "//p[contains(text(),'Личный Кабинет')]"
save_button = "//button[text()='Сохранить']"
login_button = "//button[text()='Войти']"
login_from_home_page_button = "//button[text()='Войти в аккаунт']"
login_from_reg_page_button = '//a[@href="/login"]'
order_button = "//button[text()='Оформить заказ']"
logout_button = "//button[text()='Выход']"

# other
constructor_logo = "//div[contains(@class, 'header__logo')]"
current_atribute = '[contains(@class,"current")]'
