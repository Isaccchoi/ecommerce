from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Variation
from .models import ProductImage

admin.site.register(Product)

admin.site.register(Variation)

admin.site.register(ProductImage)
