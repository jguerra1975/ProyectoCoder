# Generated by Django 4.2.4 on 2023-09-01 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_alter_curso_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ('nombre', 'camada')},
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('nombre', 'camada')},
        ),
    ]