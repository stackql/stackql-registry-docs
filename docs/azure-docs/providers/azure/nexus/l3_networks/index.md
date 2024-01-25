---
title: l3_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - l3_networks
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
<tr><td><b>Name</b></td><td><code>l3_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.l3_networks</code></td></tr>
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
| `get` | `SELECT` | `l3NetworkName, resourceGroupName, subscriptionId` | Get properties of the provided layer 3 (L3) network. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of layer 3 (L3) networks in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of layer 3 (L3) networks in the provided subscription. |
| `create_or_update` | `INSERT` | `l3NetworkName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new layer 3 (L3) network or update the properties of the existing network. |
| `delete` | `DELETE` | `l3NetworkName, resourceGroupName, subscriptionId` | Delete the provided layer 3 (L3) network. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of layer 3 (L3) networks in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of layer 3 (L3) networks in the provided subscription. |
| `update` | `EXEC` | `l3NetworkName, resourceGroupName, subscriptionId` | Update tags associated with the provided layer 3 (L3) network. |
