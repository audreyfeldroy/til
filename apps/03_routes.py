from fasthtml.common import *

app = FastHTML()

@app.route("/", methods="get")
def home():
    return H1("Hello, World")


@app.route("/")
def post_or_put():
    return "got a POST or PUT request"
