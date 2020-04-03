# Generated by Django 3.0.4 on 2020-04-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_auto_20181112_1420"),
    ]

    operations = [
        migrations.RenameField(
            model_name="custompayment", old_name="paid_on", new_name="last_payment_on",
        ),
        migrations.RemoveField(model_name="custompayment", name="amount",),
        migrations.AddField(
            model_name="custompayment",
            name="amount_locked",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=20, verbose_name="amount paid"
            ),
        ),
        migrations.AddField(
            model_name="custompayment",
            name="amount_required",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Amount in selected currency, normal notation",
                max_digits=20,
                verbose_name="amount required",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="custompayment",
            name="amount_paid",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=20, verbose_name="amount paid"
            ),
        ),
        migrations.AlterField(
            model_name="custompayment",
            name="backend",
            field=models.CharField(
                db_index=True, max_length=100, verbose_name="backend"
            ),
        ),
    ]
