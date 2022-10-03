# Generated by Django 3.2 on 2022-10-02 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoApi', '0003_rename_item_no_item_product_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(default='John Doe', max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('imageUrl', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='DjangoApi.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(to='DjangoApi.Book')),
            ],
            options={
                'ordering': ['cart_id', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tag', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imageUrl', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='DjangoApi.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Dress',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='DjangoApi.Product'),
        ),
    ]
