---
title: tiering_cost_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - tiering_cost_operation_status
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>tiering_cost_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tiering_cost_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.tiering_cost_operation_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tiering_cost_operation_status', value: 'view', },
        { label: 'tiering_cost_operation_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the operation. |
| <CopyableCode code="name" /> | `text` | Name of the operation. |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | Error information associated with operation status call. |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | Operation status. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the operation. |
| <CopyableCode code="name" /> | `string` | Name of the operation. |
| <CopyableCode code="endTime" /> | `string` | Operation end time. Format: ISO-8601. |
| <CopyableCode code="error" /> | `object` | Error information associated with operation status call. |
| <CopyableCode code="properties" /> | `object` | Base class for additional information of operation status. |
| <CopyableCode code="startTime" /> | `string` | Operation start time. Format: ISO-8601. |
| <CopyableCode code="status" /> | `string` | Operation status. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> | Gets the status of async operations of tiering cost |

## `SELECT` examples

Gets the status of async operations of tiering cost

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tiering_cost_operation_status', value: 'view', },
        { label: 'tiering_cost_operation_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
end_time,
error,
object_type,
operationId,
resourceGroupName,
start_time,
status,
subscriptionId,
vaultName
FROM azure.recovery_services_backup.vw_tiering_cost_operation_status
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
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
FROM azure.recovery_services_backup.tiering_cost_operation_status
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

