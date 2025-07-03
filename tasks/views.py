from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    """
    Display the main taskmaster page
    """
    # Get all uncompleted tasks ordered by due date (soonest first)
    uncompleted_tasks = Task.objects.filter(completed=False).order_by('due_date', 'created_at')

    # Get all completed tasks ordered by completion date (most recent first)
    completed_tasks = Task.objects.filter(completed=True).order_by('-updated_at')

    # Create an empty form for adding new tasks
    form = TaskForm()

    return render(request, 'tasks/index.html', {
        'uncompleted_tasks': uncompleted_tasks,
        'completed_tasks': completed_tasks,
        'form': form
    })


def add_task(request):
    """
    Process form submission and add a new task
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.completed = False
            task.save()
            messages.success(
                request,
                f'Task "{task.title}" added successfully!'
            )
            return redirect('tasks:index')
        else:
            messages.error(request, 'Please correct the errors below.')
            # Re-render the index page with the form containing errors
            uncompleted_tasks = Task.objects.filter(completed=False).order_by('due_date', 'created_at')
            completed_tasks = Task.objects.filter(completed=True).order_by('-updated_at')
            return render(request, 'tasks/index.html', {
                'uncompleted_tasks': uncompleted_tasks,
                'completed_tasks': completed_tasks,
                'form': form
            })

    return redirect('tasks:index')


def toggle_task(request, task_id):
    """
    Toggle the completion status of a task
    """
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()

        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'completed': task.completed,
                'message': f'Task "{task.title}" marked as {"completed" if task.completed else "incomplete"}'
            })

        # For non-AJAX requests, redirect with message
        messages.success(
            request,
            f'Task "{task.title}" marked as {"completed" if task.completed else "incomplete"}'
        )
        return redirect('tasks:index')

    return redirect('tasks:index')
