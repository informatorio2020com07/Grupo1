from django import forms
from .models import Anuncio_Trans, Contratista, Localidad, Transporte, Comentario

class LocalidadForm(forms.ModelForm):
    class Meta:
        model=Localidad
        fields="__all__"

class TransporteForm(forms.ModelForm):
    class Meta:
        model=Transporte
        fields="__all__"


class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio_Trans
        fields = "__all__"
        exclude = ('usuario',)
    
    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields["permitir_comentarios"].widget.attrs.update({"type":"checkbox", "checked":"checked"})

        """
        self.fields['nombre'].widget.attrs.update({'id' :  'name_input','placeholder' : 'ingrese nombre', 'type' : 'text'})
        self.fields['Email'].widget.attrs.update({'id' : 'email_input','placeholder' : 'ingrese email', 'type' : 'email'})
        self.fields['localidad_origen'].widget.attrs.update({'id' : 'subject_input' , 'placeholder' :'ingrese localidad origen','type' : 'subject_line'})
        self.fields['localidad_destino'].widget.attrs.update({'id' : 'subject_input' , 'placeholder' :'ingrese localidad destino', 'type' : ''})
        self.fields['recorrido'].widget.attrs.update({'class' : '','placeholder' : 'ingrese recorrido', 'type' : 'text'})
        self.fields['titulo'].widget.attrs.update({'class' :  'validate', 'placeholder': 'titulo', 'type' : 'text'})
        self.fields["descripcion"].widget.attrs.update({'message_input' : 'materialize-textarea','placeholder' : 'descripcion', 'type' : 'text'})
        self.fields['transporte'].widget.attrs.update({'class' : '' , 'placeholder' :'ingrese localidad destino', 'type' : ''})
        self.fields['fecha_caducidad'].widget.attrs.update({ 'class' : 'input-field col s12','placeholder' : 'ingrese fecha', 'type' : 'date'})
        self.fields['tel'].widget.attrs.update({'class' : 'telephone','placeholder' : 'tel', 'type' : 'number'})
"""
class ContratistaForm(forms.ModelForm):
    class Meta:
        model = Contratista
        fields = "__all__"
        exclude = ('usuario',)

    """def __init__(self, *args, **kwargs):
        super(ContratistaForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class' :  'validate', 'placeholder': 'titulo', 'type' : 'text'})
        self.fields['fecha_viaje'].widget.attrs.update({ 'class' : 'input-field col s12','placeholder' : 'ingrese fecha', 'type' : 'date'})"""


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)


