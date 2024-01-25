---
title: trunked_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - trunked_networks
  - nexus
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
<tr><td><b>Name</b></td><td><code>trunked_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.trunked_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, trunkedNetworkName` | Get properties of the provided trunked network. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of trunked networks in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of trunked networks in the provided subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, trunkedNetworkName, data__extendedLocation, data__properties` | Create a new trunked network or update the properties of the existing trunked network. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, trunkedNetworkName` | Delete the provided trunked network. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of trunked networks in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of trunked networks in the provided subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, trunkedNetworkName` | Update tags associated with the provided trunked network. |
