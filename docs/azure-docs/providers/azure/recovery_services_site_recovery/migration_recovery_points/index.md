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
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
| `properties` | `object` | Migration item recovery point properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MigrationRecoveryPoints_Get` | `SELECT` | `api-version, fabricName, migrationItemName, migrationRecoveryPointName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` |
| `MigrationRecoveryPoints_ListByReplicationMigrationItems` | `SELECT` | `api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` |
