---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | BackupPolicy base |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPolicyName, resourceGroupName, subscriptionId, vaultName` | Gets a backup policy belonging to a backup vault |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Returns list of backup policies belonging to a backup vault |
| `create_or_update` | `INSERT` | `backupPolicyName, resourceGroupName, subscriptionId, vaultName` |  |
| `delete` | `DELETE` | `backupPolicyName, resourceGroupName, subscriptionId, vaultName` |  |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Returns list of backup policies belonging to a backup vault |
