---
title: protected_item_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_item_operation_results
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

Creates, updates, deletes, gets or lists a <code>protected_item_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protected_item_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protected_item_operation_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protected_item_operation_results', value: 'view', },
        { label: 'protected_item_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="backup_management_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_set_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="containerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="deferred_delete_time_in_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="deferred_delete_time_remaining" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archive_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deferred_delete_schedule_upcoming" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_rehydrate" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_scheduled_for_deferred_delete" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_recovery_point" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectedItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_item_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="soft_delete_retention_period_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vault_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Base class for backup items. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerName, fabricName, operationId, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Fetches the result of any operation on the backup item. |

## `SELECT` examples

Fetches the result of any operation on the backup item.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protected_item_operation_results', value: 'view', },
        { label: 'protected_item_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_management_type,
backup_set_name,
containerName,
container_name,
create_mode,
deferred_delete_time_in_utc,
deferred_delete_time_remaining,
fabricName,
is_archive_enabled,
is_deferred_delete_schedule_upcoming,
is_rehydrate,
is_scheduled_for_deferred_delete,
last_recovery_point,
operationId,
policy_id,
policy_name,
protectedItemName,
protected_item_type,
resourceGroupName,
resource_guard_operation_requests,
soft_delete_retention_period_in_days,
source_resource_id,
subscriptionId,
type,
vaultName,
vault_id,
workload_type
FROM azure.recovery_services_backup.vw_protected_item_operation_results
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND operationId = '{{ operationId }}'
AND protectedItemName = '{{ protectedItemName }}'
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
properties,
type
FROM azure.recovery_services_backup.protected_item_operation_results
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND operationId = '{{ operationId }}'
AND protectedItemName = '{{ protectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

