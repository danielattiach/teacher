# Generated by Django 2.1.4 on 2018-12-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181216_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('user_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
