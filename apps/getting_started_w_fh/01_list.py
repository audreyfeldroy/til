from fasthtml.common import *

app, rt = fast_app(live=True)

def NumList(n):
    return Ul(*[Li(i+1) for i in range(n)])

@rt("/")
def get():
    return Titled(
        "My Numbers",
        P("Do you like these numbers?"),
        NumList(7),
        A("Change", href="/change"),
    )

@rt("/change")
def get():
    return Titled(
        "Change",
        P("Change is good!"),
        A("Back", href="/"),
    )

serve()
