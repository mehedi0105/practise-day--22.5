# Generated by Django 5.0.6 on 2024-06-27 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_tranfer2'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceForm',
            fields=[
                ('tranfer2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transactions.tranfer2')),
            ],
            bases=('transactions.tranfer2',),
        ),
    ]
