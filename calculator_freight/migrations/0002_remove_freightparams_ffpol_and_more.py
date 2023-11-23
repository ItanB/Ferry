# Generated by Django 4.2.7 on 2023-11-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_freight', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freightparams',
            name='FFPOL',
        ),
        migrations.RemoveField(
            model_name='freightparams',
            name='stevedoring_POD',
        ),
        migrations.RemoveField(
            model_name='freightparams',
            name='stevedoring_POL',
        ),
        migrations.RemoveField(
            model_name='freightparams',
            name='tr_declaration',
        ),
        migrations.AddField(
            model_name='freightparams',
            name='freightForwarding',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='freight_nodriver',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='seconddriver',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='stevedoring_1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='stevedoring_2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='stevedoring_3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='stevedoring_nodriver_1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='stevedoring_nodriver_2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='stevedoring_nodriver_3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightparams',
            name='transitdecl',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='freightparams',
            name='ADR',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='freightparams',
            name='BAF',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='freightparams',
            name='ISPS',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='freightparams',
            name='el_connection',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='freightparams',
            name='freight',
            field=models.FloatField(default=0),
        ),
    ]