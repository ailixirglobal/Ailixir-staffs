from django import forms
from .models import AIUserSettings
from research.models import Experiment
from product.models import Product


class AISettingsForm(forms.ModelForm):
    class Meta:
        model = AIUserSettings
        fields = [
            "system_prompt",
            "active_experiment",
            "context_products",
            "ai_model",
            "temperature",
            "max_tokens",
            "use_history",
            "use_role_context",
        ]

        widgets = {
            "system_prompt": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "active_experiment": forms.Select(attrs={"class": "form-control"}),
            "context_products": forms.SelectMultiple(attrs={"class": "form-control"}),
            "ai_model": forms.TextInput(attrs={"class": "form-control"}),
            "temperature": forms.NumberInput(attrs={"class": "form-control", "step": "0.1"}),
            "max_tokens": forms.NumberInput(attrs={"class": "form-control"}),
            "use_history": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "use_role_context": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }