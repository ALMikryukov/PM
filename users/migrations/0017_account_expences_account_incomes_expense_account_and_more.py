# Generated by Django 4.2.1 on 2023-05-13 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_account_expences_remove_account_incomes'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='expences',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acount_4', to='users.expense'),
        ),
        migrations.AddField(
            model_name='account',
            name='incomes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acount_3', to='users.income'),
        ),
        migrations.AddField(
            model_name='expense',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acount_2', to='users.account'),
        ),
        migrations.AddField(
            model_name='income',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acount_1', to='users.account'),
        ),
    ]