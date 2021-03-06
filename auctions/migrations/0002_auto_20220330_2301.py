# Generated by Django 3.2.5 on 2022-03-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(blank=True, max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=60)),
                ('description', models.TextField(max_length=320)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=320)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.commodity')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_time', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField()),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.commodity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
