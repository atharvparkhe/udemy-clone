from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Sum
from django.dispatch import receiver
from authentication.models import LearnerModel
from app.models import CourseModel
from base.models import BaseModel


class WishlistModel(BaseModel):
    user = models.ForeignKey(LearnerModel, related_name="user_wishlist",on_delete=models.CASCADE)
    item = models.ForeignKey(CourseModel, related_name="course_wishlist", on_delete=models.CASCADE)
    def __str__(self):
        return self.user


class OrderModel(BaseModel):
    owner = models.ForeignKey(LearnerModel, related_name="customer_cart",on_delete=models.PROTECT)
    total_price = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    coupon_applied = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_signature = models.CharField(max_length=300, null=True, blank=True)
    invoice = models.FileField(upload_to="invoice", max_length=100, null=True, blank=True)
    def __str__(self):
        return self.owner.email


class OrderItemsModel(BaseModel):
    cart = models.ForeignKey(OrderModel, related_name="related_cart", on_delete=models.CASCADE)
    item = models.ForeignKey(CourseModel, related_name="related_items", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(default=0)


class Coupons(BaseModel):
    coupon_name = models.CharField(max_length=100, unique=True)
    coupon_discount_amount = models.FloatField(default=0.2)
    use_times = models.PositiveIntegerField(default=10)
    is_active = models.BooleanField(default=False)


@receiver(pre_save, sender=OrderItemsModel)
def get_items_total(sender, instance, *args, **kwargs):
    instance.total = instance.item.price * instance.quantity


@receiver(post_save, sender=OrderItemsModel)
def get_total_amt(sender, instance, *args, **kwargs):
    try:
        cart_obj = instance.cart
        cart_obj.total_price = cart_obj.related_cart.all().aggregate(Sum('total'))
        cart_obj.save()
    except Exception as e:
        print(e)


@receiver(pre_save, sender=Coupons)
def coupon_update(sender, instance, *args, **kwargs):
    try:
        instance.use_times -= 1
        if instance.use_times < 1:
            instance.is_active = False
            instance.save()
    except Exception as e:
        print(e)
