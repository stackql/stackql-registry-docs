---
title: product_api_link
hide_title: false
hide_table_of_contents: false
keywords:
  - product_api_link
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
<tr><td><b>Name</b></td><td><code>product_api_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product_api_link</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiLinkId, productId, resourceGroupName, serviceName, subscriptionId` | Gets the API link for the product. |
| `list_by_product` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the API links associated with a product. |
| `create_or_update` | `INSERT` | `apiLinkId, productId, resourceGroupName, serviceName, subscriptionId` | Adds an API to the specified product via link. |
| `delete` | `DELETE` | `apiLinkId, productId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API from the specified product. |
| `_list_by_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the API links associated with a product. |
