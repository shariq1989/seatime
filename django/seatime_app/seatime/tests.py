from django.contrib.auth.models import User
from django.test import TestCase

from .models import MarinerProfile, MarinerDocument


class MarinerProfileTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.user2 = User.objects.create_user(username='testuser1', password='12345')
        self.client.login(username='testuser1', password='12345')

    def test_mariner_profile(self):
        self.assertEquals(
            MarinerProfile.objects.count(), 0
        )
        MarinerProfile.objects.create(
            user=User.objects.get(username='testuser'),
            birth_date='1989-01-01',
            citizenship_cntry='USA',
            residence_state='Colorado',
            mariner_ref_num='60771'
        )
        MarinerProfile.objects.create(
            user=User.objects.get(username='testuser1'),
            birth_date='1987-09-09',
            citizenship_cntry='USA',
            residence_state='Arizona',
            mariner_ref_num='59231'
        )
        self.assertEquals(
            MarinerProfile.objects.count(), 2
        )

    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        self.assertEquals(
            MarinerProfile.objects.count(), 0
        )


class MarinerDocumentTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.user2 = User.objects.create_user(username='testuser1', password='12345')
        self.client.login(username='testuser1', password='12345')

    def test_mariner_document(self):
        self.assertEquals(
            MarinerDocument.objects.count(), 0
        )
        MarinerDocument.objects.create(
            user=User.objects.get(username='testuser'),
            mmc_doc_num='67890',
            mmc_issue_date='2000-01-01',
            mmc_expr_date='2026-01-01',
            med_ntl_expr_date='2001-01-01',
            med_stcw_expr_date='2002-08-01',
            med_pilot_expr_date='2030-04-01',
            twic_expr_date='2004-01-01',
            basic_training_expr_date='2004-01-11',
            advanced_fire_expr_date='2000-01-01',
            first_aid_cpr_expr_date='2000-01-01',
            passport_expr_date='2000-01-01',
            drug_test_compliant=True
        )
        self.assertEquals(
            MarinerDocument.objects.count(), 1
        )
        self.user.delete()
        self.user2.delete()
        self.assertEquals(
            MarinerDocument.objects.count(), 0
        )

    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        self.assertEquals(
            MarinerDocument.objects.count(), 0
        )
