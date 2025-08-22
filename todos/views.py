from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Todo


def todo_list(request):
    todos = Todo.objects.order_by('-created_at')
    return render(request, 'todos/todo_list.html', {'todos': todos})


@require_http_methods(["POST"])
def add_todo(request):
    title = request.POST.get('title', '').strip()
    if title:
        Todo.objects.create(title=title)
    return redirect('todos:list')


def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save(update_fields=["is_completed"])
    return redirect('todos:list')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todos:list')
