from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .serializers import PetSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


class PetView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        trait_param = request.query_params.get("trait")
        pets = Pet.objects.all()

        if trait_param:
            filtered = Pet.objects.filter(traits__name__iexact=trait_param)

            result_page = self.paginate_queryset(filtered, request)
            serializer = PetSerializer(result_page, many=True)

            return self.get_paginated_response(serializer.data)

        result_page = self.paginate_queryset(pets, request)

        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        group_obj = serializer.validated_data.pop("group")
        traits_list = serializer.validated_data.pop("traits")

        # Group
        group_filter = Group.objects.filter(
            scientific_name__iexact=group_obj["scientific_name"]
        ).first()

        if not group_filter:
            group_filter = Group.objects.create(**group_obj)

        # Pet
        pet_obj = Pet.objects.create(**serializer.validated_data, group=group_filter)

        # Traits
        for trait_dict in traits_list:
            trait_filter = Trait.objects.filter(name__iexact=trait_dict["name"]).first()

            if not trait_filter:
                trait_filter = Trait.objects.create(**trait_dict)

            pet_obj.traits.add(trait_filter)

        serializer = PetSerializer(pet_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def patch(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        group_obj = serializer.validated_data.pop("group", None)
        traits_list = serializer.validated_data.pop("traits", None)

        # Group
        if group_obj:
            try:
                group_found = Group.objects.get(
                    scientific_name=group_obj["scientific_name"]
                )
            except Group.DoesNotExist:
                group_found = Group.objects.create(**group_obj)

            pet.group = group_found

        # Traits
        if traits_list:
            new_traits = []
            for trait_dict in traits_list:
                trait_filter = Trait.objects.filter(
                    name__iexact=trait_dict["name"]
                ).first()

                if not trait_filter:
                    trait_filter = Trait.objects.create(**trait_dict)

                new_traits.append(trait_filter)

            pet.traits.set(new_traits)

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)

        pet.save()

        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
