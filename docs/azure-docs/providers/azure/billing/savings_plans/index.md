---
title: savings_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plans
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

Creates, updates, deletes, gets or lists a <code>savings_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>savings_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.savings_plans" /></td></tr>
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
| <CopyableCode code="applied_scope_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="benefit_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="product_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="savingsPlanId" /> | `text` | field from the `properties` object |
| <CopyableCode code="savingsPlanOrderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `object` | The SKU to be applied for this resource |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_friendly_applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="utilization" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Savings plan properties |
| <CopyableCode code="sku" /> | `object` | The SKU to be applied for this resource |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, savingsPlanId, savingsPlanOrderId" /> | Get savings plan by billing account. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | List savings plans by billing account. |
| <CopyableCode code="list_by_savings_plan_order" /> | `SELECT` | <CopyableCode code="billingAccountName, savingsPlanOrderId" /> | List savings plans in an order by billing account. |
| <CopyableCode code="update_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, savingsPlanId, savingsPlanOrderId" /> | Update savings plan by billing account. |
| <CopyableCode code="validate_update_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, savingsPlanId, savingsPlanOrderId" /> | Validate savings plan patch by billing account. |

## `SELECT` examples

List savings plans by billing account.

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
applied_scope_properties,
applied_scope_type,
benefit_start_time,
billingAccountName,
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
product_code,
provisioning_state,
purchase_date_time,
renew,
renew_destination,
renew_properties,
renew_source,
savingsPlanId,
savingsPlanOrderId,
sku,
tags,
term,
user_friendly_applied_scope_type,
utilization
FROM azure.billing.vw_savings_plans
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku,
tags
FROM azure.billing.savings_plans
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

