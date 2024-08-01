from fasthtml.common import *

app, rt = fast_app(live=True)

def NumList(n):
    return Ul(*[Li(i+1) for i in range(n)])

@rt("/")
def get():
    return Titled(
        "My Numbers",
        P("Do you like these numbers?"),
        Div(NumList(7), hx_get="/change")
    )

@rt("/change")
def get():
    return P("Change is good!")

serve()
