---
title: authorization_server
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server
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
<tr><td><b>Name</b></td><td><code>authorization_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.authorization_server</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authsid, resourceGroupName, serviceName, subscriptionId` | Gets the details of the authorization server specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization servers defined within a service instance. |
| `create_or_update` | `INSERT` | `authsid, resourceGroupName, serviceName, subscriptionId` | Creates new authorization server or updates an existing authorization server. |
| `delete` | `DELETE` | `If-Match, authsid, resourceGroupName, serviceName, subscriptionId` | Deletes specific authorization server instance. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization servers defined within a service instance. |
| `update` | `EXEC` | `If-Match, authsid, resourceGroupName, serviceName, subscriptionId` | Updates the details of the authorization server specified by its identifier. |
