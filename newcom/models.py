from django.utils.text import slugify
from django_google_maps import fields as map_fields
from django.db import models
import string
import random
from django.contrib.auth.models import User


# Create your models here.

# images for IDstr
# def upload_id_image(filename):
#     return f' ids/{filename}'.format(filename=filename)


# images for product category
# def upload_productcategory_image(instance, filename, user=None):
#     return f' productcategory/{user}/{filename}'.format(user=instance.user, filename=filename)


# def my_slugify(text):
#     idn = random.randint(1, 50000)
#     text = text.lower()
#     unsafe = [letter for letter in text if letter == " "]
#     if unsafe:
#         for letter in unsafe:
#             text = text.replace(letter, '-')
#     text = u'_'.join(text.split())
#     text = f'{text}-{idn}'
#     return text


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=250, blank=True)
    product_category_image = models.ImageField(upload_to='upload_productcategory_image', blank=True)
    slug = models.SlugField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + rand_slug())
        super(ProductCategory, self).save(*args, **kwargs)


class Ids(models.Model):
    id_type = models.CharField(max_length=100)
    id_image = models.ImageField(help_text='Picture of the id ', upload_to='ids', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.id_type

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.id_type + "-" + rand_slug())
        super(Ids, self).save(*args, **kwargs)


class VendorSign(models.Model):
    name_of_vendor = models.CharField(max_length=50)
    name_of_shop = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15)
    phone_number1 = models.CharField(max_length=15, blank=True)
    biz_registration = models.ImageField(upload_to='upload_vendor_details_image', blank=True)
    shop_place_image = models.ImageField(upload_to='upload_vendor_details_image', blank=True)
    id_type = models.ForeignKey(Ids, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=50, unique=True)
    id_image = models.ImageField(upload_to='upload_vendor_details_image')
    current_image = models.ImageField(upload_to='upload_vendor_details_image', blank=True,
                                      help_text='current image please')
    email_add = models.EmailField(unique=True, max_length=250)
    location = map_fields.AddressField(max_length=200)
    ghana_post_address = models.CharField(max_length=20, blank=True)
    category = models.ManyToManyField(ProductCategory)
    slug = models.SlugField(unique=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_vendor + ' - ' + self.name_of_shop

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_of_vendor + "-" + rand_slug())
        super(VendorSign, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = my_slugify(self.name_of_vendor + ' - ' + self.name_of_shop)
    #     super(VendorSign, self).save(*args, **kwargs)

""""
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_short_name = models.CharField(max_length=100, blank=True, help_text='A short name eg.Iphone SE')
    product_brand = models.CharField(max_length=250, help_text='a brand name eg. Apple')
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=15, decimal_places=2)
    product_discount_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    # discount_percentage = models.
    product_image = models.ImageField(upload_to='products')
    product_image_1 = models.ImageField(upload_to='products', blank=True)
    product_image_2 = models.ImageField(upload_to='products', blank=True)
    product_image_3 = models.ImageField(upload_to='products', blank=True)
    product_image_4 = models.ImageField(upload_to='products', blank=True)
    product_image_5 = models.ImageField(upload_to='products', blank=True)
    product_video = models.FileField(upload_to='videos/', blank=True)
    product_stock = models.IntegerField()
    operating_system = models.CharField(max_length=25, blank=True)
    # product_size = models.CharField()
    available = models.BooleanField(default=True)
    vendor = models.ForeignKey(VendorSign, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    # user = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_short_name

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.product_short_name)
        super(Product, self).save(*args, **kwargs)


# how to add a copyright water to images django
# categories in django 
""
# "class Cart(models.Model):
#     cart_id = models.CharField(max_length=250, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# 
#     class Meta:
#         db_table = 'Cart'
#         ordering = ['created_at']
# 
#     def __str__(self):
#         return self.cart_id"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return self.quantity * self.product.product_price

    def __str__(self):
        return self.product


class ProductAfter(models.Model):
    product_name = models.CharField(max_length=250)
    product_short_name = models.CharField(max_length=100, blank=True, help_text='A short name eg.Iphone SE')
    product_brand = models.CharField(max_length=250, help_text='a brand name eg. Apple')
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=15, decimal_places=2)
    product_discount_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    # discount_percentage = models.
    product_image = models.ImageField(upload_to='products')
    product_image_1 = models.ImageField(upload_to='products', blank=True)
    product_image_2 = models.ImageField(upload_to='products', blank=True)
    product_image_3 = models.ImageField(upload_to='products', blank=True)
    product_image_4 = models.ImageField(upload_to='products', blank=True)
    product_image_5 = models.ImageField(upload_to='products', blank=True)
    product_video = models.FileField(upload_to='videos/', blank=True)
    product_stock = models.IntegerField()
    operating_system = models.CharField(max_length=25, blank=True)
    # product_size = models.CharField()
    available = models.BooleanField(default=True)
    vendor = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    # user = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    token = models.CharField(max_length=230, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    email_address = models.EmailField(max_length=200, blank=True)
    billing_name = models.CharField(max_length=200, blank=True)
    billing_address = models.CharField(max_length=200, blank=True)
    billing_addresss1 = models.CharField(max_length=200, blank=True)
    billing_city = models.CharField(max_length=200, blank=True)
    billing_country = models.CharField(max_length=200, blank=True)
    shipping_name = models.CharField(max_length=200, blank=True)
    shipping_address = models.CharField(max_length=200, blank=True)
    shipping_city = models.CharField(max_length=200, blank=True)
    shipping_country = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class OrderItem(models.Model):
    product = models.CharField(max_length=240)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def sub_total(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product
"""""
