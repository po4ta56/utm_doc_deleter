from django import forms

class SettingsForm(forms.Form):
    pass
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id','ID'),('created_at','Дата создания'))