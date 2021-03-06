# Generated by Django 3.2.9 on 2021-12-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodcuts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(default='', max_length=450)),
                ('image', models.ImageField(upload_to='products/')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
