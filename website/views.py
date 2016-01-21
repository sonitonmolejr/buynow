from decimal import Decimal
from django.shortcuts import render

from .braintree.gateways.braintree_payments_gateway import BraintreePaymentsGateway
from .braintree.utils.credit_card import CreditCard

def index(request):
    return render(request, 'website/index.html')

def purchase(request):
    credit_card = CreditCard(
        first_name="Test",
        last_name="User",
        month=10,
        year=2011,
        number="4111111111111111",
        verification_value="100"
    )
    braintree = BraintreePaymentsGateway()
    resp = braintree.purchase(Decimal('29.99'), credit_card)

    if resp['response'].is_success:
        return render(request, 'website/thanks.html', {'email': 'sonitomolejr@gmail.com'})
