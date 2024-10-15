---
title: operations_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_results
  - orbital
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

Creates, updates, deletes, gets or lists a <code>operations_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.operations_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operations_results', value: 'view', },
        { label: 'operations_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | Operation result error properties. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | The status of operation. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | A list of results when the operation returns multiple results. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="endTime" /> | `string` | The operation end time (ISO 8601 UTC standard). |
| <CopyableCode code="error" /> | `object` | Operation result error properties. |
| <CopyableCode code="nextLink" /> | `string` | The URL to get the next set of results. |
| <CopyableCode code="percentComplete" /> | `number` | Percentage completed. |
| <CopyableCode code="properties" /> | `object` | Operation result properties. |
| <CopyableCode code="startTime" /> | `string` | The operation start time (ISO 8601 UTC standard). |
| <CopyableCode code="status" /> | `string` | The status of operation. |
| <CopyableCode code="value" /> | `array` | A list of results when the operation returns multiple results. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> | Returns operation results. |

## `SELECT` examples

Returns operation results.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operations_results', value: 'view', },
        { label: 'operations_results', value: 'resource', },
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
next_link,
operationId,
percent_complete,
start_time,
status,
subscriptionId,
value
FROM azure.orbital.vw_operations_results
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
nextLink,
percentComplete,
properties,
startTime,
status,
value
FROM azure.orbital.operations_results
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

