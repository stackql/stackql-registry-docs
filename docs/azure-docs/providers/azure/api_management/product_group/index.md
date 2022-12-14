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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Group contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductGroup_ListByProduct` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of developer groups associated with the specified product. |
| `ProductGroup_CreateOrUpdate` | `INSERT` | `groupId, productId, resourceGroupName, serviceName, subscriptionId` | Adds the association between the specified developer group with the specified product. |
| `ProductGroup_Delete` | `DELETE` | `groupId, productId, resourceGroupName, serviceName, subscriptionId` | Deletes the association between the specified group and product. |
| `ProductGroup_CheckEntityExists` | `EXEC` | `groupId, productId, resourceGroupName, serviceName, subscriptionId` | Checks that Group entity specified by identifier is associated with the Product entity. |
