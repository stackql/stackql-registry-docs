---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
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
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.peerings</code></td></tr>
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
| `get` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` | Gets an existing peering with the specified name under the given subscription and resource group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the peerings under the given subscription and resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all of the peerings under the given subscription. |
| `create_or_update` | `INSERT` | `peeringName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku` | Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group. |
| `delete` | `DELETE` | `peeringName, resourceGroupName, subscriptionId` | Deletes an existing peering with the specified name under the given subscription and resource group. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the peerings under the given subscription and resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all of the peerings under the given subscription. |
| `update` | `EXEC` | `peeringName, resourceGroupName, subscriptionId` | Updates tags for a peering with the specified name under the given subscription and resource group. |
