__author__ = 'hwang'
from .models import EpsCase, Comment
from django.utils.dateparse import parse_datetime

customer_map = {"hum": "Humana", "hie": "Humana", "cern": "Cerner", "baystate": "Baystate", "ochsner": "Ochsner"}


def load_case(json):
    eps_case = None
    try:
        eps_case = EpsCase.objects.update_or_create(
            case_assignee=json["fields"]["assignee"]["displayName"],
            case_create_date=parse_datetime(json["fields"]["created"]),
            case_creator=json["fields"]["creator"]["displayName"],
            case_customer=get_customer(json),
            case_description=json["fields"]["description"],
            case_id=json["id"],
            case_key=json["key"],
            case_status=json["fields"]["status"]["name"],
            case_summary=json["fields"]["summary"],
            case_update_date=parse_datetime(json["fields"]["updated"]),
        )
        load_commit(eps_case, json)
    except ValueError as e:
        print "Value Validation Error", e.message
    return eps_case


def load_commit(case, json):
    for comment in json["fields"]["comment"]:
        Comment.objects.update_or_create(
            comment_text=comment["body"],
            epsCase=case,
        )


def get_customer(json):
    for k, v in customer_map:
        for label in json["fields"]["labels"]:
            if k in label:
                return v

        if k in json["fields"]["environment"]:
            return v

        if k in json["fields"]["summary"]:
            return v

        if k in json["fields"]["description"]:
            return v
    return "Unknown"