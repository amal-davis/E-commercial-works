# Generated by Django 4.2.1 on 2023-06-19 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bloomapp', '0005_order_orderitem_order_items_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloomapp.orderitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
