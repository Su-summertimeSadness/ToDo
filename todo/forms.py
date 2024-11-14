from django import forms
from .models import Tag, Action
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Choose another slug. ("Not Create")')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Choose another slug. (Not - {new_slug}))')


        return new_slug


class ActionForm(forms.ModelForm):
    is_done = forms.BooleanField(required=False)

    class Meta:
        model = Action
        fields = ['title', 'slug', 'body', 'dead_line', 'tag', 'is_done']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'dead_line': forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'tag': forms.Select(choices=Tag.objects.all(), attrs={'class': 'form-control'}),


        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
            if new_slug == 'create':
                raise ValidationError('Choose another slug. ("Not Create")')

            return new_slug





