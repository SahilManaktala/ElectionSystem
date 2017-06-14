from django.db import models

class State(models.Model):
    country_id = models.CharField(max_length = 1)
    state_id = models.CharField(max_length = 1)
    state_name = models.CharField(max_length = 100)

class District(models.Model):
    state_id = models.CharField(max_length = 1)
    district_id = models.CharField(max_length = 2)
    district_name = models.CharField(max_length = 150)

class Tehsil(models.Model):
    district_id = models.CharField(max_length = 2)
    tehsil_id = models.CharField(max_length = 2)
    tehsil_name = models.CharField(max_length = 150)

class GramPanchayat(models.Model):
    tehsil_id = models.CharField(max_length = 2)
    gram_panchayat_id = models.CharField(max_length = 2)
    gram_panchayat_name = models.CharField(max_length = 150)
