# Generated by Django 4.0.3 on 2023-01-11 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0008_remove_post_turmapertecente_delete_atividade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, max_length=250, null=True)),
                ('dataEntrega', models.DateField(blank=True, null=True)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='')),
                ('turmaPertecente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turmas.turma')),
            ],
        ),
    ]
