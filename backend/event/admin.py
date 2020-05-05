from django.contrib import admin
from .models import (
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

admin.site.register(Schedule)
admin.site.register(Sponsor)
admin.site.register(Presenter)
admin.site.register(VendorDetail)
admin.site.register(Location)
admin.site.register(MySchedule)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Faq)
admin.site.register(Favorites)

# Register your models here.
