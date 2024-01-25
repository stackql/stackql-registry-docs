---
title: data_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - data_networks
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
<tr><td><b>Name</b></td><td><code>data_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.data_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Data network properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Gets information about the specified data network. |
| `list_by_mobile_network` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all data networks in the mobile network. |
| `create_or_update` | `INSERT` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Creates or updates a data network. Must be created in the same location as its parent mobile network. |
| `delete` | `DELETE` | `dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId` | Deletes the specified data network. |
| `_list_by_mobile_network` | `EXEC` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all data networks in the mobile network. |
