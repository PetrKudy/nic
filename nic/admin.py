from django.contrib import admin
from .models import Domain, DomainFlag


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    pass


@admin.register(DomainFlag)
class DomainFlagAdmin(admin.ModelAdmin):
    pass
