---
title: web_apps_vnet_connection_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_vnet_connection_gateway
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_vnet_connection_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_vnet_connection_gateway</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | VnetGateway resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Gets an app's Virtual Network gateway. |
| `create_or_update` | `INSERT` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| `update` | `EXEC` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
