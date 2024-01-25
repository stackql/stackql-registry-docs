---
title: product
hide_title: false
hide_table_of_contents: false
keywords:
  - product
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
<tr><td><b>Name</b></td><td><code>product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the product specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of products in the specified service instance. |
| `create_or_update` | `INSERT` | `productId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a product. |
| `delete` | `DELETE` | `If-Match, productId, resourceGroupName, serviceName, subscriptionId` | Delete product. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of products in the specified service instance. |
| `_list_by_tags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of products associated with tags. |
| `list_by_tags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of products associated with tags. |
| `update` | `EXEC` | `If-Match, productId, resourceGroupName, serviceName, subscriptionId` | Update existing product details. |
