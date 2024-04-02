from django import forms
from django.db import models


# Create your models here.
class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=256, unique=True, default='')
    game_icon = models.ImageField(upload_to='')


class Calculator(forms.Form):
    calculator_id = models.AutoField(primary_key=True)
    souls_needed = forms.IntegerField()
    current_level = forms.IntegerField()
    desired_level = forms.IntegerField()
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return (f'To reach level {self.desired_level} from level {self.current_level},'
                f' you need {self.souls_needed:,} souls')
