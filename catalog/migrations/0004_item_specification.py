# Generated by Django 2.2.9 on 2021-03-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210324_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='specification',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]