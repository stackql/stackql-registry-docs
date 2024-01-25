---
title: order_items
hide_title: false
hide_table_of_contents: false
keywords:
  - order_items
  - edge_order
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>order_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_order.order_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Msi identity details of the resource |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Represents order item properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `orderItemName, resourceGroupName, subscriptionId` | Get an order item. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List order items at resource group level. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List order items at subscription level. |
| `create` | `INSERT` | `orderItemName, resourceGroupName, subscriptionId, data__properties` | Create an order item. Existing order item cannot be updated with this api and should instead be updated with the Update order item<br />API. |
| `delete` | `DELETE` | `orderItemName, resourceGroupName, subscriptionId` | Delete an order item. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List order items at resource group level. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List order items at subscription level. |
| `cancel` | `EXEC` | `orderItemName, resourceGroupName, subscriptionId, data__reason` | Cancel order item. |
| `return` | `EXEC` | `orderItemName, resourceGroupName, subscriptionId, data__returnReason` | Return order item. |
| `update` | `EXEC` | `orderItemName, resourceGroupName, subscriptionId` | Update the properties of an existing order item. |
