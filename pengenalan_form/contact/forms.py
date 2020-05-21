# membuat form
from django import forms

class ContactForm(forms.Form):
    nama_lengkap   = forms.CharField(
        label = 'Nama Lengkap',
        max_length = 20,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'masukkan nama Lengkap Anda',
            }
        )
    )
    jenis_kelamin   = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs= {'class':'form-check-input'}
        ),
        choices= [
            ('p', 'Pria'),
            ('W', 'Wanita'),
        ],
        
    )
    tanggal_lahir   = forms.DateField(
        widget= forms.SelectDateWidget(
            attrs = {'class' : 'form-control col-sm-2'},
            years=range(1945, 2021, 1),
        ),
    )
    email           = forms.EmailField(
        widget= forms.TextInput(
            attrs= {
                'class' : 'form-control',
                'placeholder' : 'Isi dengan email Anda',
            }
        )
    )
    alamat          = forms.CharField(
        widget= forms.Textarea(
            { 
                'class' : 'form-control',
                'placeholder' : 'isi dengan alamat lengkap',
            }
        ),
        max_length=100,
        required=False,
        
        )
    agree           = forms.BooleanField(
        widget= forms.CheckboxInput(
            attrs= { 'class' : 'form-check-input' }
        )
    )