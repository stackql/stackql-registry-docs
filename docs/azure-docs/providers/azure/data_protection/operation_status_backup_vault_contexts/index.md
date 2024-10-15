---
title: operation_status_backup_vault_contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status_backup_vault_contexts
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>operation_status_backup_vault_contexts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_status_backup_vault_contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.operation_status_backup_vault_contexts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operation_status_backup_vault_contexts', value: 'view', },
        { label: 'operation_status_backup_vault_contexts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | It should match what is used to GET the operation result |
| <CopyableCode code="name" /> | `text` | It must match the last segment of the "id" field, and will typically be a GUID / system generated value |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | The resource management error response. |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | It should match what is used to GET the operation result |
| <CopyableCode code="name" /> | `string` | It must match the last segment of the "id" field, and will typically be a GUID / system generated value |
| <CopyableCode code="endTime" /> | `string` | End time of the operation |
| <CopyableCode code="error" /> | `object` | The resource management error response. |
| <CopyableCode code="properties" /> | `object` | Operation Extended Info |
| <CopyableCode code="startTime" /> | `string` | Start time of the operation |
| <CopyableCode code="status" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operation_status_backup_vault_contexts', value: 'view', },
        { label: 'operation_status_backup_vault_contexts', value: 'resource', },
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
FROM azure.data_protection.vw_operation_status_backup_vault_contexts
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
FROM azure.data_protection.operation_status_backup_vault_contexts
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

