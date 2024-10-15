---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - terraform
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

Creates, updates, deletes, gets or lists a <code>operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.terraform.operation_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operation_status', value: 'view', },
        { label: 'operation_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The operation status resource id. |
| <CopyableCode code="name" /> | `text` | The operation name. |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | The error detail. |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="skipped_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | The status of the operation. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation status resource id. |
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="percentComplete" /> | `number` | The progress percentage of the operation, ranges from 0 to 100 |
| <CopyableCode code="properties" /> | `object` | The Terraform export result |
| <CopyableCode code="resourceId" /> | `string` | The fully qualified resource id of the resource for which the operation was performed. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | The status of the operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, subscriptionId" /> | Get the status of a long running azure asynchronous operation. |

## `SELECT` examples

Get the status of a long running azure asynchronous operation.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operation_status', value: 'view', },
        { label: 'operation_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configuration,
end_time,
error,
errors,
operationId,
percent_complete,
resource_id,
skipped_resources,
start_time,
status,
subscriptionId
FROM azure.terraform.vw_operation_status
WHERE operationId = '{{ operationId }}'
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
percentComplete,
properties,
resourceId,
startTime,
status
FROM azure.terraform.operation_status
WHERE operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

