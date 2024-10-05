from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.


# 新增待事項
def create_todo(request):
    message = ""
    user = request.user
    if not user.is_authenticated:
        message = "請先登入"
    else:
        form = TodoForm()
        if request.method == "POST":
            try:
                print(request.POST)
                form = TodoForm(request.POST)
                todo = form.save(commit=False)
                todo.user = request.user
                todo.save()
                message = "提交成功"
                return redirect("todolist")
            except Exception as e:
                print(e)
                message = "提交失敗，請確認"

        return render(
            request, "todo/create-todo.html", {"form": form, "message": message}
        )


# 檢視待辦事項
def todo(request, id):
    message = ""
    todo = None
    user = request.user  # user id要對才會顯示
    try:
        todo = Todo.objects.get(id=id, user=user)
        form = TodoForm(instance=todo)
    except Exception as e:
        print(e)
        message = "編號錯誤"
    return render(
        request, "todo/todo.html", {"form": form, "todo": todo, "message": message}
    )


def todolist(request):
    user = request.user
    todos = None
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)

    print(todos)
    return render(request, "todo/todolist.html", {"todos": todos})
