---
title: tag
hide_title: false
hide_table_of_contents: false
keywords:
  - tag
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
<tr><td><b>Name</b></td><td><code>tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tag</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, tagId` | Gets the details of the tag specified by its identifier. |
| `list_by_api` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the API. |
| `list_by_operation` | `SELECT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the Operation. |
| `list_by_product` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the Product. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of tags defined within a service instance. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, tagId` | Creates a tag. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, tagId` | Deletes specific tag of the API Management service instance. |
| `_list_by_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the API. |
| `_list_by_operation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the Operation. |
| `_list_by_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the Product. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of tags defined within a service instance. |
| `assign_to_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Assign tag to the Api. |
| `assign_to_operation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Assign tag to the Operation. |
| `assign_to_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Assign tag to the Product. |
| `detach_from_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Detach the tag from the Api. |
| `detach_from_operation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Detach the tag from the Operation. |
| `detach_from_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Detach the tag from the Product. |
| `get_by_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Get tag associated with the API. |
| `get_by_operation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Get tag associated with the Operation. |
| `get_by_product` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Get tag associated with the Product. |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, tagId` | Updates the details of the tag specified by its identifier. |
