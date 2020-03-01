from django.contrib.auth.models import User
from django.test import TestCase

from .models import MarinerProfile


class MarinerProfileTestCase(TestCase):
    def test_mariner_profile(self):
        self.assertEquals(
            MarinerProfile.objects.count(),
            0
        )
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser2', password='12345')
        MarinerProfile.objects.create(
            user=self.user,
            birth_date='1989-01-01',
            citizenship_cntry='USA',
            residence_state='Colorado',
            mariner_ref_num='60771'
        )
        MarinerProfile.objects.create(
            user=self.user2,
            birth_date='1987-09-09',
            citizenship_cntry='USA',
            residence_state='Arizona',
            mariner_ref_num='59231'
        )
        self.assertEquals(
            MarinerProfile.objects.count(),
            2
        )
