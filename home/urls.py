from django.urls import path
from .views import charge, show_balance , list_profit

urlpatterns = [
    path("charge/<int:account_id>/", charge),
    path("balance/<int:account_id>/", show_balance),
    path("profits/<int:account_id>/", list_profit),
]
