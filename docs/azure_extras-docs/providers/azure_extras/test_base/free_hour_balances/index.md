---
title: free_hour_balances
hide_title: false
hide_table_of_contents: false
keywords:
  - free_hour_balances
  - test_base
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

Creates, updates, deletes, gets or lists a <code>free_hour_balances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>free_hour_balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.free_hour_balances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_free_hour_balances', value: 'view', },
        { label: 'free_hour_balances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="freeHourBalanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="increment_entries" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_remaining_free_hours" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="freeHourBalanceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Return the Test Base free hour balance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Return the Test Base free hour balances list. |

## `SELECT` examples

Return the Test Base free hour balances list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_free_hour_balances', value: 'view', },
        { label: 'free_hour_balances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
freeHourBalanceName,
increment_entries,
resourceGroupName,
subscriptionId,
testBaseAccountName,
total_remaining_free_hours
FROM azure_extras.test_base.vw_free_hour_balances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.free_hour_balances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

