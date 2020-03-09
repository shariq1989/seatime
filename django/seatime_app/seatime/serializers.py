from django.contrib.auth.models import User
from rest_framework import serializers

from .models import MarinerDocument, MarinerProfile, Vessel, WorkdayType, VoyageType, \
    StaffPosition, Voyage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'is_staff']


class MarinerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarinerProfile
        fields = ('user', 'birth_date', 'citizenship_cntry', 'residence_state', 'mariner_ref_num')


class MarinerDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarinerDocument
        fields = ('user', 'mmc_doc_num', 'mmc_issue_date', 'mmc_expr_date', 'med_ntl_expr_date', 'med_stcw_expr_date',
                  'med_pilot_expr_date', 'twic_expr_date', 'basic_training_expr_date',
                  'advanced_fire_expr_date', 'first_aid_cpr_expr_date', 'passport__expr_date', 'drug_test_compliant')


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('name', 'official_number', 'tonnage', 'propulsion', 'hp')


class WorkdayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkdayType
        fields = ('type',)


class VoyageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoyageType
        fields = ('type',)


class StaffPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPosition
        fields = ('department', 'title', 'rank')


class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = ('user', 'vessel', 'depart_date', 'arrival_date', 'voyage_type', 'workday_type',
                  'position')
