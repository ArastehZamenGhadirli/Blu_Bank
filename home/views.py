import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Account

@csrf_exempt
def charge(request , account_id :int):
    if request.method == 'POST' :
        data = json.loads(request.body)
        account = get_object_or_404(Account, id = account_id)
        account.card_number+= data.get("a")
