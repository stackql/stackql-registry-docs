---
title: replication_protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protected_items
  - recovery_services_site_recovery
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_protected_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Replication protected item custom data details. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Gets the details of an ASR replication protected item. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protected items in the vault. |
| `list_by_replication_protection_containers` | `SELECT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protected items in the protection container. |
| `create` | `INSERT` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to create an ASR replication protected item (Enable replication). |
| `delete` | `DELETE` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to disable replication on a replication protected item. This will also remove the item. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protected items in the vault. |
| `_list_by_replication_protection_containers` | `EXEC` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protected items in the protection container. |
| `add_disks` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to add disks(s) to the replication protected item. |
| `apply_recovery_point` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to change the recovery point of a failed over replication protected item. |
| `failover_cancel` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to cancel the failover of the replication protected item. |
| `failover_commit` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to commit the failover of the replication protected item. |
| `planned_failover` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to initiate a planned failover of the replication protected item. |
| `purge` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item. |
| `remove_disks` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to remove disk(s) from the replication protected item. |
| `repair_replication` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization. |
| `reprotect` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to reprotect or reverse replicate a failed over replication protected item. |
| `resolve_health_errors` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to resolve health issues of the replication protected item. |
| `switch_provider` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to initiate a switch provider of the replication protected item. |
| `test_failover` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | Operation to perform a test failover of the replication protected item. |
| `test_failover_cleanup` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | Operation to clean up the test failover of a replication protected item. |
| `unplanned_failover` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | Operation to initiate a failover of the replication protected item. |
| `update` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to update the recovery settings of an ASR replication protected item. |
