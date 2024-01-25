---
title: api_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operation
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
<tr><td><b>Name</b></td><td><code>api_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_operation</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the API Operation specified by its identifier. |
| `list_by_api` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the operations for the specified API. |
| `create_or_update` | `INSERT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Creates a new operation in the API or updates an existing one. |
| `delete` | `DELETE` | `If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified operation in the API. |
| `_list_by_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the operations for the specified API. |
| `update` | `EXEC` | `If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the operation in the API specified by its identifier. |
