---
title: api
hide_title: false
hide_table_of_contents: false
keywords:
  - api
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
<tr><td><b>Name</b></td><td><code>api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the API specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all APIs of the API Management service instance. |
| `create_or_update` | `INSERT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Creates new or updates existing specified API of the API Management service instance. |
| `delete` | `DELETE` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API of the API Management service instance. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists all APIs of the API Management service instance. |
| `_list_by_tags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of apis associated with tags. |
| `list_by_tags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of apis associated with tags. |
| `update` | `EXEC` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId` | Updates the specified API of the API Management service instance. |
