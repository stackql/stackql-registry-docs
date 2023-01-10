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
| `properties` | `object` | Represents order item properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OrderItems_Get` | `SELECT` | `orderItemName, resourceGroupName, subscriptionId` | Get an order item. |
| `OrderItems_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List order items at resource group level. |
| `OrderItems_ListBySubscription` | `SELECT` | `subscriptionId` | List order items at subscription level. |
| `OrderItems_Create` | `INSERT` | `orderItemName, resourceGroupName, subscriptionId, data__properties` | Create an order item. Existing order item cannot be updated with this api and should instead be updated with the Update order item<br />API. |
| `OrderItems_Delete` | `DELETE` | `orderItemName, resourceGroupName, subscriptionId` | Delete an order item. |
| `OrderItems_Cancel` | `EXEC` | `orderItemName, resourceGroupName, subscriptionId, data__reason` | Cancel order item. |
| `OrderItems_Return` | `EXEC` | `orderItemName, resourceGroupName, subscriptionId, data__returnReason` | Return order item. |
| `OrderItems_Update` | `EXEC` | `orderItemName, resourceGroupName, subscriptionId` | Update the properties of an existing order item. |
