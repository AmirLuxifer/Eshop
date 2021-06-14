from django.contrib import admin

from .models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'link']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
