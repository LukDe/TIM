from rest_framework import serializers
from tim_app.models import Good


class GoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Good
        fields = ('goodName', 'unit', 'description')
