---
title: tag_product_link
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_product_link
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
<tr><td><b>Name</b></td><td><code>tag_product_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tag_product_link</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `productLinkId, resourceGroupName, serviceName, subscriptionId, tagId` | Gets the product link for the tag. |
| `list_by_product` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, tagId` | Lists a collection of the product links associated with a tag. |
| `create_or_update` | `INSERT` | `productLinkId, resourceGroupName, serviceName, subscriptionId, tagId` | Adds a product to the specified tag via link. |
| `delete` | `DELETE` | `productLinkId, resourceGroupName, serviceName, subscriptionId, tagId` | Deletes the specified product from the specified tag. |
| `_list_by_product` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, tagId` | Lists a collection of the product links associated with a tag. |
