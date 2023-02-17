# Generated by Django 4.1.7 on 2023-02-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_new',
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('New toy order', 'New'), ('Toy from shop', 'Exist')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='preferable_messenger',
            field=models.CharField(choices=[('whatsapp', 'WhatsApp'), ('telegram', 'Telegram'), ('Email', 'e-mail')], default='em', max_length=10),
        ),
    ]
