---
title: migration_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_recovery_points
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
<tr><td><b>Name</b></td><td><code>migration_recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.migration_recovery_points</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Migration item recovery point properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, fabricName, migrationItemName, migrationRecoveryPointName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` |
| `list_by_replication_migration_items` | `SELECT` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` |
| `_list_by_replication_migration_items` | `EXEC` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` |
