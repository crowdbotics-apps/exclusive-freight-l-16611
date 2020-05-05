from django.conf import settings
from django.db import models


class CustomerWallet(models.Model):
    "Generated Model"
    customer = models.OneToOneField(
        "task_profile.CustomerProfile",
        on_delete=models.CASCADE,
        related_name="customerwallet_customer",
    )
    balance = models.FloatField()
    expiration_date = models.DateTimeField()
    last_transaction = models.DateTimeField()


class PaymentMethod(models.Model):
    "Generated Model"
    wallet = models.ForeignKey(
        "wallet.CustomerWallet",
        on_delete=models.CASCADE,
        related_name="paymentmethod_wallet",
    )
    account_token = models.CharField(max_length=255,)
    payment_account = models.CharField(max_length=10,)
    timestamp_created = models.DateTimeField(auto_now_add=True,)


class TaskerPaymentAccount(models.Model):
    "Generated Model"
    wallet = models.ForeignKey(
        "wallet.TaskerWallet",
        on_delete=models.CASCADE,
        related_name="taskerpaymentaccount_wallet",
    )
    account_token = models.CharField(max_length=255,)
    payment_account = models.CharField(max_length=10,)
    timestamp_created = models.DateTimeField(auto_now_add=True,)


class TaskerWallet(models.Model):
    "Generated Model"
    tasker = models.OneToOneField(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="taskerwallet_tasker",
    )
    balance = models.FloatField(max_length=254,)
    expiration_date = models.DateTimeField()
    last_transaction = models.DateTimeField()


class PaymentTransaction(models.Model):
    "Generated Model"
    price = models.FloatField()
    tip = models.FloatField()
    tracking_id = models.CharField(max_length=50,)
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="paymenttransaction_tasker",
    )
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="paymenttransaction_customer",
    )
    transaction = models.ForeignKey(
        "task.TaskTransaction",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="paymenttransaction_transaction",
    )
    payment_method = models.ForeignKey(
        "wallet.PaymentMethod",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="paymenttransaction_payment_method",
    )


# Create your models here.
