---
title: product_group_link
hide_title: false
hide_table_of_contents: false
keywords:
  - product_group_link
  - api_management
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
<tr><td><b>Name</b></td><td><code>product_group_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product_group_link</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupLinkId, productId, resourceGroupName, serviceName, subscriptionId` | Gets the group link for the product. |
| `list_by_product` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the group links associated with a product. |
| `create_or_update` | `INSERT` | `groupLinkId, productId, resourceGroupName, serviceName, subscriptionId` | Adds a group to the specified product via link. |
| `delete` | `DELETE` | `groupLinkId, productId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified group from the specified product. |
| `_list_by_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the group links associated with a product. |
