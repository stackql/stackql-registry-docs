---
title: gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway
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
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Gateway specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of gateways registered with service instance. |
| `create_or_update` | `INSERT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Creates or updates a Gateway to be used in Api Management instance. |
| `delete` | `DELETE` | `If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId` | Deletes specific Gateway. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of gateways registered with service instance. |
| `generate_token` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId, data__expiry, data__keyType` | Gets the Shared Access Authorization Token for the gateway. |
| `invalidate_debug_credentials` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Action is invalidating all debug credentials issued for gateway. |
| `regenerate_key` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId, data__keyType` | Regenerates specified gateway key invalidating any tokens created with it. |
| `update` | `EXEC` | `If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the gateway specified by its identifier. |
