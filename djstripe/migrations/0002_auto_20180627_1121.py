# Generated by Django 2.0.6 on 2018-06-27 08:21

import django.db.models.deletion
from django.db import migrations, models

import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="business_name",
            field=models.CharField(help_text="The publicly visible name of the business", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="support_url",
            field=models.CharField(help_text="A publicly shareable URL that provides support for this account", max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="card",
            name="customer",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="legacy_cards", to="djstripe.Customer"),
        ),
        migrations.AlterField(
            model_name="charge",
            name="receipt_number",
            field=models.CharField(help_text="The transaction number that appears on email receipts sent for this charge.", max_length=14, null=True),
        ),
        migrations.AddField(
            model_name="coupon",
            name="name",
            field=models.CharField(blank=True, help_text="Name of the coupon displayed to customers on for instance invoices or receipts.", max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="deactivate_on",
            field=djstripe.fields.JSONField(help_text="An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="images",
            field=djstripe.fields.JSONField(help_text="A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="source",
            name="type",
            field=djstripe.fields.StripeEnumField(enum=djstripe.enums.SourceType, help_text="The type of the source.", max_length=20),
        ),
        migrations.AddField(
            model_name="plan",
            name="active",
            field=models.BooleanField(default=True, help_text="Whether the plan is currently available for new subscriptions."),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="charge",
            name="fraudulent",
        ),
        migrations.RemoveField(
            model_name="charge",
            name="receipt_sent",
        ),
        migrations.RemoveField(
            model_name="charge",
            name="source_stripe_id",
        ),
        migrations.RemoveField(
            model_name="charge",
            name="source_type",
        ),
        migrations.RemoveField(
            model_name="charge",
            name="fee",
        ),
        migrations.RemoveField(
            model_name="charge",
            name="fee_details",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="date",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="destination_type",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="failure_code",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="failure_message",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="fee",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="fee_details",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="statement_descriptor",
        ),
        migrations.RemoveField(
            model_name="transfer",
            name="status",
        ),
        migrations.AlterModelOptions(
            name="account",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="bankaccount",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="card",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="charge",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="dispute",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="event",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="fileupload",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="invoiceitem",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="payout",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="refund",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="source",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="transfer",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="upcominginvoice",
            options={"get_latest_by": "created"},
        ),
        migrations.CreateModel(
            name="BalanceTransaction",
            fields=[
                ("djstripe_id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                ("livemode", models.NullBooleanField(default=None, help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.")),
                ("created", djstripe.fields.StripeDateTimeField(blank=True, help_text="The datetime this object was created in stripe.", null=True)),
                ("metadata", djstripe.fields.JSONField(blank=True, help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.", null=True)),
                ("description", models.TextField(blank=True, help_text="A description of this object.", null=True)),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                ("amount", djstripe.fields.StripeQuantumCurrencyAmountField(help_text="Gross amount of the transaction, in cents.")),
                ("available_on", djstripe.fields.StripeDateTimeField(help_text="The date the transaction's net funds will become available in the Stripe balance.")),
                ("currency", djstripe.fields.StripeCurrencyCodeField(help_text="Three-letter ISO currency code", max_length=3)),
                ("exchange_rate", models.DecimalField(null=True, decimal_places=6, max_digits=8)),
                ("fee", djstripe.fields.StripeQuantumCurrencyAmountField(help_text="Fee (in cents) paid for this transaction.")),
                ("fee_details", djstripe.fields.JSONField()),
                ("net", djstripe.fields.StripeQuantumCurrencyAmountField(help_text="Net amount of the transaction, in cents.")),
                ("status", djstripe.fields.StripeEnumField(enum=djstripe.enums.BalanceTransactionStatus, max_length=9)),
                ("type", djstripe.fields.StripeEnumField(enum=djstripe.enums.BalanceTransactionType, max_length=22)),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SubscriptionItem",
            fields=[
                ("djstripe_id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                ("livemode", models.NullBooleanField(default=None, help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.")),
                ("created", djstripe.fields.StripeDateTimeField(blank=True, help_text="The datetime this object was created in stripe.", null=True)),
                ("metadata", djstripe.fields.JSONField(blank=True, help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.", null=True)),
                ("description", models.TextField(blank=True, help_text="A description of this object.", null=True)),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                ("quantity", models.PositiveIntegerField(help_text="The quantity of the plan to which the customer should be subscribed.")),
                ("plan", models.ForeignKey(help_text="The plan the customer is subscribed to.", on_delete=django.db.models.deletion.CASCADE, related_name="subscription_items", to="djstripe.Plan")),
                ("subscription", models.ForeignKey(help_text="The subscription this subscription item belongs to.", on_delete=django.db.models.deletion.CASCADE, related_name="items", to="djstripe.Subscription")),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UsageRecord",
            fields=[
                ("djstripe_id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                ("livemode", models.NullBooleanField(default=None, help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.")),
                ("created", djstripe.fields.StripeDateTimeField(blank=True, help_text="The datetime this object was created in stripe.", null=True)),
                ("metadata", djstripe.fields.JSONField(blank=True, help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.", null=True)),
                ("description", models.TextField(blank=True, help_text="A description of this object.", null=True)),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                ("quantity", models.PositiveIntegerField(help_text="The quantity of the plan to which the customer should be subscribed.")),
                ("subscription_item", models.ForeignKey(help_text="The subscription item this usage record contains data for.", on_delete=django.db.models.deletion.CASCADE, related_name="usage_records", to="djstripe.SubscriptionItem")),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="charge",
            name="balance_transaction",
            field=models.ForeignKey(help_text="The balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).", null=True, on_delete=django.db.models.deletion.SET_NULL, to="djstripe.BalanceTransaction"),
        ),
        migrations.AddField(
            model_name="payout",
            name="balance_transaction",
            field=models.ForeignKey(help_text="Balance transaction that describes the impact on your account balance.", null=True, on_delete=django.db.models.deletion.SET_NULL, to="djstripe.BalanceTransaction"),
        ),
        migrations.AddField(
            model_name="payout",
            name="failure_balance_transaction",
            field=models.ForeignKey(help_text="If the payout failed or was canceled, this will be the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance.", null=True, on_delete=django.db.models.deletion.SET_NULL, to="djstripe.BalanceTransaction"),
        ),
        migrations.AddField(
            model_name="refund",
            name="balance_transaction",
            field=models.ForeignKey(help_text="Balance transaction that describes the impact on your account balance.", null=True, on_delete=django.db.models.deletion.SET_NULL, to="djstripe.BalanceTransaction"),
        ),
        migrations.AddField(
            model_name="refund",
            name="failure_balance_transaction",
            field=models.ForeignKey(help_text="If the refund failed, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction.", null=True, on_delete=django.db.models.deletion.SET_NULL, to="djstripe.BalanceTransaction"),
        ),
        migrations.AddField(
            model_name="transfer",
            name="balance_transaction",
            field=models.ForeignKey(blank=True, help_text="Balance transaction that describes the impact on your account balance.", null=True, on_delete=django.db.models.deletion.SET_NULL, to="djstripe.BalanceTransaction"),
        ),
        migrations.RenameField(
            model_name="account",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="bankaccount",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="card",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="charge",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="customer",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="dispute",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="event",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="fileupload",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="invoice",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="invoiceitem",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="payout",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="plan",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="refund",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="source",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="subscription",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="transfer",
            old_name="stripe_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="coupon",
            old_name="stripe_id",
            new_name="id",
        ),
    ]
