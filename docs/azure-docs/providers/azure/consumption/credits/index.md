---
title: credits
hide_title: false
hide_table_of_contents: false
keywords:
  - credits
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

Creates, updates, deletes, gets or lists a <code>credits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.credits" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credits', value: 'view', },
        { label: 'credits', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="balance_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountId" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileId" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="credit_currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="expired_credit" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_estimated_balance" /> | `text` | field from the `properties` object |
| <CopyableCode code="pending_credit_adjustments" /> | `text` | field from the `properties` object |
| <CopyableCode code="pending_eligible_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="reseller" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | The properties of the credit summary. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountId, billingProfileId" /> | The credit summary by billingAccountId and billingProfileId. |

## `SELECT` examples

The credit summary by billingAccountId and billingProfileId.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credits', value: 'view', },
        { label: 'credits', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
balance_summary,
billingAccountId,
billingProfileId,
billing_currency,
credit_currency,
e_tag,
expired_credit,
is_estimated_balance,
pending_credit_adjustments,
pending_eligible_charges,
reseller,
type
FROM azure.consumption.vw_credits
WHERE billingAccountId = '{{ billingAccountId }}'
AND billingProfileId = '{{ billingProfileId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
properties,
type
FROM azure.consumption.credits
WHERE billingAccountId = '{{ billingAccountId }}'
AND billingProfileId = '{{ billingProfileId }}';
```
</TabItem></Tabs>

