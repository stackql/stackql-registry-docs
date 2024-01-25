---
title: application_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways
  - network
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
<tr><td><b>Name</b></td><td><code>application_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the application gateway. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the specified application gateway. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all application gateways in a resource group. |
| `create_or_update` | `INSERT` | `applicationGatewayName, resourceGroupName, subscriptionId` | Creates or updates the specified application gateway. |
| `delete` | `DELETE` | `applicationGatewayName, resourceGroupName, subscriptionId` | Deletes the specified application gateway. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all application gateways in a resource group. |
| `backend_health` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the backend health of the specified application gateway in a resource group. |
| `backend_health_on_demand` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group. |
| `start` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Starts the specified application gateway. |
| `stop` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Stops the specified application gateway in a resource group. |
