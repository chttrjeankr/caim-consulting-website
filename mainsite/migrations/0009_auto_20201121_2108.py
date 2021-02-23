# Generated by Django 3.0.8 on 2020-11-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20201014_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='contact_platform',
            field=models.CharField(choices=[('PHN', 'via Phone/WhatsApp'), ('EML', 'via Email'), ('WEB', 'via Website Chat')], default='WEB', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='mobile_num_chat',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]