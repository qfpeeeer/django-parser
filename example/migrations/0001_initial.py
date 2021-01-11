# Generated by Django 3.1.5 on 2021-01-11 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.URLField(max_length=150, unique=True)),
                ('shop', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.URLField(max_length=150)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='example.category')),
            ],
            bases=('example.category',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='example.category')),
            ],
            bases=('example.category',),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='example.category')),
            ],
            bases=('example.category',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='example.category')),
            ],
            bases=('example.category',),
        ),
        migrations.CreateModel(
            name='PhoneHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='example.phone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonitorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='example.monitor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LaptopHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='example.laptop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeyboardHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='example.keyboard')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
