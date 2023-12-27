from django.db import models



class Movie(models.Model):

    GENRE_CHOICES = [
        ('Triller', 'Triller'),
        ('Action', 'Action'),
        ('Horal', 'Horal'),
        ('Drama', 'Drama'),
    ]

    author = models.CharField("Movie Author" , max_length=50)
    title  = models.CharField('Title' ,max_length=128, unique=True)
    genre = models.CharField('Genres' ,max_length=50, choices=GENRE_CHOICES)
    year = models.PositiveIntegerField('Year')
    img = models.ImageField('Movie Image' , upload_to='media' , null=True)



    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='Movie'
        verbose_name_plural='Movies'















