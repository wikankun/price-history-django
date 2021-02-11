from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class ItemUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()

class ItemPriceHistory(models.Model):
    item = models.ForeignKey(ItemUrl, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.updated_at = timezone.localtime(timezone.now())
        return super(ItemPriceHistory, self).save(*args, **kwargs)
