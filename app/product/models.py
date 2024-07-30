
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255) # 제품명
    product_kind = models.CharField(max_length=255) # 유형명
    manufacture = models.CharField(max_length=255) # 제조원
    allergy = models.TextField() # 알레르기 유발 물질
    nutrient = models.TextField() # 영양 성분
    product_img = models.URLField(null=True, blank=True) # 제품 이미지
    meta_img = models.URLField(null=True, blank=True) # 메타 이미지 (없어도 될 듯함.)

    def __str__(self):
        return self.product_name

