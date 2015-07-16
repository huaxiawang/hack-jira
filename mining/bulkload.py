__author__ = 'hwang'
from .models import EpsCase, Comment, Customer
from django.utils.dateparse import parse_datetime

customer_map = {"hum": "Humana", "hie": "Humana", "cern": "Cerner", "epic": "Epic", "legacy": "Legacy",
                "baystate": "Baystate", "ochsner": "Ochsner", "alexian": "Alexian", "unknown": "Others"}


def load_case(json):
    eps_case = None
    try:
        eps_case, created = EpsCase.objects.update_or_create(
            case_assignee=json["fields"]["assignee"]["displayName"],
            case_create_date=parse_datetime(json["fields"]["created"]),
            case_creator=json["fields"]["creator"]["displayName"],
            case_description=json["fields"]["description"],
            case_id=json["id"],
            case_key=json["key"],
            case_status=json["fields"]["status"]["name"],
            case_summary=json["fields"]["summary"],
            case_update_date=parse_datetime(json["fields"]["updated"]),
        )
        get_customer(eps_case, json)
        get_commit(eps_case, json)
    except ValueError as e:
        print "Value Validation Error", e.args
    return eps_case


def get_commit(case, json):
    comments = json["fields"]["comment"]["comments"]
    if len(comments) > 0:
        for comment in comments:
            Comment.objects.update_or_create(
                comment_text=comment["body"],
                epsCase=case,
            )


def get_customer(case, json):
    customer_exist = False
    for k, v in customer_map.iteritems():
        labels = json["fields"]["labels"]
        if len(labels) > 0:
            for label in labels:
                print label
                if k in label.lower():
                    customer_exist = True
                    Customer.objects.update_or_create(
                        customer_name=v,
                        epsCase=case,
                    )

        environment = json["fields"]["environment"]
        if environment is not None:
            if k in environment.lower():
                customer_exist = True
                Customer.objects.update_or_create(
                    customer_name=v,
                    epsCase=case,
                )

        summary = json["fields"]["summary"]
        if k in summary.lower():
            customer_exist = True
            Customer.objects.update_or_create(
                customer_name=v,
                epsCase=case,
            )

        description = json["fields"]["description"]
        if description is not None:
            if k in json["fields"]["description"].lower():
                customer_exist = True
                Customer.objects.update_or_create(
                    customer_name=v,
                    epsCase=case,
                )

    if not customer_exist:
        Customer.objects.update_or_create(
            customer_name=customer_map["unknown"],
            epsCase=case,
        )