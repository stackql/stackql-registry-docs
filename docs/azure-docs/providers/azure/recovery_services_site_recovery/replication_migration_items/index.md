---
title: replication_migration_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_migration_items
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
<tr><td><b>Name</b></td><td><code>replication_migration_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_migration_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Migration item properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` |  |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` |  |
| `list_by_replication_protection_containers` | `SELECT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR migration items in the protection container. |
| `create` | `INSERT` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to create an ASR migration item (enable migration). |
| `delete` | `DELETE` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to delete an ASR migration item. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` |  |
| `_list_by_replication_protection_containers` | `EXEC` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the list of ASR migration items in the protection container. |
| `migrate` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to initiate migration of the item. |
| `pause_replication` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to initiate pause replication of the item. |
| `resume_replication` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to initiate resume replication of the item. |
| `resync` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to resynchronize replication of an ASR migration item. |
| `test_migrate` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to initiate test migration of the item. |
| `test_migrate_cleanup` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to initiate test migrate cleanup. |
| `update` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to update the recovery settings of an ASR migration item. |
