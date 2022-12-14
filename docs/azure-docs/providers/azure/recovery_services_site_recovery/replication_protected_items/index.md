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
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
| `properties` | `object` | Replication protected item custom data details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationProtectedItems_Get` | `SELECT` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Gets the details of an ASR replication protected item. |
| `ReplicationProtectedItems_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protected items in the vault. |
| `ReplicationProtectedItems_ListByReplicationProtectionContainers` | `SELECT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR replication protected items in the protection container. |
| `ReplicationProtectedItems_Create` | `INSERT` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to create an ASR replication protected item (Enable replication). |
| `ReplicationProtectedItems_Delete` | `DELETE` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to disable replication on a replication protected item. This will also remove the item. |
| `ReplicationProtectedItems_AddDisks` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to add disks(s) to the replication protected item. |
| `ReplicationProtectedItems_ApplyRecoveryPoint` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to change the recovery point of a failed over replication protected item. |
| `ReplicationProtectedItems_FailoverCancel` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to cancel the failover of the replication protected item. |
| `ReplicationProtectedItems_FailoverCommit` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to commit the failover of the replication protected item. |
| `ReplicationProtectedItems_PlannedFailover` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to initiate a planned failover of the replication protected item. |
| `ReplicationProtectedItems_Purge` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item. |
| `ReplicationProtectedItems_RemoveDisks` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to remove disk(s) from the replication protected item. |
| `ReplicationProtectedItems_RepairReplication` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization. |
| `ReplicationProtectedItems_Reprotect` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to reprotect or reverse replicate a failed over replication protected item. |
| `ReplicationProtectedItems_ResolveHealthErrors` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to resolve health issues of the replication protected item. |
| `ReplicationProtectedItems_SwitchProvider` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Operation to initiate a switch provider of the replication protected item. |
| `ReplicationProtectedItems_TestFailover` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | Operation to perform a test failover of the replication protected item. |
| `ReplicationProtectedItems_TestFailoverCleanup` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | Operation to clean up the test failover of a replication protected item. |
| `ReplicationProtectedItems_UnplannedFailover` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | Operation to initiate a failover of the replication protected item. |
| `ReplicationProtectedItems_Update` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to update the recovery settings of an ASR replication protected item. |
| `ReplicationProtectedItems_UpdateAppliance` | `EXEC` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to update appliance of an ASR replication protected item. |
| `ReplicationProtectedItems_UpdateMobilityService` | `EXEC` | `api-version, fabricName, protectionContainerName, replicationProtectedItemName, resourceGroupName, resourceName, subscriptionId` | The operation to update(push update) the installed mobility service software on a replication protected item to the latest available version. |
