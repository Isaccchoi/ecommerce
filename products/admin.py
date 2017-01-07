from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Variation
from .models import ProductImage
from .models import Category
from .models import ProductFeatured

admin.site.register(Product)

admin.site.register(Variation)

admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(ProductFeatured)
