---
title: l2_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - l2_networks
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
<tr><td><b>Name</b></td><td><code>l2_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.l2_networks</code></td></tr>
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
| `get` | `SELECT` | `l2NetworkName, resourceGroupName, subscriptionId` | Get properties of the provided layer 2 (L2) network. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of layer 2 (L2) networks in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of layer 2 (L2) networks in the provided subscription. |
| `create_or_update` | `INSERT` | `l2NetworkName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new layer 2 (L2) network or update the properties of the existing network. |
| `delete` | `DELETE` | `l2NetworkName, resourceGroupName, subscriptionId` | Delete the provided layer 2 (L2) network. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of layer 2 (L2) networks in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of layer 2 (L2) networks in the provided subscription. |
| `update` | `EXEC` | `l2NetworkName, resourceGroupName, subscriptionId` | Update tags associated with the provided layer 2 (L2) network. |
