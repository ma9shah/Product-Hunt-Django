# Generated by Django 2.2.2 on 2019-06-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='upvoters',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]