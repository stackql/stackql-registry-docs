---
title: item_level_recovery_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - item_level_recovery_connections
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>item_level_recovery_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.item_level_recovery_connections</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ItemLevelRecoveryConnections_Provision` | `EXEC` | `api-version, containerName, fabricName, protectedItemName, recoveryPointId, resourceGroupName, subscriptionId, vaultName` | Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens a file<br />explorer displaying all the recoverable files and folders. This is an asynchronous operation. To know the status of<br />provisioning, call GetProtectedItemOperationResult API. |
| `ItemLevelRecoveryConnections_Revoke` | `EXEC` | `api-version, containerName, fabricName, protectedItemName, recoveryPointId, resourceGroupName, subscriptionId, vaultName` | Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer<br />displaying all recoverable files and folders. This is an asynchronous operation. |
