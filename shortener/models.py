from django.db import models


class Url(models.Model):
    full_url = models.URLField(
        verbose_name="Сокращаемая ссылка",
        help_text="Вставте ссылку для сокращения"
    )
    nums_of_visits = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_url[:30]
