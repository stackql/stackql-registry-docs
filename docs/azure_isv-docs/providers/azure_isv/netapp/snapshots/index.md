---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location |
| `properties` | `object` | Snapshot properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName` | Get details of the specified snapshot |
| `list` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all snapshots associated with the volume |
| `create` | `INSERT` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__location` | Create the specified snapshot within the given volume |
| `delete` | `DELETE` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName` | Delete snapshot |
| `_list` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all snapshots associated with the volume |
| `restore_files` | `EXEC` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__filePaths` | Restore the specified files from the specified snapshot to the active filesystem |
| `update` | `EXEC` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName` | Patch a snapshot |
