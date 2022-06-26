# Generated by Django 3.2.5 on 2022-06-26 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(max_length=100, verbose_name='Descricao')),
                ('date_fabrication', models.DateField(verbose_name='Data Fabricacao')),
                ('is_active', models.BooleanField(default=False, verbose_name='Ativo')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Foto')),
                ('doc', models.FileField(upload_to='docs', verbose_name='Documentos')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'ordering': ['id'],
            },
        ),
    ]
