---
title: peering
hide_title: false
hide_table_of_contents: false
keywords:
  - peering
  - peering
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
<tr><td><b>Name</b></td><td><code>peering</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.peering</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `kind` | `string` | The kind of the peering. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | The properties that define connectivity to the Microsoft Cloud Edge. |
| `sku` | `object` | The SKU that defines the tier and kind of the peering. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Peerings_Get` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` | Gets an existing peering with the specified name under the given subscription and resource group. |
| `Peerings_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the peerings under the given subscription and resource group. |
| `Peerings_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the peerings under the given subscription. |
| `Peerings_CreateOrUpdate` | `INSERT` | `peeringName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku` | Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group. |
| `Peerings_Delete` | `DELETE` | `peeringName, resourceGroupName, subscriptionId` | Deletes an existing peering with the specified name under the given subscription and resource group. |
| `Peerings_Update` | `EXEC` | `peeringName, resourceGroupName, subscriptionId` | Updates tags for a peering with the specified name under the given subscription and resource group. |
