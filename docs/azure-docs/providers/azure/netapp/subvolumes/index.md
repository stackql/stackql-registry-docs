---
title: subvolumes
hide_title: false
hide_table_of_contents: false
keywords:
  - subvolumes
  - netapp
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
<tr><td><b>Name</b></td><td><code>subvolumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.subvolumes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subvolumes_Get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Returns the path associated with the subvolumeName provided |
| `Subvolumes_ListByVolume` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Returns a list of the subvolumes in the volume |
| `Subvolumes_Create` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Creates a subvolume in the path or clones the subvolume mentioned in the parentPath |
| `Subvolumes_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Delete subvolume |
| `Subvolumes_GetMetadata` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Get details of the specified subvolume |
| `Subvolumes_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName` | Patch a subvolume |
