---
title: smart_groups_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - smart_groups_histories
  - alerts_management
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

Creates, updates, deletes, gets or lists a <code>smart_groups_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>smart_groups_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.smart_groups_histories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_smart_groups_histories', value: 'view', },
        { label: 'smart_groups_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="modifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="smartGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="smart_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties of the smartGroup modification item. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="smartGroupId, subscriptionId" /> | Get the history a smart group, which captures any Smart Group state changes (New/Acknowledged/Closed) . |

## `SELECT` examples

Get the history a smart group, which captures any Smart Group state changes (New/Acknowledged/Closed) .

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_smart_groups_histories', value: 'view', },
        { label: 'smart_groups_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
modifications,
next_link,
smartGroupId,
smart_group_id,
subscriptionId,
type
FROM azure.alerts_management.vw_smart_groups_histories
WHERE smartGroupId = '{{ smartGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.alerts_management.smart_groups_histories
WHERE smartGroupId = '{{ smartGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

