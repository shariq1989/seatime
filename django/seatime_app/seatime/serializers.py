from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import MarinerDocument, MarinerProfile, Vessel, WorkdayType, VoyageType, \
    StaffPosition, Voyage, Rating, StaffRatingCombinations, Album


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')


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
    id = serializers.IntegerField()

    class Meta:
        model = MarinerProfile
        fields = (
            'id', 'user', 'first_name', 'middle_name', 'last_name', 'birth_date', 'citizenship_cntry',
            'residence_state')
        # this was needed to allow blank on middle name
        extra_kwargs = {'middle_name': {'required': False, 'allow_blank': True}}


class MarinerProfileNoIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarinerProfile
        fields = (
            'user', 'first_name', 'middle_name', 'last_name', 'birth_date', 'citizenship_cntry',
            'residence_state')
        # this was needed to allow blank on middle name
        extra_kwargs = {'middle_name': {'required': False, 'allow_blank': True}}


class MarinerDocumentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = MarinerDocument
        fields = (
            'id', 'user', 'mariner_ref_num', 'mmc_doc_num', 'mmc_issue_date', 'mmc_expr_date', 'med_ntl_expr_date',
            'med_stcw_expr_date', 'med_pilot_expr_date', 'twic_expr_date', 'basic_training_expr_date',
            'advanced_fire_expr_date', 'first_aid_cpr_expr_date', 'passport_expr_date', 'drug_test_compliant')


class MarinerDocumentNoIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarinerDocument
        fields = (
            'user', 'mariner_ref_num', 'mmc_doc_num', 'mmc_issue_date', 'mmc_expr_date', 'med_ntl_expr_date',
            'med_stcw_expr_date', 'med_pilot_expr_date', 'twic_expr_date', 'basic_training_expr_date',
            'advanced_fire_expr_date', 'first_aid_cpr_expr_date', 'passport_expr_date', 'drug_test_compliant')


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('id', 'name', 'official_number')


class WorkdayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkdayType
        fields = ('id', 'type',)


class VoyageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoyageType
        fields = ('id', 'type',)


class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = ('id', 'user', 'vessel', 'depart_date', 'arrival_date', 'voyage_type', 'workday_type',
                  'position')


class StaffPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPosition
        fields = ('id', 'title',)


class StaffRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'title',)


class StaffRatingCombinationsSerializer(serializers.ModelSerializer):
    positions = StaffPositionSerializer(read_only=True)
    ratings = StaffRatingSerializer(many=True, read_only=True)

    class Meta:
        model = StaffRatingCombinations
        fields = ['positions', 'ratings']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
