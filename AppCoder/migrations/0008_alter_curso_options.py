# Generated by Django 4.2.4 on 2023-09-01 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_remove_profesor_curso_profesor_cursos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ('nombre',)},
        ),
    ]
