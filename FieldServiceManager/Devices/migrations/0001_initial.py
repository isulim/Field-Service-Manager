# Generated by Django 2.1.7 on 2019-03-30 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32, verbose_name='First name')),
                ('lastName', models.CharField(max_length=64, verbose_name='Last name')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('sn', models.CharField(max_length=13, verbose_name='Serial number')),
                ('modelName', models.CharField(max_length=64, verbose_name='Model')),
                ('installationDate', models.DateField(verbose_name='Installation date')),
                ('guaranteeDate', models.DateField(verbose_name='Guarantee date')),
                ('lastMaintenance', models.DateField(verbose_name='Last maintenance')),
                ('nextMaintenance', models.DateField(verbose_name='Next maintenance')),
                ('caretaker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='Devices.Caretaker', verbose_name='Caretaker')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('city', models.CharField(max_length=64, verbose_name='City')),
                ('address', models.CharField(max_length=128, verbose_name='Address')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='deviceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Devices.DeviceType', verbose_name='Device type'),
        ),
        migrations.AddField(
            model_name='device',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.Hospital', verbose_name='Hospital'),
        ),
        migrations.AddField(
            model_name='device',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Devices.Manufacturer', verbose_name='Manufacturer'),
        ),
        migrations.AddField(
            model_name='caretaker',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.Hospital', verbose_name='Hospital'),
        ),
    ]
