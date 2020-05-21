from django import forms

from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'author',
            'judul',
            'body',
            'category',
        ]

        labels ={
            'judul':'title',
            'author' : 'Penulis',
        }
        widgets = {
            'judul' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Isi dengan judul artikel'
                }
            ),

            'author' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Nama Penulis',
                }
            ),

            'body' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Isi Blog',
                }
            ),

            'category' : forms.Select(
                attrs={
                    'class' : 'form-control',
                }
            ),
        }