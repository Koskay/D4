from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE,
                                related_name="book_author")
    redaction = models.ForeignKey("Redaction", on_delete=models.CASCADE,null=True,blank=True,
                                related_name="book_house")
    copy_count = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    friends = models.ManyToManyField("Friend", blank=True,
                                     related_name="friends_books")
    def __str__(self):
        return self.title

class Redaction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name




class Friend(models.Model):
    full_name = models.TextField()

    def __str__(self):
        return self.full_name

