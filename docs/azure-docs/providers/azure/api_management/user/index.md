---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.user</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, userId` | Gets the details of the user specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of registered users in the specified service instance. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, userId` | Creates or Updates a user. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, userId` | Deletes specific user. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of registered users in the specified service instance. |
| `generate_sso_url` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, userId` | Retrieves a redirection URL containing an authentication token for signing a given user into the developer portal. |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, userId` | Updates the details of the user specified by its identifier. |
