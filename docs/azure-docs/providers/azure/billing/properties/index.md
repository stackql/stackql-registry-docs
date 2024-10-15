---
title: properties
hide_title: false
hide_table_of_contents: false
keywords:
  - properties
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

Creates, updates, deletes, gets or lists a <code>properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>properties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.properties" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_properties', value: 'view', },
        { label: 'properties', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_admin_notification_email_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_agreement_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_sold_to_country" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_status_reason_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_sub_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_payment_method_family" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_payment_method_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_spending_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_spending_limit_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_status_reason_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cost_center" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_status_reason_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_account_admin" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_transitioned_billing_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_billing_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_billing_status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_billing_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_service_usage_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_workload_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A billing property. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the billing properties for a subscription |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="subscriptionId" /> | Updates the billing property of a subscription. Currently, cost center can be updated for billing accounts with agreement type Microsoft Customer Agreement and subscription service usage address can be updated for billing accounts with agreement type Microsoft Online Service Program. |

## `SELECT` examples

Gets the billing properties for a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_properties', value: 'view', },
        { label: 'properties', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_admin_notification_email_address,
billing_account_agreement_type,
billing_account_display_name,
billing_account_id,
billing_account_sold_to_country,
billing_account_status,
billing_account_status_reason_code,
billing_account_sub_type,
billing_account_type,
billing_currency,
billing_profile_display_name,
billing_profile_id,
billing_profile_payment_method_family,
billing_profile_payment_method_type,
billing_profile_spending_limit,
billing_profile_spending_limit_details,
billing_profile_status,
billing_profile_status_reason_code,
billing_tenant_id,
cost_center,
customer_display_name,
customer_id,
customer_status,
enrollment_details,
invoice_section_display_name,
invoice_section_id,
invoice_section_status,
invoice_section_status_reason_code,
is_account_admin,
is_transitioned_billing_account,
product_id,
product_name,
sku_description,
sku_id,
subscriptionId,
subscription_billing_status,
subscription_billing_status_details,
subscription_billing_type,
subscription_service_usage_address,
subscription_workload_type,
tags
FROM azure.billing.vw_properties
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.properties
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>properties</code> resource.

```sql
/*+ update */
UPDATE azure.billing.properties
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
subscriptionId = '{{ subscriptionId }}';
```
