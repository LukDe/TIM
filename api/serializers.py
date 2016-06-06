##
## Serializers
##
## This file is responsible for creating serializers, which parse and convert
## models from and into Json. All of the classes that need to be sent to the frontend
## must have a serializer.
##
from rest_framework import serializers
from tim_app.models import Good, Request


# Parses a Good model from tim_app.models.Good.
# The Meta class defines which model the serializer belongs to,
# and which fields are going to be in the Json.
class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('goodName', 'unit', 'description')


# Parses a Request model from tim_app.models.Request.
# The fields behave in the same way as GoodSerializer's fields do.
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
