from rest_framework import serializers


class StripeSessionIdSerializer(serializers.Serializer):

    id = serializers.CharField()
