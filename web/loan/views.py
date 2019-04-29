import pickle

from django.http import JsonResponse
from django.shortcuts import render


def loan_client(request):
    return render(request, 'loan_client.html')


def loan_status_check(request):
    # read parameters
    amount = float(request.GET["amount"])
    income = float(request.GET["income"])
    cincome = float(request.GET["cincome"])
    term = float(request.GET["term"])
    cr = float(request.GET["cr"])

    # load model and make prediction
    f = open(r"e:\classroom\ds\mar21\loan\lr_model.pkl", "rb")
    model = pickle.load(f)
    f.close()
    X_test = [[amount,income, cincome,term,cr]]
    print(X_test)
    status = model.predict(X_test)[0]

    return JsonResponse({"status": status})
