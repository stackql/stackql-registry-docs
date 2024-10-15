---
title: asc_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - asc_operations
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>asc_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asc_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.asc_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_asc_operations', value: 'view', },
        { label: 'asc_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The operation Id. |
| <CopyableCode code="name" /> | `text` | The operation name. |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | Describes the format of Error response. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="output" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | The status of the operation. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation Id. |
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | Describes the format of Error response. |
| <CopyableCode code="properties" /> | `object` | Additional operation-specific output. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | The status of the operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> | Gets the status of an asynchronous operation for the Azure HPC Cache |

## `SELECT` examples

Gets the status of an asynchronous operation for the Azure HPC Cache

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_asc_operations', value: 'view', },
        { label: 'asc_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
end_time,
error,
location,
operationId,
output,
start_time,
status,
subscriptionId
FROM azure.storage_cache.vw_asc_operations
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
endTime,
error,
properties,
startTime,
status
FROM azure.storage_cache.asc_operations
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

