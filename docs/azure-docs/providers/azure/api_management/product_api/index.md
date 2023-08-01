---
title: product_api
hide_title: false
hide_table_of_contents: false
keywords:
  - product_api
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
<tr><td><b>Name</b></td><td><code>product_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product_api</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | API Entity Properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductApi_ListByProduct` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the APIs associated with a product. |
| `ProductApi_CreateOrUpdate` | `INSERT` | `apiId, productId, resourceGroupName, serviceName, subscriptionId` | Adds an API to the specified product. |
| `ProductApi_Delete` | `DELETE` | `apiId, productId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API from the specified product. |
| `ProductApi_CheckEntityExists` | `EXEC` | `apiId, productId, resourceGroupName, serviceName, subscriptionId` | Checks that API entity specified by identifier is associated with the Product entity. |
