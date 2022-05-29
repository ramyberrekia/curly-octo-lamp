from django import forms
from .models import Post 
from django.core.exceptions import ValidationError
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from django.utils.text import slugify


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','display_pic','tags',)
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }
    
    def clean(self):
        cleaned_data = super(PostCreateForm, self).clean()
        title = self.cleaned_data['title']
        if self.instance.title != title and Post.objects.filter(title=title).exists():
            self.add_error('title', 'This title has been used before! Try using another one')
        
        return cleaned_data

        
    