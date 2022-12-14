---
title: network
hide_title: false
hide_table_of_contents: false
keywords:
  - network
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.network</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes properties of a network resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Network_Get` | `SELECT` | `api-version, networkResourceName, resourceGroupName, subscriptionId` | Gets the information about the network resource with the given name. The information include the description and other properties of the network. |
| `Network_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network. |
| `Network_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets the information about all network resources in a given resource group. The information include the description and other properties of the network. |
| `Network_Create` | `INSERT` | `api-version, networkResourceName, resourceGroupName, subscriptionId, data__properties` | Creates a network resource with the specified name, description and properties. If a network resource with the same name exists, then it is updated with the specified description and properties. |
| `Network_Delete` | `DELETE` | `api-version, networkResourceName, resourceGroupName, subscriptionId` | Deletes the network resource identified by the name. |
