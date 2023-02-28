# Generated by Django 4.1.6 on 2023-02-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbr_students', models.IntegerField(null=True)),
                ('german_mean_note', models.FloatField(null=True)),
                ('math_mean_note', models.FloatField(null=True)),
                ('portuguese_mean_note', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('salary', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('frequency', models.FloatField(null=True)),
                ('german', models.FloatField(null=True)),
                ('mathematics', models.FloatField(null=True)),
                ('portuguese', models.FloatField(null=True)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.classroom')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='professors',
            field=models.ManyToManyField(blank=True, related_name='professors', to='api.professor'),
        ),
    ]
