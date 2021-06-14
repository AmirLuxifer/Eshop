# Generated by Django 3.2 on 2021-04-17 16:49

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سایت')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=50, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=50, verbose_name='تلفن همراه')),
                ('fax', models.CharField(max_length=50, verbose_name='فکس')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('about_us', models.TextField(verbose_name='درباره ما')),
                ('copy_right', models.CharField(max_length=200, verbose_name='متن کپی رایت')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='لوگوی سایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات',
            },
        ),
    ]