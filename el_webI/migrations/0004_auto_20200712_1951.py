# Generated by Django 2.2.6 on 2020-07-12 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('el_webI', '0003_component_status_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant_power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Board_Log_24hr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_energy_consumed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Device_Log_24hr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_time', models.IntegerField()),
                ('oncount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='home',
        ),
        migrations.RenameField(
            model_name='component_data',
            old_name='room',
            new_name='boardNo',
        ),
        migrations.RenameField(
            model_name='component_data',
            old_name='typ',
            new_name='deviceNo',
        ),
        migrations.AddField(
            model_name='device_log_24hr',
            name='dev_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='el_webI.Component_data'),
        ),
        migrations.AddField(
            model_name='board_log_24hr',
            name='dev1_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev1_id', to='el_webI.Device_Log_24hr'),
        ),
        migrations.AddField(
            model_name='board_log_24hr',
            name='dev2_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev2_id', to='el_webI.Device_Log_24hr'),
        ),
        migrations.AddField(
            model_name='board_log_24hr',
            name='dev3_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev3_id', to='el_webI.Device_Log_24hr'),
        ),
        migrations.AddField(
            model_name='board_log_24hr',
            name='dev4_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev4_id', to='el_webI.Device_Log_24hr'),
        ),
        migrations.AddField(
            model_name='board_log_24hr',
            name='dev5_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev5_id', to='el_webI.Device_Log_24hr'),
        ),
        migrations.AddField(
            model_name='board',
            name='dev1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev1_id', to='el_webI.Component_data'),
        ),
        migrations.AddField(
            model_name='board',
            name='dev2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev2_id', to='el_webI.Component_data'),
        ),
        migrations.AddField(
            model_name='board',
            name='dev3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev3_id', to='el_webI.Component_data'),
        ),
        migrations.AddField(
            model_name='board',
            name='dev4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev4_id', to='el_webI.Component_data'),
        ),
        migrations.AddField(
            model_name='board',
            name='dev5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev5_id', to='el_webI.Component_data'),
        ),
    ]