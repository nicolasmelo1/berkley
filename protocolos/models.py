from django.db import models
from pipeline.models import \
    Regionals, Subsidiaries, Commercials, Products, InsuranceType, Expectations, Status, ReasonsForLoss, Congeners


class Protocols(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    regional = models.ForeignKey(Regionals, on_delete=models.CASCADE)
    subsidiary = models.ForeignKey(Subsidiaries, on_delete=models.CASCADE)
    commercial = models.ForeignKey(Commercials, on_delete=models.CASCADE)
    broker = models.CharField(max_length=250)
    first_quotation = models.BooleanField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    client = models.CharField(max_length=250)
    prize = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    receipt = models.DateField()
    maturity = models.DateField()
    closure = models.DateField()
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE)
    expectation = models.ForeignKey(Expectations, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    subscriber = models.CharField(max_length=250)
    reason_for_loss = models.ForeignKey(ReasonsForLoss, on_delete=models.CASCADE, null=True, blank=True)
    congener = models.ForeignKey(Congeners, on_delete=models.CASCADE, null=True, blank=True)
    loss_comment = models.CharField(max_length=250, null=True, blank=True)
    loss_detail = models.CharField(max_length=400, null=True, blank=True)

    class Meta:
        db_table = 'protocols'


class History(models.Model):

    protocol = models.ForeignKey(Protocols, on_delete=models.CASCADE)
    history = models.CharField(max_length=4000, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'history'
