# Generated by Django 4.1.7 on 2023-02-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Under17', '0009_alter_calciatore_immagine_calciatore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calciatore',
            name='immagine_calciatore',
            field=models.ImageField(blank=True, default='../static/images/lnd.png', upload_to='foto_calciatori/'),
        ),
    ]
