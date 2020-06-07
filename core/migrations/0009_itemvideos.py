# Generated by Django 2.2.10 on 2020-06-05 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='item_videos')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_video', to='core.Item')),
            ],
        ),
    ]
