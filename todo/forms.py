from .models import Todo
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "date_complated", "important"]
        # fields = "__all__"
