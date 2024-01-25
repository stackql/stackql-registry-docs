---
title: slices
hide_title: false
hide_table_of_contents: false
keywords:
  - slices
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>slices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.slices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network slice properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId` | Gets information about the specified network slice. |
| `list_by_mobile_network` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all slices in the mobile network. |
| `create_or_update` | `INSERT` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId, data__properties` | Creates or updates a network slice. Must be created in the same location as its parent mobile network. |
| `delete` | `DELETE` | `mobileNetworkName, resourceGroupName, sliceName, subscriptionId` | Deletes the specified network slice. |
| `_list_by_mobile_network` | `EXEC` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all slices in the mobile network. |
