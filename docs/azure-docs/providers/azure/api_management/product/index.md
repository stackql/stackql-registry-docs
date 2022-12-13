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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Product profile. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Product_Get` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the product specified by its identifier. |
| `Product_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of products in the specified service instance. |
| `Product_CreateOrUpdate` | `INSERT` | `productId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a product. |
| `Product_Delete` | `DELETE` | `If-Match, productId, resourceGroupName, serviceName, subscriptionId` | Delete product. |
| `Product_GetEntityTag` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the product specified by its identifier. |
| `Product_ListByTags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of products associated with tags. |
| `Product_Update` | `EXEC` | `If-Match, productId, resourceGroupName, serviceName, subscriptionId` | Update existing product details. |
