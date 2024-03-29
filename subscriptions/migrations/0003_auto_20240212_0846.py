# Generated by Django 3.2 on 2024-02-12 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0002_auto_20240203_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_desc',
            field=models.CharField(blank=True, default='Access to basic gym facilities Personalized workout plans £14.99/month', max_length=300),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_price',
            field=models.FloatField(default=14.99),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_title',
            field=models.CharField(blank=True, default='Basic Subscription', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_type',
            field=models.CharField(blank=True, default='BA', max_length=10),
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscriptions.subscription')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
