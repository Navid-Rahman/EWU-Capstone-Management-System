# Generated by Django 3.0.14 on 2023-01-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposedTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=30)),
                ('member2', models.CharField(max_length=30)),
                ('member3', models.CharField(blank=True, max_length=30)),
                ('paper1', models.CharField(max_length=30)),
                ('paper2', models.CharField(max_length=30)),
                ('paper3', models.CharField(max_length=30)),
                ('paper4', models.CharField(max_length=30)),
                ('paper5', models.CharField(max_length=30)),
            ],
        ),
    ]