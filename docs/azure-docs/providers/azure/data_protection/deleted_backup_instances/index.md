---
title: deleted_backup_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_backup_instances
  - data_protection
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
<tr><td><b>Name</b></td><td><code>deleted_backup_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.deleted_backup_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | Deleted Backup Instance |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | Gets a deleted backup instance with name in a backup vault |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets deleted backup instances belonging to a backup vault |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Gets deleted backup instances belonging to a backup vault |
| `undelete` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` |  |
