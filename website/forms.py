import logging
from datetime import datetime

from django import forms


class UserCCDetailsForm(forms.Form):
    __MONTH_CHOICES = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )

    __YEAR_CHOICES = (
        (2010, '2010'),
        (2011, '2011'),
        (2012, '2012'),
        (2013, '2013'),
        (2014, '2014'),
        (2015, '2015'),
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
        (2020, '2020'),
    )

    email = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Your email address'})
    )

    cc_number = forms.CharField(
        max_length=16,
        label='Card Number',
        widget=forms.TextInput(attrs={'placeholder': '4242 4242 4242 4242'})
    )
    expiration_month = forms.ChoiceField(choices=__MONTH_CHOICES)
    expiration_year = forms.ChoiceField(choices=__YEAR_CHOICES)

    zip_code = forms.CharField(max_length=8, label='Zip Code')
    cvv = forms.CharField(
        max_length=4,
        label='CV Code',
        widget=forms.TextInput(attrs={'placeholder': '123'})
    )
