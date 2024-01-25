---
title: logger
hide_title: false
hide_table_of_contents: false
keywords:
  - logger
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
<tr><td><b>Name</b></td><td><code>logger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.logger</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `loggerId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the logger specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of loggers in the specified service instance. |
| `create_or_update` | `INSERT` | `loggerId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a logger. |
| `delete` | `DELETE` | `If-Match, loggerId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified logger. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of loggers in the specified service instance. |
| `update` | `EXEC` | `If-Match, loggerId, resourceGroupName, serviceName, subscriptionId` | Updates an existing logger. |
