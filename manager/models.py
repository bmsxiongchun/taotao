# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    title = models.CharField(max_length=200, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    title_desc = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    pic = models.CharField(max_length=300, blank=True, null=True)
    pic2 = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_content'


class TbContentCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_parent = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_content_category'


class TbItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    sell_point = models.CharField(max_length=500, blank=True, null=True)
    price = models.BigIntegerField()
    num = models.IntegerField()
    barcode = models.CharField(max_length=30, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    cid = models.BigIntegerField()
    status = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tb_item'


class TbItemCat(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_parent = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_item_cat'


class TbItemDesc(models.Model):
    item_id = models.BigIntegerField(primary_key=True)
    item_desc = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_item_desc'


class TbItemParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_cat_id = models.BigIntegerField(blank=True, null=True)
    param_data = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_item_param'


class TbItemParamItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.BigIntegerField(blank=True, null=True)
    param_data = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_item_param_item'


class TbOrder(models.Model):
    order_id = models.CharField(primary_key=True, max_length=50)
    payment = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    post_fee = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    payment_time = models.DateTimeField(blank=True, null=True)
    consign_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    close_time = models.DateTimeField(blank=True, null=True)
    shipping_name = models.CharField(max_length=20, blank=True, null=True)
    shipping_code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    buyer_message = models.CharField(max_length=100, blank=True, null=True)
    buyer_nick = models.CharField(max_length=50, blank=True, null=True)
    buyer_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_order'


class TbOrderItem(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    item_id = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    num = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    total_fee = models.BigIntegerField(blank=True, null=True)
    pic_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_order_item'


class TbOrderShipping(models.Model):
    order_id = models.CharField(primary_key=True, max_length=50)
    receiver_name = models.CharField(max_length=20, blank=True, null=True)
    receiver_phone = models.CharField(max_length=20, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=30, blank=True, null=True)
    receiver_state = models.CharField(max_length=10, blank=True, null=True)
    receiver_city = models.CharField(max_length=10, blank=True, null=True)
    receiver_district = models.CharField(max_length=20, blank=True, null=True)
    receiver_address = models.CharField(max_length=200, blank=True, null=True)
    receiver_zip = models.CharField(max_length=6, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_order_shipping'


class TbUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=32)
    phone = models.CharField(unique=True, max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tb_user'
