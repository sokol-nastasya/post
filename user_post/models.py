from django.db import models

SHORT_TEXT_LEN = 200

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 150, verbose_name = 'Title')
    descriptions = models.TextField(verbose_name = 'Informations')
    date = models.DateTimeField(auto_now = True, verbose_name = 'Date')
    likes = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.descriptions) > SHORT_TEXT_LEN:
            return self.descriptions[:SHORT_TEXT_LEN]
        else:
            return self.descriptions

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
