# Generated by Django 5.0 on 2023-12-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_grade_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grade_status',
            field=models.BooleanField(null=True),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]