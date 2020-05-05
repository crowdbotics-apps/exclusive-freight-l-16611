from django.contrib import admin
from .models import (
    PaymentTransaction,
    TaskerPaymentAccount,
    TaskerWallet,
    PaymentMethod,
    CustomerWallet,
)

admin.site.register(CustomerWallet)
admin.site.register(PaymentMethod)
admin.site.register(TaskerPaymentAccount)
admin.site.register(TaskerWallet)
admin.site.register(PaymentTransaction)

# Register your models here.
