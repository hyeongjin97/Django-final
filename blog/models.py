from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=10)
    pub_date= models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(blank = True, null = True, upload_to = "blog/")


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]