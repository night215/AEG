from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0003_auto_20180812_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='min_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
