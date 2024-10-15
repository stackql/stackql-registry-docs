---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - billing
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscriptions', value: 'view', },
        { label: 'subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="beneficiary" /> | `text` | field from the `properties` object |
| <CopyableCode code="beneficiary_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingSubscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumption_cost_center" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_account_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_account_subscription_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_month_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="month_to_date_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_billing_cycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="renewal_term_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="reseller" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="suspension_reason_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="suspension_reasons" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_overrides" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="term_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="term_end_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="term_start_date" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The billing properties of a subscription. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Gets a subscription by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement,  Microsoft Partner Agreement, and Enterprise Agreement. |
| <CopyableCode code="get_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, billingSubscriptionName" /> | Gets a subscription by its billing profile and ID. The operation is supported for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the subscriptions for a billing account. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the subscriptions that are billed to a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Lists the subscriptions for a customer. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="list_by_customer_at_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, customerName" /> | Lists the subscriptions for a customer at billing account level. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="list_by_enrollment_account" /> | `SELECT` | <CopyableCode code="billingAccountName, enrollmentAccountName" /> | Lists the subscriptions for an enrollment account. The operation is supported for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Cancels a billing subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Updates the properties of a billing subscription. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="billingAccountName, billingSubscriptionName, data__cancellationReason" /> | Cancels a usage-based subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement. |
| <CopyableCode code="merge" /> | `EXEC` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Merges the billing subscription provided in the request with a target billing subscription. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Moves charges for a subscription to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="split" /> | `EXEC` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Splits a subscription into a new subscription with quantity less than current subscription quantity and not equal to 0. |
| <CopyableCode code="validate_move_eligibility" /> | `EXEC` | <CopyableCode code="billingAccountName, billingSubscriptionName" /> | Validates if charges for a subscription can be moved to a new invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the subscriptions for a billing account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscriptions', value: 'view', },
        { label: 'subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_renew,
beneficiary,
beneficiary_tenant_id,
billingAccountName,
billingProfileName,
billingSubscriptionName,
billing_frequency,
billing_policies,
billing_profile_display_name,
billing_profile_id,
billing_profile_name,
consumption_cost_center,
customer_display_name,
customer_id,
customer_name,
display_name,
enrollment_account_display_name,
enrollment_account_id,
enrollment_account_subscription_details,
invoice_section_display_name,
invoice_section_id,
invoice_section_name,
last_month_charges,
month_to_date_charges,
next_billing_cycle_details,
offer_id,
operation_status,
product_category,
product_type,
product_type_id,
provisioning_state,
provisioning_tenant_id,
purchase_date,
quantity,
renewal_term_details,
reseller,
resource_uri,
sku_description,
sku_id,
status,
subscription_id,
suspension_reason_details,
suspension_reasons,
system_overrides,
tags,
term_duration,
term_end_date,
term_start_date
FROM azure.billing.vw_subscriptions
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.subscriptions
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure.billing.subscriptions
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
billingAccountName = '{{ billingAccountName }}'
AND billingSubscriptionName = '{{ billingSubscriptionName }}';
```

## `DELETE` example

Deletes the specified <code>subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.subscriptions
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingSubscriptionName = '{{ billingSubscriptionName }}';
```
