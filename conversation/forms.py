from django import forms

from .models import ConversationMessage

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        
        widgets = {
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
        }
