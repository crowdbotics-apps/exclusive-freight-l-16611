from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PaymentTransactionViewSet,
    TaskerPaymentAccountViewSet,
    TaskerWalletViewSet,
    PaymentMethodViewSet,
    CustomerWalletViewSet,
)

router = DefaultRouter()
router.register("customerwallet", CustomerWalletViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("taskerwallet", TaskerWalletViewSet)
router.register("paymenttransaction", PaymentTransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
