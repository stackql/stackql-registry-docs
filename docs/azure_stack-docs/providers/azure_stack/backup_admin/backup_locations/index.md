---
title: backup_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_locations
  - backup_admin
  - azure_stack    
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
<tr><td><b>Id</b></td><td><code>azure_stack.backup_admin.backup_locations</code></td></tr>
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
| `get` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a specific backup location based on name. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Returns the list of backup locations. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Returns the list of backup locations. |
| `prune_external_store` | `EXEC` | `location, resourceGroupName, subscriptionId` | Prune the external backup store. |
| `update` | `EXEC` | `location, resourceGroupName, subscriptionId` | Update a backup location. |
