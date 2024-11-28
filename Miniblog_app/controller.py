import web
from models import RegisterModel, LoginModel

urls = (
    '/', 'home',
    '/register', 'register',
    '/login', 'Login',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin'
)

render = web.template.render("views/templates/", base="MainLayout")
app = web.application(urls, globals())

class home:
    def GET(self):
        return render.Home()


class register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()
        #print(type(data))
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            return isCorrect
        return "error"


if __name__ == "__main__":
    app.run()