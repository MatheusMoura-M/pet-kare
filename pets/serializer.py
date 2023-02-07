from rest_framework import serializers
from .models import SexTypes
from groups.serializer import GroupSerializer
from traits.serializer import TraitSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexTypes.choices, default=SexTypes.DEFAULT
    )  # noqa
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
