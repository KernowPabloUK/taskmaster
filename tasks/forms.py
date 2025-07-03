from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from .models import Task, Category


class TaskForm(forms.ModelForm):
    """
    ModelForm for creating and editing tasks with Crispy Forms styling
    """

    class Meta:
        model = Task
        fields = ['title', 'due_date', 'category']

        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

        labels = {
            'title': 'Task Title',
            'due_date': 'Due Date',
            'category': 'Category'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make due_date optional
        self.fields['due_date'].required = False

        # Order categories alphabetically
        self.fields['category'].queryset = Category.objects.all().order_by('name')

        # Configure Crispy Forms helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title', placeholder='Enter task title...'),
            Field('due_date'),
            Field('category'),
            Div(
                Submit('submit', 'Add Task', css_class='btn btn-primary'),
                css_class='d-grid gap-2'
            )
        )
