# Generated by Django 4.2.1 on 2023-06-03 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRelatedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_related_images')),
                ('related_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product_image', to='ecommerceapp.product')),
            ],
        ),
    ]
