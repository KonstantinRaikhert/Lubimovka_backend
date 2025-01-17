from rest_framework import serializers

from apps.afisha.models import Event
from apps.core.serializers import ImageSerializer
from apps.library.models import Performance, PerformanceMediaReview, PerformanceReview, TeamMember
from apps.library.utilities import team_collector

from .play import PlaySerializer


class EventSerializer(serializers.ModelSerializer):
    """Serializer for performance."""

    class Meta:
        model = Event
        fields = ("id", "date_time", "paid", "url", "place")


class PerformanceSerializer(serializers.ModelSerializer):
    """Сериализатор Спектакля для отображения на странице Спектакля."""

    play = PlaySerializer()
    team = serializers.SerializerMethodField()
    images_in_block = ImageSerializer(many=True)
    events = serializers.SerializerMethodField()

    def get_team(self, obj):
        return team_collector(TeamMember, {"performance": obj})

    def get_events(self, obj):
        return EventSerializer(obj.events.body.first()).data

    class Meta:
        exclude = (
            "created",
            "modified",
            "project",
            "persons",
        )
        model = Performance


class EventPerformanceSerializer(serializers.ModelSerializer):
    """Сериализатор Спектакля для отображения на странице Афиши."""

    team = serializers.SerializerMethodField()
    image = serializers.ImageField(source="main_image")
    project_title = serializers.SlugRelatedField(slug_field="title", read_only=True, source="project")

    def get_team(self, obj):
        return team_collector(
            TeamMember,
            {"performance": obj, "role__slug__in": ["director", "dramatist"]},
        )

    class Meta:
        model = Performance
        fields = (
            "id",
            "name",
            "description",
            "team",
            "image",
            "project_title",
        )


class PerformanceMediaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceMediaReview
        exclude = (
            "created",
            "modified",
            "performance",
        )


class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        exclude = (
            "created",
            "modified",
            "performance",
        )
