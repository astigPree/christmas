# Generated by Django 4.2.16 on 2024-10-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envelope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
                ('tree_id', models.CharField(blank=True, max_length=255, null=True)),
                ('image_index', models.SmallIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('expires_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=225, null=True)),
                ('tree_id', models.CharField(blank=True, max_length=255, null=True)),
                ('location_name', models.CharField(blank=True, max_length=255)),
                ('location', models.JSONField(blank=True, default=dict, null=True)),
                ('image_index', models.SmallIntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('found_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_found', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
