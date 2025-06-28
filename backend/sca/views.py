from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from sca.models import Cat, Mission, Target
from sca.serializers import CatSerializer, CatUpdateSerializer, MissionDetailSerializer, MissionUpdateSerializer, \
    MissionListSerializer, MissionCreateSerializer, TargetUpdateSerializer


# 1. Cats views
# 1.1. Create cat
class CatCreateView(generics.CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def perform_create(self, serializer):
        serializer.save()

# 1.2. List of cats
class CatListView(generics.ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

# 1.3. Retrieve cat
class CatRetrieveView(generics.RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

# 1.4. Update info about cat (only salary)
class CatUpdateView(generics.UpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatUpdateSerializer

    def get_object(self):
        cat = super().get_object()
        return cat

    def perform_update(self, serializer):
        if 'salary' not in serializer.validated_data:
            raise ValidationError({"salary": "Only salary can be updated."})
        serializer.save()

# 1.5. Delete cat
class CatDeleteView(generics.DestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        cat_name = instance.name
        self.perform_destroy(instance)
        return Response(
            {"message": f"Cat {cat_name} was successfully deleted."},
            status=status.HTTP_200_OK
        )


# 2. Missions views
# 2.1. Create Mission
class MissionCreateView(generics.CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionCreateSerializer

# 2.2. List of Mission
class MissionListView(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionListSerializer

# 2.3. Mission details
class MissionDetailView(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionDetailSerializer

# 2.4. Mission update (only is_completed)
class MissionUpdateView(generics.UpdateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionUpdateSerializer

# 2.5. Mission delete (if not assigned)
class MissionDeleteView(generics.DestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionDetailSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.cat:
            return Response({"error": "You can't delete a mission if it's assigned to a cat."}, status=400)
        self.perform_destroy(instance)
        return Response({"message": f"Mission {instance.pk} successfully deleted."}, status=status.HTTP_200_OK)

# 2.6. Assigning a cat to a mission
class AssignCatToMissionView(generics.GenericAPIView):
    queryset = Mission.objects.all()

    def post(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        cat_id = request.data.get("cat_id")

        if not cat_id:
            return Response({"error": "cat_id is required."}, status=400)

        cat = get_object_or_404(Cat, pk=cat_id)

        if Mission.objects.filter(cat=cat).exists():
            return Response({"error": "This cat is already assigned to a mission."}, status=400)

        mission.cat = cat
        mission.save()
        return Response(
            {"message": f"Cat '{cat.name}' assigned to mission '{mission.name}'"},
            status=200
        )


# 3. Target views
class TargetUpdateView(generics.UpdateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetUpdateSerializer
