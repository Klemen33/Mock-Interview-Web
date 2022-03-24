from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import transaction


from .models import User, Student, Interviewer


class InterviewerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_interviewer = True
        user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

# Newly created, To be completed
class EditInterviewerProfileForm(forms.Form):
    username = forms.CharField()
    full_name = forms.CharField()
    profession = forms.CharField()
    current_company = forms.CharField()
    previous_companies = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def clean_username(self):
        """
        This function throws an exception if the username has already been 
        taken by another user
        """

        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('A user with that username already exists.')
        return username

# Newly created, To be completed
class EditStudentProfileForm(forms.Form):
    username = forms.CharField()
    student_name = forms.CharField()
    college_name = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def clean_username(self):
        """
        This function throws an exception if the username has already been 
        taken by another user
        """

        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('A user with that username already exists.')
        return username

# # User Reset Password Form
# class UserPasswordResetForm(SetPasswordForm):
#     """Reset Password Form. After Email was sent"""
#     new_password1 = forms.CharField(label='Password',
#         help_text="<ul class='errorlist text-muted'><li>Your password can't be too similar tou your other personal information.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>",
#         max_length=100,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password',
#                 'type': 'password',
#                 'id': 'user_password',
#             }
#         ))

#     new_password2 = forms.CharField(label='Password',
#         help_text=False,
#         max_length=100,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Confirm Password',
#                 'type': 'password',
#                 'id': 'user_password',
#             }
#         ))

# # Email Request Forgot Password Form
# class UserForgotPasswordForm(PasswordResetForm):
#     """User forgot password, check via email form."""
#     email = forms.EmailField(label='Email Address',
#     max_length=254,
#     required=True,
#     widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Email Address',

#             'type': 'text',
#             'id': 'email_address',
#         }
#     ))