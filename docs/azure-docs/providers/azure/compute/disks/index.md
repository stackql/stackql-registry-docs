---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
  - compute
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
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | Resource location |
| `managedBy` | `string` | A relative URI containing the ID of the VM that has the disk attached. |
| `managedByExtended` | `array` | List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs. |
| `properties` | `object` | Disk resource properties. |
| `sku` | `object` | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `zones` | `array` | The Logical zone list for Disk. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diskName, resourceGroupName, subscriptionId` | Gets information about a disk. |
| `list` | `SELECT` | `subscriptionId` | Lists all the disks under a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the disks under a resource group. |
| `create_or_update` | `INSERT` | `diskName, resourceGroupName, subscriptionId` | Creates or updates a disk. |
| `delete` | `DELETE` | `diskName, resourceGroupName, subscriptionId` | Deletes a disk. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the disks under a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the disks under a resource group. |
| `grant_access` | `EXEC` | `diskName, resourceGroupName, subscriptionId, data__access, data__durationInSeconds` | Grants access to a disk. |
| `revoke_access` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Revokes access to a disk. |
| `update` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Updates (patches) a disk. |
