# Generated by Django 5.0.7 on 2024-08-08 14:07

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Image must be 200px by 200px.', upload_to='avatars/', validators=[users.models.validate_avatar]),
        ),
    ]
