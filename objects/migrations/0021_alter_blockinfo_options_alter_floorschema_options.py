# Generated by Django 5.1.3 on 2025-01-19 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0020_alter_interestingnearbybuilding_section9'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockinfo',
            options={'verbose_name': 'Планы этажа', 'verbose_name_plural': 'Планы этажей'},
        ),
        migrations.AlterModelOptions(
            name='floorschema',
            options={'verbose_name': 'Планировка блока', 'verbose_name_plural': 'Планировки блоков'},
        ),
    ]
