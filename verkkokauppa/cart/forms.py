from django import forms

from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'name',
            'last_name',
            'address',
            'post_code',
            'post_address',
            'email',
            'card_number',
            'card_exp_month',
            'card_exp_year',
            'card_ccs',
        ]