# Generated by Django 3.0.3 on 2020-04-13 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200413_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('color', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('gabarites', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Корпус',
                'verbose_name_plural': 'Корпусы',
            },
        ),
        migrations.CreateModel(
            name='GraphicsCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('memory', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Видеокарта',
                'verbose_name_plural': 'Видеокарты',
            },
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('power', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Блок питания',
                'verbose_name_plural': 'Блоки питания',
            },
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('socket', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('frequency', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('count_of_cores', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Процессор',
                'verbose_name_plural': 'Процессоры',
            },
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('type_of_ram', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'ОЗУ',
                'verbose_name_plural': 'ОЗУ',
            },
        ),
        migrations.RemoveField(
            model_name='computer',
            name='color',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='count_of_cores',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='gabarites',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='gpu',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='model',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='socket',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='type_of_product',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='type_of_ram',
        ),
        migrations.AlterField(
            model_name='computer',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category'),
        ),
        migrations.AddField(
            model_name='computer',
            name='corpus',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.Corpus'),
        ),
        migrations.AddField(
            model_name='computer',
            name='graphics',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.GraphicsCard'),
        ),
        migrations.AddField(
            model_name='computer',
            name='power',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.PowerSupply'),
        ),
        migrations.AddField(
            model_name='computer',
            name='processor',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.Processor'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='ram',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.Ram'),
        ),
    ]
