# Generated by Django 3.1.3 on 2021-01-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('demanda_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_demanda', models.CharField(max_length=100)),
                ('data_demanda', models.DateField()),
                ('rua_servico', models.CharField(max_length=100)),
                ('numero_endereco_servico', models.CharField(max_length=10)),
                ('bairro_servico', models.CharField(max_length=100)),
                ('cidade_servico', models.CharField(max_length=100)),
                ('desc_demanda', models.TextField(max_length=1400)),
                ('pessoas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demanda', to='pessoas.pessoa')),
                ('servico', models.ManyToManyField(related_name='demanda', to='servico.Servico')),
            ],
            options={
                'verbose_name': 'Demanda',
                'verbose_name_plural': 'Demandas',
            },
        ),
    ]
