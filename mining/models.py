from django.db import models


# Create your models here.
class EpsCase(models.Model):
    case_assignee = models.CharField(max_length=50, null=True, default=None)
    case_create_date = models.DateTimeField('Date Created', null=False)
    case_creator = models.CharField(max_length=50, null=True, default=None)
    case_description = models.TextField(null=True)
    case_id = models.BigIntegerField(null=False)
    case_key = models.CharField(max_length=20, null=False)
    case_status = models.CharField(max_length=50, null=True, default=None)
    case_summary = models.CharField(max_length=200, null=False)
    case_update_date = models.DateTimeField('Date Updated', null=False)

    def __str__(self):
        return self.case_key + " Summary: " + self.case_summary

    def __unicode__(self):
        return self.case_key + " Summary: " + self.case_summary


class Comment(models.Model):
    epsCase = models.ForeignKey(EpsCase)
    comment_text = models.TextField(null=True)

    def __str__(self):
        return self.epsCase.case_summary + " " + self.comment_text[:50] + ".."

    def __unicode__(self):
        return self.epsCase.case_summary + " " + self.comment_text[:50] + ".."


class Customer(models.Model):
    epsCase = models.ForeignKey(EpsCase)
    customer_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.customer_name

    def __unicode__(self):
        return self.customer_name