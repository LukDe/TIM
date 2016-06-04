from rest_framework import serializers
from tim_app.models import Good, Request


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('goodName', 'unit', 'description')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = (
            'id', 'username',
            'goodName', 'misc',
            'quantity', 'priority',
            'catastrophy', 'postalCode',
            'creationDate'
        )
