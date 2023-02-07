from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .serializer import PetSerializer
import ipdb


class PetView(APIView):
    def get(self, request):
        return Response({"msg": "Rota GET de Pets!"})

    def post(self, request):
        serializer = PetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        g1 = Group.objects.get(
            scientific_name=serializer.validated_data["group"][
                "scientific_name"
            ]  # noqa
        )
        serializer.validated_data["group"] = g1

        t1 = Trait.objects.get(
            name=serializer.validated_data["traits"][0]["name"]
        )  # noqa

        serializer.validated_data["traits"][0] = t1

        pet = Pet.objects.create(**serializer.validated_data)

        serializer = PetSerializer(pet)

        return Response(serializer.data, status.HTTP_201_CREATED)
