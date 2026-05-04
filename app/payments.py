import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_payment(amount=1000):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
    )
    return intent.client_secret
