# Generated by Django 3.1.1 on 2020-10-06 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionType', models.CharField(blank=True, choices=[(1, 'اختيار من متعدد'), (2, 'مقالى')], max_length=255, verbose_name='نوع السؤال')),
                ('question', models.CharField(blank=True, max_length=255, null=True, verbose_name='السؤال')),
                ('answer', models.CharField(blank=True, max_length=255, null=True, verbose_name='الإجابة')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='وصف الإمتحان'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الإسم'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='TotalResult',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الإسم'),
        ),
        migrations.CreateModel(
            name='TrueAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=255, verbose_name='السؤال')),
                ('trueAnswer', models.CharField(blank=True, max_length=255, verbose_name='الإجابة')),
                ('Exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.question')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.category')),
            ],
            options={
                'verbose_name': 'TrueAnswer',
                'verbose_name_plural': 'TrueAnswers',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='Exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.category'),
        ),
    ]
