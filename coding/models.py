from django.db import models

# Create your models here.

# Category table cotains the various category of the articls like linked list, tree, queue etc


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.category_name)


# Article table cotanis article id article heading and cotegory


class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    article_heading = models.TextField()
    publish_date = models.DateField()
    decription = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.article_heading)
