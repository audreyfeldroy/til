from fasthtml.common import *

app,rt,todos,Todo = fast_app('todos.db', live=True, 
                             id=int, title=str, done=bool, pk='id')


@rt("/")
def get():
    todos.insert(Todo("Pick up Uma", done=False))
    items = todos()
    return Titled("Todos", Div(*items))



serve()
