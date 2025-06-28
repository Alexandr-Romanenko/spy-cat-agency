import requests
from rest_framework import serializers
from .models import Cat, Mission, Target
from rest_framework.exceptions import ValidationError


# 1. Cat Serializers
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"

    def validate_breed(self, value):
        # Requesting a list of breeds from the API
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        if response.status_code != 200:
            raise ValidationError("Failed to fetch cat breeds from TheCatAPI.")
        breeds = response.json()

        # Checking for the presence of the breed
        if not any(breed["name"].lower() == value.lower() for breed in breeds):
            raise ValidationError(f"Breed '{value}' is not valid according to TheCatAPI.")
        return value

class CatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['salary']


# 2. Target Serializers
class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_completed']

    def validate(self, data):
        if self.instance and (self.instance.is_completed or self.instance.mission.is_completed):
            raise serializers.ValidationError("Cannot modify notes — target or mission completed.")
        return data

class TargetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'country', 'notes', 'is_completed']

class TargetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_completed']

class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['notes', 'is_completed']

    def validate(self, data):
        target = self.instance

        if 'notes' in data:
            if target.is_completed or target.mission.is_completed:
                raise serializers.ValidationError("Cannot update notes — target or mission is already completed.")

        return data


# 3. Mission Serializers
class MissionCreateSerializer(serializers.ModelSerializer):
    targets = TargetCreateSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['name', 'cat', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target in targets_data:
            Target.objects.create(mission=mission, **target)
        return mission

class MissionDetailSerializer(serializers.ModelSerializer):
    targets = TargetDetailSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_completed', 'targets']

class MissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_completed']

class MissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['is_completed']

    def validate_is_completed(self, value):
        if value:
            mission = self.instance
            incomplete_targets = mission.targets.filter(is_completed=False)
            if incomplete_targets.exists():
                raise serializers.ValidationError(
                    "Mission cannot be marked as completed until all targets are completed."
                )
        return value
