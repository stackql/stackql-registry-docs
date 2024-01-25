---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | Extended location pointing to the underlying infrastructure |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the virtual network resource |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the virtual networks in the specified resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists the virtual networks in the specified subscription |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Creates or updates the virtual network resource |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName` | Deletes the specified virtual network resource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the virtual networks in the specified resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists the virtual networks in the specified subscription |
| `retrieve` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets the specified virtual network resource |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Patches the virtual network resource |
