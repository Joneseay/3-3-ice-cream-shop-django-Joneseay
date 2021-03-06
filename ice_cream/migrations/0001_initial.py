# Generated by Django 2.1.5 on 2019-05-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=100)),
                ('base', models.CharField(choices=[('CHOCOLATE', 'chocolate'), ('VANILLA', 'vanilla')], max_length=100)),
                ('available', models.CharField(choices=[('DAILY', 'daily'), ('WEEKLY', 'weekly'), ('SEASONAL', 'seasonal')], max_length=100)),
                ('featured', models.BooleanField()),
                ('date', models.DateField()),
            ],
        ),
    ]
