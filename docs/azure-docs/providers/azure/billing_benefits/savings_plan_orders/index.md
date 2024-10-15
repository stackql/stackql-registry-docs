---
title: savings_plan_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plan_orders
  - billing_benefits
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.savings_plan_orders" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_scope_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_status_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="savingsPlanOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="savings_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Savings plan order properties |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="savingsPlanOrderId" /> | Get a savings plan order. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List all Savings plan orders. |
| <CopyableCode code="elevate" /> | `EXEC` | <CopyableCode code="savingsPlanOrderId" /> | Elevate as owner on savings plan order based on billing permissions. |

## `SELECT` examples

List all Savings plan orders.

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
id,
name,
benefit_start_time,
billing_account_id,
billing_plan,
billing_profile_id,
billing_scope_id,
customer_id,
display_name,
expiry_date_time,
extended_status_info,
plan_information,
provisioning_state,
savingsPlanOrderId,
savings_plans,
sku,
system_data,
term,
type
FROM azure.billing_benefits.vw_savings_plan_orders
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
sku,
systemData,
type
FROM azure.billing_benefits.savings_plan_orders
;
```
</TabItem></Tabs>

