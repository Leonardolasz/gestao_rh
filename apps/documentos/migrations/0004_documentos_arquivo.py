# Generated by Django 4.1.5 on 2023-02-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_alter_documentos_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
