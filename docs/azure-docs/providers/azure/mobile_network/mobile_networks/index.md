---
title: mobile_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_networks
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
<tr><td><b>Name</b></td><td><code>mobile_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.mobile_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Mobile network properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Gets information about the specified mobile network. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the mobile networks in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the mobile networks in a subscription. |
| `create_or_update` | `INSERT` | `mobileNetworkName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a mobile network. |
| `delete` | `DELETE` | `mobileNetworkName, resourceGroupName, subscriptionId` | Deletes the specified mobile network. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the mobile networks in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the mobile networks in a subscription. |
