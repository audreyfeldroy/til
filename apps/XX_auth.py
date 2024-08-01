from fasthtml.common import *

auth = user_pwd_auth(testuser="spycraft")
app, rt = fast_app(middleware=[auth])

@rt("/")
def get():
    return Div(P("Hello World!"), hx_get="/change")

@rt("/locked")
def get(auth):
    return "Hello, " + auth

serve()
