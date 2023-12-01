from django.contrib import admin

# Register your models here.

from.models import Children
from.models import Admin
from.models import Adoption
from.models import StatusForChildren

admin.site.register(Children)
admin.site.register(Admin)
admin.site.register(Adoption)
admin.site.register(StatusForChildren)
