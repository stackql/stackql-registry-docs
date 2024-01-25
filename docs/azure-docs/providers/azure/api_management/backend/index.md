---
title: backend
hide_title: false
hide_table_of_contents: false
keywords:
  - backend
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
<tr><td><b>Name</b></td><td><code>backend</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.backend</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backendId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the backend specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of backends in the specified service instance. |
| `create_or_update` | `INSERT` | `backendId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a backend. |
| `delete` | `DELETE` | `If-Match, backendId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified backend. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of backends in the specified service instance. |
| `reconnect` | `EXEC` | `backendId, resourceGroupName, serviceName, subscriptionId` | Notifies the API Management gateway to create a new connection to the backend after the specified timeout. If no timeout was specified, timeout of 2 minutes is used. |
| `update` | `EXEC` | `If-Match, backendId, resourceGroupName, serviceName, subscriptionId` | Updates an existing backend. |
