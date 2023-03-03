from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        ordering=('-created_at',)

STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Draft', 'Draft'),
)

class Pricing(BaseModel):
    """
    Pricing config model
    """
    base_distance = models.IntegerField(null=True, default=0)
    base_time = models.IntegerField(null=True, default=0)
    distance_base_price = models.IntegerField(null=True, default=0)
    distance_additional_price = models.IntegerField(null=True, default=0)
    time_multiplier_factor = models.FloatField(null=True, default=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Draft')
    
    def __str__(self) -> str:
        return f"{self.id}"
