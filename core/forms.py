from django import forms
from django.db.models import fields
# from django.db import models
# from django.db.models import fields
from django.forms import ModelForm
# from bootstrap_modal_forms.forms import BSModalModelForm
# from django.forms import widgets

# from .widgets import BootstrapDateTimePickerInput
from .models import Meeting, Meeting_Request

class MeetingForm(ModelForm):
    meet_date_time = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        # widgets=BootstrapDateTimePickerInput()
    )
    class Meta:
        model = Meeting_Request
        fields = ('meet_date_time',)

# Meeting Timing Edit
class MeetingEditForm(ModelForm):
    class Meta:
        model = Meeting_Request
        fields = ('meet_date_time',)

class MeetingLinkForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ('meeting_link',)