# Generated by Django 3.2.5 on 2022-06-23 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetworks', '0002_alter_socialnetwork_options'),
        ('clients', '0005_remove_client_client_socialnetwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialnetworks.socialnetwork'),
        ),
    ]