from .models import Info
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ["title", "anons", "full_text", "date"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name"
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Anons"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Date"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text"
            })
        }
