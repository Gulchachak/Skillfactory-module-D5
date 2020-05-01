# Generated by Django 2.2.6 on 2020-05-01 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200206_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
                ('inspirer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspired_works', to='p_library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=60)),
                ('friend_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='p_library.Inspiration', to='p_library.Author'),
        ),
    ]