# Generated by Django 4.1.3 on 2022-12-05 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_alter_budget_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='budget.budget'),
        ),
    ]