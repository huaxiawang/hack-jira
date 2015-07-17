from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from restkit import Resource, BasicAuth
from mining import mining_settings, nlp
from .models import EpsCase
import json
import bulkload

BASE_URL = mining_settings.JIRA_REST_BASE_URL
JIRA_USR = mining_settings.JIRA_USER_NAME
JIRA_PWD = mining_settings.JIRA_USER_PWD
customer_list = ["Humana", "Cerner", "Baystate", "Ochsner", "Epic", "Legacy", "Alexian", "Others"]


def load_data(request):
    loaded_case = []
    for num in range(115, 649):
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
    response = {}
    for customer_name in customer_list:
        case_list = EpsCase.objects.filter(
            customer__customer_name=customer_name
        )
        inner_object_list = []
        for case in case_list:
            inner_object = {"key": case.case_key.encode("utf-8"), "value": case.case_create_date.isoformat()}
            inner_object_list.append(inner_object)
        if len(inner_object_list) != 0:
            response[customer_name] = inner_object_list
    return render(request, "mining/index.html", {"json": response})
    # return JsonResponse(response_list, safe=False)


def case_list(request):
    customer = request.POST.get('customer', False)
    print customer
    cases = EpsCase.objects.filter(
        customer__customer_name=customer
    )
    return HttpResponseRedirect(reverse('detail', args=(cases, )))


def detail(request, cases):
    return render(request, 'mining/details.html', {"cases": cases})


def correlation(request):
    response = []
    case_key = request.POST["case_key"]
    related_cases = nlp.get_relation(case_key)
    for case_key, case_similarity in related_cases.iteritems():
        case = EpsCase.objects.get(case_key=case_key)
        response.append({"pid": case.case_key, "ratio": case_similarity, "des": case.case_summary})
    return JsonResponse(response, safe=False)