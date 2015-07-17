from django.shortcuts import render
from django.http import JsonResponse
from restkit import Resource, BasicAuth
from mining import mining_settings
from .models import EpsCase
import json
import bulkload

BASE_URL = mining_settings.JIRA_REST_BASE_URL
JIRA_USR = mining_settings.JIRA_USER_NAME
JIRA_PWD = mining_settings.JIRA_USER_PWD
customer_list = ["Humana", "Cerner", "Baystate", "Ochsner", "Epic", "Legacy", "Alexian", "Others"]


def load_data(request):
    loaded_case = []
    for num in range(187, 188):
        auth = BasicAuth(JIRA_USR, JIRA_PWD)
        resource = Resource(BASE_URL + "EPS-" + str(num), filters=[auth])
        response = resource.get(headers={'Content-Type': 'application/json'})
        if response.status_int == 200:
            json_obj = json.loads(response.body_string())
            loaded_case.append(bulkload.load_case(json_obj).case_key)
        else:
            c = {
                "error_message": "Unable to fetch data from JIRA"
            }
            return render(request, "mining/load_data.html", c)
    return render(request, "mining/load_data.html", {"cases": loaded_case})


def index(request):
    response_list = []
    for customer_name in customer_list:
        case_list = EpsCase.objects.filter(
            customer__customer_name=customer_name
        )
        inner_object_list = []
        for case in case_list:
            inner_object = {"key": case.case_key, "value": case.case_create_date}
            inner_object_list.append(inner_object)
        if len(inner_object_list) != 0:
            response = {"name": customer_name, "cases": inner_object_list}
            response_list.append(response)
    return render(request, "mining/index.html", {"json": response_list})
    # return JsonResponse(response_list, safe=False)


def detail(request):
    customer = request.POST["customer"]
    case_list = EpsCase.objects.filter(
        customer__customer_name=customer
    )