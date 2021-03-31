from django import forms
from django.contrib.auth.tokens import default_token_generator

from accounts.models import User
from accounts.tasks import send_activate_account_email


class SighUpForm(forms.ModelForm):
    password1 = forms.CharField(min_length=6)
    password2 = forms.CharField(min_length=6)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email__iexact=email).exists():
    #         login_url = reverse('login')
    #         raise forms.ValidationError(
    #             f'Seems that you already have account! Please visit {login_url}'
    #         )
    #     return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password2', 'Passwords should match!')
            # raise forms.ValidationError('Passwords should match!')

        return cleaned_data

    def save(self, commit=True):
        instance: User = super().save(commit=False)
        instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            instance.save()

        token = default_token_generator.make_token(instance)
        send_activate_account_email.delay(instance.username, token)

        return instance
