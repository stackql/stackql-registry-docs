---
title: product_group
hide_title: false
hide_table_of_contents: false
keywords:
  - product_group
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
<tr><td><b>Name</b></td><td><code>product_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product_group</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_product` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of developer groups associated with the specified product. |
| `create_or_update` | `INSERT` | `groupId, productId, resourceGroupName, serviceName, subscriptionId` | Adds the association between the specified developer group with the specified product. |
| `delete` | `DELETE` | `groupId, productId, resourceGroupName, serviceName, subscriptionId` | Deletes the association between the specified group and product. |
| `_list_by_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of developer groups associated with the specified product. |
| `check_entity_exists` | `EXEC` | `groupId, productId, resourceGroupName, serviceName, subscriptionId` | Checks that Group entity specified by identifier is associated with the Product entity. |
