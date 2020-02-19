# Generated by Django 3.0.3 on 2020-02-18 11:16

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(max_length=100, verbose_name='Criado')),
                ('modificado', models.DateField(max_length=100, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menu.Base')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Preço')),
                ('imagem', stdimage.models.StdImageField(upload_to='media', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'cardapio',
                'verbose_name_plural': 'cardapios',
            },
            bases=('menu.base',),
        ),
    ]