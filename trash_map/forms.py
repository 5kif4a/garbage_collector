from django.forms import ModelForm,  Textarea, NumberInput
from trash_map.models import Dump, Event


class DumpForm(ModelForm):
    class Meta:
        model = Dump
        fields = "__all__"
        widgets = {
            'long': NumberInput(attrs={'readonly': 'readonly', 'id': 'd_long'}),
            'lat': NumberInput(attrs={'readonly': 'readonly', 'id': 'd_lat'}),
            'description': Textarea(attrs={'rows': 5, 'style': 'resize:none;'})
        }

    def __init__(self, *args, **kwargs):
        super(DumpForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'ФИО (полностью)'
        self.fields['phone'].label = 'Контактный номер телефона'
        self.fields['email'].label = "Адрес электронной почты"
        self.fields['long'].label = 'Широта'
        self.fields['lat'].label = 'Долгота'
        self.fields['street'].label = 'Улица'
        self.fields['description'].label = 'Описание'
        self.fields['photo'].label = 'Фотографий'
        self.fields['status'].required = False
        self.fields['rating'].required = False


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'long': NumberInput(attrs={'readonly': 'readonly', 'id': 'e_long'}),
            'lat': NumberInput(attrs={'readonly': 'readonly', 'id': 'e_lat'}),
            'description': Textarea(attrs={'rows': 5, 'style': 'resize:none;'})
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'ФИО (полностью)'
        self.fields['long'].label = 'Широта'
        self.fields['lat'].label = 'Долгота'
        self.fields['street'].label = 'Улица'
        self.fields['description'].label = 'Описание'
        self.fields['org_email'].label = "Адрес электронной почты организатора"
        self.fields['org_phone'].label = "Контактный номер организатора"
        self.fields['rating'].required = False
