---
title: replication_protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protected_items
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_protected_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protected_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protected_items', value: 'view', },
        { label: 'replication_protected_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="active_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_scenario" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_recovery_point_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_test_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="policy_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_fabric_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_protection_container_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectable_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_item_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_protection_container_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_services_provider_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicatedProtectedItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="switch_provider_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="switch_provider_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_failover_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_failover_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Replication protected item custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR replication protected item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected items in the vault. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected items in the protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an ASR replication protected item (Enable replication). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to disable replication on a replication protected item. This will also remove the item. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update the recovery settings of an ASR replication protected item. |
| <CopyableCode code="add_disks" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to add disks(s) to the replication protected item. |
| <CopyableCode code="apply_recovery_point" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to change the recovery point of a failed over replication protected item. |
| <CopyableCode code="failover_cancel" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to cancel the failover of the replication protected item. |
| <CopyableCode code="failover_commit" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to commit the failover of the replication protected item. |
| <CopyableCode code="planned_failover" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to initiate a planned failover of the replication protected item. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item. |
| <CopyableCode code="remove_disks" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to remove disk(s) from the replication protected item. |
| <CopyableCode code="repair_replication" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization. |
| <CopyableCode code="reprotect" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to reprotect or reverse replicate a failed over replication protected item. |
| <CopyableCode code="resolve_health_errors" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to resolve health issues of the replication protected item. |
| <CopyableCode code="switch_provider" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to initiate a switch provider of the replication protected item. |
| <CopyableCode code="test_failover" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to perform a test failover of the replication protected item. |
| <CopyableCode code="test_failover_cleanup" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to clean up the test failover of a replication protected item. |
| <CopyableCode code="unplanned_failover" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to initiate a failover of the replication protected item. |

## `SELECT` examples

Gets the list of ASR replication protected items in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protected_items', value: 'view', },
        { label: 'replication_protected_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
active_location,
allowed_operations,
current_scenario,
event_correlation_id,
fabricName,
failover_health,
failover_recovery_point_id,
friendly_name,
health_errors,
last_successful_failover_time,
last_successful_test_failover_time,
location,
policy_friendly_name,
policy_id,
primary_fabric_friendly_name,
primary_fabric_provider,
primary_protection_container_friendly_name,
protectable_item_id,
protected_item_type,
protectionContainerName,
protection_state,
protection_state_description,
provider_specific_details,
recovery_container_id,
recovery_fabric_friendly_name,
recovery_fabric_id,
recovery_protection_container_friendly_name,
recovery_services_provider_id,
replicatedProtectedItemName,
replication_health,
resourceGroupName,
resourceName,
subscriptionId,
switch_provider_state,
switch_provider_state_description,
test_failover_state,
test_failover_state_description,
type
FROM azure.recovery_services_site_recovery.vw_replication_protected_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.recovery_services_site_recovery.replication_protected_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_protected_items</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_protected_items (
fabricName,
protectionContainerName,
replicatedProtectedItemName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ fabricName }}',
'{{ protectionContainerName }}',
'{{ replicatedProtectedItemName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: policyId
          value: string
        - name: protectableItemId
          value: string
        - name: providerSpecificDetails
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_protected_items</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replication_protected_items
SET 
properties = '{{ properties }}'
WHERE 
fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicatedProtectedItemName = '{{ replicatedProtectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_protected_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_protected_items
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicatedProtectedItemName = '{{ replicatedProtectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```
