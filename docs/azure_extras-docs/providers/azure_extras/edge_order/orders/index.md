---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
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
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_order.orders</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, orderName, resourceGroupName, subscriptionId` | Get an order. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List orders at resource group level. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List orders at subscription level. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List orders at resource group level. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List orders at subscription level. |
