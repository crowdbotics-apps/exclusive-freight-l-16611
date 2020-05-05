from rest_framework import authentication
from event.models import (
    Vendor,
    Location,
    Favorites,
    VendorDetail,
    Category,
    Faq,
    Presenter,
    Schedule,
    MySchedule,
    Sponsor,
)
from .serializers import (
    VendorSerializer,
    LocationSerializer,
    FavoritesSerializer,
    VendorDetailSerializer,
    CategorySerializer,
    FaqSerializer,
    PresenterSerializer,
    ScheduleSerializer,
    MyScheduleSerializer,
    SponsorSerializer,
)
from rest_framework import viewsets


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Schedule.objects.all()


class SponsorViewSet(viewsets.ModelViewSet):
    serializer_class = SponsorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sponsor.objects.all()


class PresenterViewSet(viewsets.ModelViewSet):
    serializer_class = PresenterSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Presenter.objects.all()


class VendorDetailViewSet(viewsets.ModelViewSet):
    serializer_class = VendorDetailSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = VendorDetail.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Location.objects.all()


class MyScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = MyScheduleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MySchedule.objects.all()


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Vendor.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Faq.objects.all()


class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Favorites.objects.all()
