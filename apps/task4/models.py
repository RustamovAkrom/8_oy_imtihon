from django.db import models


class AbstractBaseMode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UsersTask4(AbstractBaseMode):
    username = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.username


class Pinned_leagues(AbstractBaseMode):
    leagues = models.ForeignKey("task4.Leagues", models.CASCADE, "pinned_leagues")

    def __str__(self) -> str:
        return self.leagues.name


class Categories(AbstractBaseMode):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Countryes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Bookmakers(models.Model):
    cover = models.ImageField(upload_to="images/bookmakers/")
    url = models.URLField()


class Leagues(AbstractBaseMode):
    form_choices = [
        ("?", "?"),
        ("w", "W"),
        ("d", "D"),
        ("l", "L"),
    ]

    name = models.CharField(max_length=120)
    cover = models.ImageField(upload_to="images/legues/")
    country = models.ForeignKey(Countryes, models.CASCADE)
    stadium = models.CharField(max_length=128, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    last_date = models.DateField()
    finished = models.IntegerField(default=0)
    form = models.CharField(choices=form_choices, max_length=1, null=True, blank=True)


class Matches(AbstractBaseMode):
    round = models.IntegerField(default=0)
    liga1 = models.ForeignKey(Leagues, models.CASCADE, "liga1")
    # liga1 VS liga2
    liga2 = models.ForeignKey(Leagues, models.CASCADE, "liga2")
    date = models.DateTimeField()
    summary = models.TextField()
    report = models.TextField()
    odds = models.ForeignKey(Bookmakers, models.DO_NOTHING, "matches")
    h2h = None
    standings = models.ForeignKey(Leagues, models.CASCADE)
    news = models.ForeignKey("task4.News", models.DO_NOTHING, "matches")
    videos = models.FileField(upload_to="videos/matches/")
    history = models.CharField(max_length=5)


class Scores(AbstractBaseMode):
    categories = models.ForeignKey(Categories, models.CASCADE)
    matches = models.ForeignKey(Matches, models.CASCADE, "scores")


class News(AbstractBaseMode):
    title = models.CharField(max_length=120)
    categories = models.ForeignKey(Categories, models.CASCADE)
    description = models.TextField()
    content = models.TextField()
