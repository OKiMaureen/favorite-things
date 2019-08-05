from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import HStoreField
from simple_history.models import HistoricalRecords



# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'


    def __str__(self):
        return self.category_name
    
    history = HistoricalRecords()

class FavoriteThing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ranking = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    metadata = HStoreField(null=True, blank=True)
    audit_logs = HStoreField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='favourite_things',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(FavoriteThing, self).save(*args, **kwargs)

    class Meta:
        db_table = 'favorite_thing'
        ordering = ['ranking', ]
        constraints = [
            models.UniqueConstraint(fields=['title', 'category'],
                                    name='unique_favorite_thing')
        ]

    def __str__(self):
        return self.title
    
    history = HistoricalRecords()
