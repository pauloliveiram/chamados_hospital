from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioForm(forms.ModelForm):
     class Meta:
        model = Usuario
        fields = ['username', 'email', 'nome',]
 
class CadastroUsuarioForm(forms.ModelForm):
    #usuario = UsuarioForm()
    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Senha','required': 'required'}))
    senha2 = forms.CharField(
        label='Confirmação de senha', widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Confirmação de Senha','required': 'required'})
    )

    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError('A confirmação não está correta')
        return senha2

    def clean_username(self):
        username = self.cleaned_data['username']
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Já existe um usuário com esse nome de usuário')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com esse e-mail')
        return email

    def create(self, commit=True):
        user = super(CadastroUsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['senha1'])
        if commit:
            user.save()
            #usuario = Usuario.objects.create(user=user)
        return user


    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'username', 'email', 'cpf', 'telefone', 'data_nascimento', 'tipo_profissional']

class AtualizarUsuarioForm(forms.ModelForm):

     

    def save(self, commit=True):
        user = super(AtualizarUsuarioForm, self).save(commit=False)
        if commit:
            user.save()
        return user


    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'cpf', 'telefone', 'data_nascimento', 'tipo_profissional']
      