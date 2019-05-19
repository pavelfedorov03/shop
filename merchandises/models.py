from django.db import models


class Merchandise(models.Model):
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    text = models.TextField(max_length=500)
    title = models.CharField(max_length=40)
    seller = models.ForeignKey(
        to='sellers.Seller',
        related_name='merchandises',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

