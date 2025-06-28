from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name

class Mission(models.Model):
    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    cat = models.OneToOneField(Cat, on_delete=models.SET_NULL, null=True, blank=True, related_name="mission")

    def __str__(self):
        return f"Mission {self.name}"

    def check_completion(self):
        if all(t.is_completed for t in self.targets.all()):
            self.is_completed = True
            self.save()


class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="targets")
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('mission', 'name')
        verbose_name = "Target"
        verbose_name_plural = "Targets"

    def __str__(self):
        return f"{self.name} ({self.country})"

    