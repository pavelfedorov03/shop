from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(max_length=300)
    seller = models.ForeignKey(
        to='sellers.Seller',
        related_name='comments',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

