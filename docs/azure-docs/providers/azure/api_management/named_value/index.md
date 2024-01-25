---
title: named_value
hide_title: false
hide_table_of_contents: false
keywords:
  - named_value
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
<tr><td><b>Name</b></td><td><code>named_value</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.named_value</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the named value specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of named values defined within a service instance. |
| `create_or_update` | `INSERT` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Creates or updates named value. |
| `delete` | `DELETE` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId` | Deletes specific named value from the API Management service instance. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of named values defined within a service instance. |
| `refresh_secret` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Refresh the secret of the named value specified by its identifier. |
| `update` | `EXEC` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId` | Updates the specific named value. |
