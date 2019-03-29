from django import forms

class SettingsForm(forms.Form):
    #search = forms.CharField(required=False)
    #sort_field = forms.ChoiceField(choices=(('id','ID'),('created_at','Дата создания')))
    address = forms.CharField(required=True)