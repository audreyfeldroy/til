from fasthtml.common import *


def render(todo):
    tid = f"todo-{todo.id}"
    toggle = A("Toggle", hx_get=f"/toggle/{todo.id}", target_id=tid)
    delete = A("Delete", hx_delete=f"/{todo.id}", hx_swap="outerHTML", target_id=tid)
    return Li(toggle, delete, todo.title + (" ✅" if todo.done else ""), id=tid)


app, rt, todos, Todo = fast_app(
    "todos.db", live=True, render=render, id=int, title=str, done=bool, pk="id"
)


@rt("/")
def get():
    frm = Form(Group(Input(placeholder="Add a new todo", name='title'), Button("Add")), 
               hx_post="/", target_id="todo-list", hx_swap="beforeend")
    return Titled(
        "Todos",
        Card(
            Ul(*todos(), id="todo-list"),
            header=frm,
        ),
    )

@rt("/")
def post(todo: Todo): return todos.insert(todo)

@rt("/{tid}")
def delete(tid: int): todos.delete(tid)


@rt("/toggle/{tid}")
def get(tid: int):
    todo = todos[tid]
    todo.done = not todo.done
    todos.update(todo)
    return todo


serve()
