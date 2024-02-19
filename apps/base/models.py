from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid
class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4)
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class RegionModel(MPTTModel, BaseModel):
    
    name = models.CharField(null=True, blank=True, max_length = 255)
    parent = TreeForeignKey('self',on_delete = models.CASCADE, null=True, blank=True, related_name = 'children')

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'

    
    def __str__(self) -> str:
        return self.name




    
