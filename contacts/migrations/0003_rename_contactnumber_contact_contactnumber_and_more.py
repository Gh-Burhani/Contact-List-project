# Generated by Django 4.2.4 on 2023-08-27 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_contactnumber_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='ContactNumber',
            new_name='contactNumber',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
    ]
