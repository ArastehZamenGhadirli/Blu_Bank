from django.urls import path
from . import views

urlpatterns = [
    path("charge/<int:account_id>/", "charge_account"),
    path("balance/<int:account_id>/", "account_balance"),
    path("profits/<int:account_id>/", "list_profit"),
]
