# Generated by Django 2.2.16 on 2020-10-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0234_remove_obsolete_block_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfgovpage',
            name='is_archived',
            field=models.CharField(choices=[('false', 'No'), ('true', 'Yes'), ('never', 'Never')], default='false', help_text='If "Never" is selected, the page will not be archived automatically after a certain period of time.', max_length=16, verbose_name='This page is archived'),
        ),
    ]