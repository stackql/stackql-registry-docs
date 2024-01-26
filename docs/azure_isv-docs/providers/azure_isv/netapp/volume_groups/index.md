---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
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
<tr><td><b>Name</b></td><td><code>volume_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.volume_groups</code></td></tr>
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
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId, volumeGroupName` | Get details of the specified volume group |
| `list_by_netapp_account` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all volume groups for given account |
| `create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, volumeGroupName` | Create a volume group along with specified volumes |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, volumeGroupName` | Delete the specified volume group only if there are no volumes under volume group. |
| `_list_by_netapp_account` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | List all volume groups for given account |
