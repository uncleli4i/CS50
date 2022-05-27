from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Comps


class NewCompForm(ModelForm):
        class Meta:
            model = Comps
            fields = ['name', 'user', 'CPU', 'OS','RAM', 'HDD', 'monitor']



