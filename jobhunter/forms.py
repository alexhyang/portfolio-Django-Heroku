from django.db.models import fields
from django.forms import widgets
from .models import Posting

from django import forms

LEVEL_CHOICES = (
    ("Unknown", "Unknown"),
    ("Junior", "Junior (less than 3 years)"),
    ("Intermediate", "Intermediate (3~5 years)"),
    ("Senior", "Senior (more than 5 years)"),
    ("Intern", "Intern"),
    ("Other", "Other"),
)

TYPE_CHOICES = (
    ("Part-time", "Part-time"),
    ("Full-time", "Full-time"),
    ("Temporary", "Temporary"),
    ("Contract", "Contract"),
    ("Remote", "Remote"),
    ("Internship", "Internship"),
    ("Co-op", "Co-op"),
    ("Other", "Other"),
)

PLACE_CHOICES = (
    ("Vancouver, BC", "Vancouver, BC"),
    ("Burnaby, BC", "Burnaby, BC"),
    ("Richmond, BC", "Richmond, BC"),
    ("Surrey, BC", "Surrey, BC"),
    ("Victoria, BC", "Victoria, BC"),
    ("Kamloops, BC", "Kamloops, BC"),
    ("Brentwood Bay, BC", "Brentwood Bay, BC"),
)


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = [
            "url",
            "position",
            "company",
            "location",
            "type",
            "level",
            "due_date",
            "responsibilities",
            "qualifications",
            "skills",
            "other",
        ]
        widgets = {
            "level": forms.Select(choices=LEVEL_CHOICES),
            "type": forms.SelectMultiple(choices=TYPE_CHOICES),
            # "place": forms.Select(choices=PLACE_CHOICES),
            "due_date": forms.TextInput(attrs={"type": "date"}),
            "url": forms.TextInput(attrs={"type": "url", "autofocus": "autofocus"}),
        }
