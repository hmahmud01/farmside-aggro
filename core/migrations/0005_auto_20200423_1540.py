# Generated by Django 2.2.10 on 2020-04-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('M', 'Milk'), ('C', 'Cow'), ('ME', 'Meat')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
