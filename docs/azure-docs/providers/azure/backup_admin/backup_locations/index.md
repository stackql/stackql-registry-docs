---
title: backup_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_locations
  - backup_admin
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
<tr><td><b>Name</b></td><td><code>backup_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.backup_admin.backup_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of a backup location. |
| `tags` | `object` | List of key value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupLocations_Get` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a specific backup location based on name. |
| `BackupLocations_List` | `SELECT` | `resourceGroupName, subscriptionId` | Returns the list of backup locations. |
| `BackupLocations_CreateBackup` | `EXEC` | `location, resourceGroupName, subscriptionId` | Back up a specific location. |
| `BackupLocations_PruneExternalStore` | `EXEC` | `location, resourceGroupName, subscriptionId` | Prune the external backup store. |
| `BackupLocations_Update` | `EXEC` | `location, resourceGroupName, subscriptionId` | Update a backup location. |
