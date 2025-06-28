from django.urls import path
from .views import (
    CatCreateView, CatListView, CatRetrieveView, CatUpdateView, CatDeleteView, MissionListView, MissionCreateView,
    MissionDetailView, MissionUpdateView, MissionDeleteView, AssignCatToMissionView, TargetUpdateView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [

    # Cat endpoints
    path("cats/", CatListView.as_view(), name="cat-list"),
    path("cat/create/", CatCreateView.as_view(), name="cat-create"),
    path("cat/<int:pk>/", CatRetrieveView.as_view(), name="cat-detail"),
    path("cat/<int:pk>/update/", CatUpdateView.as_view(), name="cat-update"),
    path("cat/<int:pk>/delete/", CatDeleteView.as_view(), name="cat-delete"),

    # Mission endpoints
    path("missions/", MissionListView.as_view(), name="mission-list"),
    path("mission/create/", MissionCreateView.as_view(), name="mission-create"),
    path("mission/<int:pk>/detail/", MissionDetailView.as_view(), name="mission-detail"),
    path("mission/<int:pk>/update/", MissionUpdateView.as_view(), name="mission-update"),
    path("mission/<int:pk>/delete/", MissionDeleteView.as_view(), name="mission-delete"),
    path("mission/<int:pk>/assign-cat/", AssignCatToMissionView.as_view(), name="mission-assign-cat"),

    # Target endpoints
    path('target/<int:pk>/update/', TargetUpdateView.as_view(), name='target-update'),

]

urlpatterns += router.urls
