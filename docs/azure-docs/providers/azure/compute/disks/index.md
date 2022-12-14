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
| `properties` | `object` | Disk resource properties. |
| `sku` | `object` | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | Resource location |
| `zones` | `array` | The Logical zone list for Disk. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `managedByExtended` | `array` | List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs. |
| `managedBy` | `string` | A relative URI containing the ID of the VM that has the disk attached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Disks_Get` | `SELECT` | `diskName, resourceGroupName, subscriptionId` | Gets information about a disk. |
| `Disks_List` | `SELECT` | `subscriptionId` | Lists all the disks under a subscription. |
| `Disks_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the disks under a resource group. |
| `Disks_CreateOrUpdate` | `INSERT` | `diskName, resourceGroupName, subscriptionId` | Creates or updates a disk. |
| `Disks_Delete` | `DELETE` | `diskName, resourceGroupName, subscriptionId` | Deletes a disk. |
| `Disks_GrantAccess` | `EXEC` | `diskName, resourceGroupName, subscriptionId, data__access, data__durationInSeconds` | Grants access to a disk. |
| `Disks_RevokeAccess` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Revokes access to a disk. |
| `Disks_Update` | `EXEC` | `diskName, resourceGroupName, subscriptionId` | Updates (patches) a disk. |
