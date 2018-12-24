from django import forms

class Namepnr(forms.Form):
    pnr_no = forms.CharField(label='pnr')