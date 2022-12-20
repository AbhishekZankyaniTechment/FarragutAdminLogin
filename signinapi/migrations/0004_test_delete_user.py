# Generated by Django 4.1 on 2022-08-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signinapi', '0003_user_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]