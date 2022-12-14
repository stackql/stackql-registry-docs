---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
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
<tr><td><b>Name</b></td><td><code>volume_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.volume_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Volume group properties |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VolumeGroups_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId, volumeGroupName` | Get details of the specified volume group |
| `VolumeGroups_ListByNetAppAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all volume groups for given account |
| `VolumeGroups_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, volumeGroupName` | Create a volume group along with specified volumes |
| `VolumeGroups_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, volumeGroupName` | Delete the specified volume group only if there are no volumes under volume group. |
