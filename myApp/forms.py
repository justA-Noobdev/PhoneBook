from django import forms
from .models import Contract, Contact


choices = Contract.objects.all().values_list('contract', 'contract')
choice_list = []
for item in choices:
    choice_list.append(item)


class ContactForm(forms.ModelForm):                    # Creating form for adding a new contact
    class Meta:
        model = Contact
        fields = ('name', 'address', 'contract', 'email', 'phone_number', 'website')

        widgets = {
            'name': forms.TextInput(),
            'address': forms.TextInput(),
            'contract': forms.Select(choices=choice_list, attrs={'class': 'browser-default'}),
            'email': forms.EmailInput(),
            'website': forms.URLInput(),
            'phone_number': forms.NumberInput()
        }