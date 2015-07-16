__author__ = 'hwang'
from django.conf import settings


def get(key, default):
    return getattr(settings, key, default)

JIRA_REST_BASE_URL = get('JIRA_REST_BASE_URL', None)
JIRA_BROWSE_BASE_URL = get('JIRA_BROWSE_BASE_URL', None)
JIRA_USER_NAME = get('JIRA_USER_NAME', None)
JIRA_USER_PWD = get('JIRA_USER_PWD', None)