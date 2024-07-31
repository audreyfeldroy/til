from fasthtml.common import *

app = FastHTML()

@app.get("/")
def home():
    return Div(H1("Hello, World"), P("Some text"), P("Some more text"))

