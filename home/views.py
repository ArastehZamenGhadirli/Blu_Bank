import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from home.models import Account, Profit


@csrf_exempt
def charge(request, account_id: int):
    if request.method == "POST":
        data = json.loads(request.body)
        account = get_object_or_404(Account, id=account_id)
        account.amount += data.get("amount")
        account.save()

        return HttpResponse(f"your account charged with {data.get('amount')} ")


def show_balance(request, account_id: int):
    account = get_object_or_404(Account, id=account_id)
    return HttpResponse(f"you have {account.amount} in your account")


def list_profit(request, account_id):
    if request.method == "GET":
        profits = Profit.objects.filter(account_id=account_id)
        return HttpResponse(
            "\n".join(
                f"{p.date}: {p.title} - {p.amount} ({p.duration} days)" for p in profits
            )
        )
    elif request.method == "POST":
        Profit.objects.create(
            account_id=account_id,
            title=request.POST.get("title"),
            amount=request.POST.get("amount"),
            duration=request.POST.get("duartion"),
        )
        return HttpResponse("proft reccord created", status=201)

    return HttpResponseNotAllowed(["GET", "POST"])
