from django.db import models

class State(models.Model):
    country_id = models.CharField(max_length = 1)
    state_id = models.CharField(max_length = 1)
    state_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.country_id + ' ' + self.state_id + ' ' + self.state_name

class District(models.Model):
    state_id = models.CharField(max_length = 1)
    district_id = models.CharField(max_length = 2)
    district_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.state_id + ' ' + self.district_id + ' ' + self.district_name

class Tehsil(models.Model):
    district_id = models.CharField(max_length = 4) #CSDD
    tehsil_id = models.CharField(max_length = 2)
    tehsil_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.district_id + ' ' + self.tehsil_id + ' ' + self.tehsil_name

class GramPanchayat(models.Model):
    tehsil_id = models.CharField(max_length = 6) #CSDDTT
    gram_panchayat_id = models.CharField(max_length = 2)
    gram_panchayat_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.tehsil_id + ' ' + self.gram_panchayat_id + ' ' + self.gram_panchayat_name
