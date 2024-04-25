import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class AppConfig(BaseAppConfig):

    name = "pinax.stripe"
    label = "pinax_stripe"
    verbose_name = _("Pinax Stripe")

    def ready(self):
        if getattr(settings, "PINAX_STRIPE_ENABLED", True):
            importlib.import_module("pinax.stripe.webhooks")
