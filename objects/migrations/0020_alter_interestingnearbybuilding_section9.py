# Generated by Django 5.1.3 on 2025-01-19 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0019_alter_section6_options_alter_section9_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestingnearbybuilding',
            name='section9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interesteds_secrion', to='objects.section9', verbose_name='Обьект'),
        ),
    ]
