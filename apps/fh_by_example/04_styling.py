from fasthtml import *

# App with custom styling to override the pico defaults
css = Style(":root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}")
app = FastHTML(hdrs=(picolink, css))


@app.route("/")
def get():
    return Title("Hello World"), Main(H1("Hello, World"), cls="container")
