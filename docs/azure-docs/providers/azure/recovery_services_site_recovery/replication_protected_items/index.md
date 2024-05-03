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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protected_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Replication protected item custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR replication protected item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected items in the vault. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected items in the protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an ASR replication protected item (Enable replication). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to disable replication on a replication protected item. This will also remove the item. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected items in the vault. |
| <CopyableCode code="_list_by_replication_protection_containers" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected items in the protection container. |
| <CopyableCode code="add_disks" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to add disks(s) to the replication protected item. |
| <CopyableCode code="apply_recovery_point" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to change the recovery point of a failed over replication protected item. |
| <CopyableCode code="failover_cancel" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to cancel the failover of the replication protected item. |
| <CopyableCode code="failover_commit" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to commit the failover of the replication protected item. |
| <CopyableCode code="planned_failover" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to initiate a planned failover of the replication protected item. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item. |
| <CopyableCode code="remove_disks" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to remove disk(s) from the replication protected item. |
| <CopyableCode code="repair_replication" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization. |
| <CopyableCode code="reprotect" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to reprotect or reverse replicate a failed over replication protected item. |
| <CopyableCode code="resolve_health_errors" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to resolve health issues of the replication protected item. |
| <CopyableCode code="switch_provider" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Operation to initiate a switch provider of the replication protected item. |
| <CopyableCode code="test_failover" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to perform a test failover of the replication protected item. |
| <CopyableCode code="test_failover_cleanup" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to clean up the test failover of a replication protected item. |
| <CopyableCode code="unplanned_failover" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to initiate a failover of the replication protected item. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update the recovery settings of an ASR replication protected item. |
