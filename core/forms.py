from django import forms


class CepForm(forms.Form):

    cep = forms.CharField(max_length=10)
    logradouro = forms.CharField(max_length=50)
    bairro = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=30)
    uf = forms.CharField(max_length=2)

    def __init__(self, *args, **kwargs):
        super(CepForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['readonly'] = 'readonly'
