# Generated by Django 5.1.3 on 2025-01-19 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0017_remove_section6_architecture_architecture_section6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section9',
            name='interest_nearby',
        ),
        migrations.AddField(
            model_name='interestingnearbybuilding',
            name='section9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.section9', verbose_name='Обьект'),
        ),
    ]
