from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from hangapp.models import Category, Note, Priority, Task, SubTask, HomePageView
from hangapp.forms import CategoryForm, NoteForm, PriorityForm, SubTaskForm, TaskForm


class HomePageView(ListView):
    model = HomePageView
    context_object_name = 'home'
    template_name = "index.html"
#ListView
class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 5

class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5

class PriorityList(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5

class SubtaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5


#CreateView

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class SubtaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


#UpdateView
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class SubtaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

#DeleteView
class CategoryDeleteView(DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class NoteDeleteView(DeleteView):
    model = Note
    form_class = NoteForm
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

class SubtaskDeleteView(DeleteView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

class TaskDeleteView(DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')