from cProfile import label
from .models import Message
from django import forms

class SendMessForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = { 'text':
                        forms.Textarea(attrs={'class': 'form-input',
                            'placeholder': 'Введите сообщение'})}
    def save(self, commit=True):
        print(self.cleaned_data['text'] + "  govno")