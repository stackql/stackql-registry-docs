---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.backup_admin.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties for a backup. |
| `tags` | `object` | List of key value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backup, location, resourceGroupName, subscriptionId` | Returns a backup from a location based on name. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of backups from a location. |
| `create` | `INSERT` | `location, resourceGroupName, subscriptionId` | Back up a specific location. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns a list of backups from a location. |
| `restore` | `EXEC` | `backup, location, resourceGroupName, subscriptionId` | Restore a backup. |
