---
title: gateway_api
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_api
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
<tr><td><b>Name</b></td><td><code>gateway_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway_api</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_service` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the APIs associated with a gateway. |
| `create_or_update` | `INSERT` | `apiId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Adds an API to the specified Gateway. |
| `delete` | `DELETE` | `apiId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API from the specified Gateway. |
| `_list_by_service` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the APIs associated with a gateway. |
