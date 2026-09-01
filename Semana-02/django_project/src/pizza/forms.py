from django import forms

MASA_CHOICES = [
    ('Masa delgada', 'Masa delgada'),
    ('Masa tradicional', 'Masa tradicional'),
    ('Masa integral', 'Masa integral'),
    ('Masa artesanal', 'Masa artesanal'),
]

STOCK_CHOICES = [
    ('Disponible', 'Disponible'),
    ('Poco stock', 'Poco stock'),
    ('Agotado', 'Agotado'),
]


class PizzaForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre de la Pizza')
    dough_type = forms.ChoiceField(
        choices=MASA_CHOICES, label='Tipo de Masa', widget=forms.Select
    )
    ingredients = forms.CharField(widget=forms.Textarea, label='Ingredientes')
    stock_status = forms.ChoiceField(
        choices=STOCK_CHOICES, label='Estado del Stock', widget=forms.Select
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['dough_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['stock_status'].widget.attrs.update({'class': 'form-select'})
        self.fields['ingredients'].widget.attrs.update({
            'rows': 3,
            'class': 'form-control'
        })