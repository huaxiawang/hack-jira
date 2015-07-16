from django.shortcuts import render
from restkit import Resource, BasicAuth
from mining import mining_settings
import json
import bulkload

BASE_URL = mining_settings.JIRA_REST_BASE_URL


# Create your views here.
def load_data(request):
    for num in range(14, 100):
        auth = BasicAuth("", "")
        resource = Resource(BASE_URL + "EPS-" + str(num), filters=[auth])
        response = resource.get(headers={'Content-Type': 'application/json'})
        if response.status_int == 200:
            json_obj = json.loads(response.body_string())
            bulkload.load_case(json_obj)
        else:
            return render(request, "")