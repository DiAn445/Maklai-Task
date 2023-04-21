from rest_framework import serializers


class ParaphraseSerializer(serializers.Serializer):
    tree = serializers.CharField(required=False)
    limit = serializers.IntegerField(default=20)

