---
title: balances_for_billing_period_by_billing_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - balances_for_billing_period_by_billing_accounts
  - consumption
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

Creates, updates, deletes, gets or lists a <code>balances_for_billing_period_by_billing_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>balances_for_billing_period_by_billing_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.balances_for_billing_period_by_billing_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_balances_for_billing_period_by_billing_accounts', value: 'view', },
        { label: 'balances_for_billing_period_by_billing_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `text` | The ID that uniquely identifies an event.  |
| <CopyableCode code="adjustment_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="adjustments" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_marketplace_service_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="beginning_balance" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountId" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingPeriodName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="charges_billed_separately" /> | `text` | field from the `properties` object |
| <CopyableCode code="currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="ending_balance" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag for the resource. |
| <CopyableCode code="new_purchases" /> | `text` | field from the `properties` object |
| <CopyableCode code="new_purchases_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="overage_refund" /> | `text` | field from the `properties` object |
| <CopyableCode code="price_hidden" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_overage" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="total_overage" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="utilized" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The full qualified ARM ID of an event. |
| <CopyableCode code="name" /> | `string` | The ID that uniquely identifies an event.  |
| <CopyableCode code="etag" /> | `string` | The etag for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the balance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountId, billingPeriodName" /> | Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later. |

## `SELECT` examples

Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_balances_for_billing_period_by_billing_accounts', value: 'view', },
        { label: 'balances_for_billing_period_by_billing_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
adjustment_details,
adjustments,
azure_marketplace_service_charges,
beginning_balance,
billingAccountId,
billingPeriodName,
billing_frequency,
charges_billed_separately,
currency,
ending_balance,
etag,
new_purchases,
new_purchases_details,
overage_refund,
price_hidden,
service_overage,
tags,
total_overage,
total_usage,
type,
utilized
FROM azure.consumption.vw_balances_for_billing_period_by_billing_accounts
WHERE billingAccountId = '{{ billingAccountId }}'
AND billingPeriodName = '{{ billingPeriodName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
tags,
type
FROM azure.consumption.balances_for_billing_period_by_billing_accounts
WHERE billingAccountId = '{{ billingAccountId }}'
AND billingPeriodName = '{{ billingPeriodName }}';
```
</TabItem></Tabs>

