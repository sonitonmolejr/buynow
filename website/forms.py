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
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
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

    def clean(self):
        today = datetime.today()
        exp_month = int(self.cleaned_data['expiration_month'])
        exp_year = int(int(self.cleaned_data['expiration_year']))

        if exp_year < today.year or (exp_month <= today.month and exp_year <= today.year):
            raise forms.ValidationError('Please make sure your Credit Card expires in the future.')

        return self.cleaned_data

