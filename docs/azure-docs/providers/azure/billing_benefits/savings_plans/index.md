---
title: savings_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plans
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

Creates, updates, deletes, gets or lists a <code>savings_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>savings_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.savings_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_savings_plans', value: 'view', },
        { label: 'savings_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="applied_scope_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_scope_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitment" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="effective_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_status_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="savingsPlanId" /> | `text` | field from the `properties` object |
| <CopyableCode code="savingsPlanOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="user_friendly_applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="utilization" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Savings plan properties |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="savingsPlanId, savingsPlanOrderId" /> | Get savings plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="savingsPlanOrderId" /> | List savings plans in an order. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="" /> | List savings plans. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="savingsPlanId, savingsPlanOrderId" /> | Update savings plan. |
| <CopyableCode code="validate_update" /> | `EXEC` | <CopyableCode code="savingsPlanId, savingsPlanOrderId" /> | Validate savings plan patch. |

## `SELECT` examples

List savings plans.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_savings_plans', value: 'view', },
        { label: 'savings_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applied_scope_properties,
applied_scope_type,
benefit_start_time,
billing_account_id,
billing_plan,
billing_profile_id,
billing_scope_id,
commitment,
customer_id,
display_name,
display_provisioning_state,
effective_date_time,
expiry_date_time,
extended_status_info,
provisioning_state,
purchase_date_time,
renew,
renew_destination,
renew_properties,
renew_source,
savingsPlanId,
savingsPlanOrderId,
sku,
system_data,
term,
type,
user_friendly_applied_scope_type,
utilization
FROM azure.billing_benefits.vw_savings_plans
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
FROM azure.billing_benefits.savings_plans
;
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>savings_plans</code> resource.

```sql
/*+ update */
UPDATE azure.billing_benefits.savings_plans
SET 
properties = '{{ properties }}'
WHERE 
savingsPlanId = '{{ savingsPlanId }}'
AND savingsPlanOrderId = '{{ savingsPlanOrderId }}';
```
