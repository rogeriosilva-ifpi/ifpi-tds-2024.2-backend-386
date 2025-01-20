# Generated by Django 5.1.4 on 2025-01-16 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_fabricante_ano_fundacao_fabricante_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('motor', models.CharField(blank=True, choices=[('1.0', 'Motor 1.0'), ('1.3', 'Motor 1.3'), ('1.4', 'Motor 1.4'), ('1.6', 'Motor 1.6'), ('1.8', 'Motor 1.8'), ('2.0', 'Motor 2.0')], max_length=5, null=True)),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='modelos', to='core.fabricante')),
            ],
        ),
    ]
