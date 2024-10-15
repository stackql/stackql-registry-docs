---
title: savings_plan_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plan_orders
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

Creates, updates, deletes, gets or lists a <code>savings_plan_orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>savings_plan_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.savings_plan_orders" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_savings_plan_orders', value: 'view', },
        { label: 'savings_plan_orders', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_scope_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_status_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="savingsPlanOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="savings_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU to be applied for this resource |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Savings plan order properties |
| <CopyableCode code="sku" /> | `object` | The SKU to be applied for this resource |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, savingsPlanOrderId" /> | Get a savings plan order by billing account. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | List all Savings plan orders by billing account. |

## `SELECT` examples

List all Savings plan orders by billing account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_savings_plan_orders', value: 'view', },
        { label: 'savings_plan_orders', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
benefit_start_time,
billingAccountName,
billing_account_id,
billing_plan,
billing_profile_id,
billing_scope_id,
customer_id,
display_name,
expiry_date_time,
extended_status_info,
plan_information,
product_code,
provisioning_state,
savingsPlanOrderId,
savings_plans,
sku,
tags,
term
FROM azure.billing.vw_savings_plan_orders
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku,
tags
FROM azure.billing.savings_plan_orders
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

