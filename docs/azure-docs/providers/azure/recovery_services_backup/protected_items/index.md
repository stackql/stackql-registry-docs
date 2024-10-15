---
title: protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items
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

Creates, updates, deletes, gets or lists a <code>protected_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protected_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protected_items', value: 'view', },
        { label: 'protected_items', value: 'resource', },
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,
call the GetItemOperationResult API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an
asynchronous operation. To know the status of the operation, call the GetItemOperationResult API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the
request, call the GetItemOperationResult API. |

## `SELECT` examples

Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,
call the GetItemOperationResult API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protected_items', value: 'view', },
        { label: 'protected_items', value: 'resource', },
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
FROM azure.recovery_services_backup.vw_protected_items
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
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
FROM azure.recovery_services_backup.protected_items
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND protectedItemName = '{{ protectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>protected_items</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.recovery_services_backup.protected_items (
containerName,
fabricName,
protectedItemName,
resourceGroupName,
subscriptionId,
vaultName,
properties
)
SELECT 
'{{ containerName }}',
'{{ fabricName }}',
'{{ protectedItemName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: protectedItemType
          value: string
        - name: backupManagementType
          value: string
        - name: workloadType
          value: string
        - name: containerName
          value: string
        - name: sourceResourceId
          value: string
        - name: policyId
          value: string
        - name: lastRecoveryPoint
          value: string
        - name: backupSetName
          value: string
        - name: createMode
          value: string
        - name: deferredDeleteTimeInUTC
          value: string
        - name: isScheduledForDeferredDelete
          value: boolean
        - name: deferredDeleteTimeRemaining
          value: string
        - name: isDeferredDeleteScheduleUpcoming
          value: boolean
        - name: isRehydrate
          value: boolean
        - name: resourceGuardOperationRequests
          value:
            - string
        - name: isArchiveEnabled
          value: boolean
        - name: policyName
          value: string
        - name: softDeleteRetentionPeriodInDays
          value: integer
        - name: vaultId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>protected_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_backup.protected_items
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND protectedItemName = '{{ protectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
