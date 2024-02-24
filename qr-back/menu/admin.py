from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from menu import models
from django.utils.html import format_html
import qrcode
import qrcode.image.svg
from io import BytesIO
import base64
from django.conf import settings
from django import forms


class CategoryAdminCustomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryAdminCustomForm, self).__init__(*args, **kwargs)
        if not self.request.user.is_superuser:
            self.initial = {
                'store': self.request.user.store.id if self.request.user.store else None
            }

       
    class Meta:
        model = models.Category
        fields = '__all__'

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminCustomForm

    search_fields = ('id', 'name')
    def get_form(self, request, *args, **kwargs):
        form = super(CategoryAdmin, self).get_form(request,*args, **kwargs)
        form.request = request
        return form
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(store_id=request.user.store.id)

class FoodImageInline(admin.TabularInline):
    model = models.FoodImage
    extra = 0 
    fields = ('image_tag','image')
    readonly_fields = ('image_tag', )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))
    
    image_tag.short_description = 'Фотография'



class FoodCustomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FoodCustomForm, self).__init__(*args, **kwargs)
        if not self.request.user.is_superuser:
            self.initial = {
                'store': self.request.user.store.id if self.request.user.store else None
            }
            self.fields['category'].queryset = models.Category.objects.filter(store_id=self.request.user.store_id)
       
    class Meta:
        model = models.Category
        fields = '__all__'

@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [FoodImageInline]

    form = FoodCustomForm
    def get_form(self, request, *args, **kwargs):
        form = super(FoodAdmin, self).get_form(request,*args, **kwargs)
        form.request = request
        return form

    def image_tag(self, obj):
        if obj.images.first():
            return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.images.first().image.url))
        return 'Нету фотографий'
    
    image_tag.short_description = 'Фотография'
    
    list_display = ['image_tag','name','price', 'discount_price']
    list_display_links = ['name', 'image_tag']
    autocomplete_fields = ('category', )
    list_editable = ['price', 'discount_price']


    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(category__store_id=request.user.store_id)

def generate_qr_code_base64(url):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    buffer = BytesIO()
    img.save(buffer, format="PNG")

    # Convert the BytesIO object to a base64 string
    base64_string = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return base64_string



@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    
    def qr_code_tag(self, obj):
        image = "data:image/png;base64,"+generate_qr_code_base64(settings.HOSTNAME+"/resto/"+obj.slug)
        return format_html('<a download="qrcode.png" href="{}"><img src="{}" width="auto" height="200px" /></a>'.format(image, image))
    
    qr_code_tag.short_description = 'Получить qr'

    def image_tag(self, obj):
        if not obj.image:
            return 'Нет фото'
        return format_html('<img src="{}" width="300px" />'.format(obj.image.url))
    
    image_tag.short_description = 'Фотография'

    list_display = ('name','address', 'image_tag', 'qr_code_tag')
    list_display_links = ('image_tag','name')

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(id=request.user.store_id)
