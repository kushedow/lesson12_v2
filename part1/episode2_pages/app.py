from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Главная страничка"


app.run()


# Чтобы создать страничку просто добавьте маршрут в декоратор и готово.
# Давайте сделаем четыре странички - одна у нас уже есть
# Начнем с главной странички

# @app.route("/profile/")
# def page_profile():
#     return "Профиль пользователя"

# ОТКРЫВАЕМ БРАУЗЕР И ЗАПУСКАЕМ

# @app.route("/feed/")
# def page_feed():
#     return "Лента пользователя"

# ОТКРЫВАЕМ БРАУЗЕР И ЗАПУСКАЕМ

# @app.route("/messages/")
# def page_messages():
#     return "Страничка сообщений"

# ОТКРЫВАЕМ БРАУЗЕР И ЗАПУСКАЕМ

# Со страничками разобрались – двигаемся дальше