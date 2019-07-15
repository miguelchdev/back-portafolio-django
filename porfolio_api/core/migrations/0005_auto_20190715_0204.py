# Generated by Django 2.2.3 on 2019-07-15 02:04

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190715_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file',
            field=versatileimagefield.fields.VersatileImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='image_ppoi'),
        ),
    ]