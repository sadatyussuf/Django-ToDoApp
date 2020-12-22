from django.shortcuts import redirect, render

from .forms import todoForm
from .models import todoModel



# Create your views here.
def todoApp(request):
    form = todoForm()
    todoMod = todoModel.objects.all()
    return render(request,'todo.html',{'forms': form,'todoMods': todoMod})

def addTodoItem(request):
    form = todoForm()
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todoapp')
    else:
        form = todoForm()
    return render(request,'todo.html',{'forms': form})

def deleteTodoItem(request,pk):
    todoMod = todoModel.objects.get(pk=pk)
    todoMod.delete()
    return redirect('todoapp')