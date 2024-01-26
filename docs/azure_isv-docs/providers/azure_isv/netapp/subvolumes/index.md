---
title: subvolumes
hide_title: false
hide_table_of_contents: false
keywords:
  - subvolumes
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
<tr><td><b>Name</b></td><td><code>subvolumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.subvolumes</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Returns the path associated with the subvolumeName provided |
| `list_by_volume` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Returns a list of the subvolumes in the volume |
| `create` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Creates a subvolume in the path or clones the subvolume mentioned in the parentPath |
| `delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Delete subvolume |
| `_list_by_volume` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Returns a list of the subvolumes in the volume |
| `update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Patch a subvolume |
