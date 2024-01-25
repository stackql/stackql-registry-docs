---
title: web_apps_vnet_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_vnet_connection
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
<tr><td><b>Name</b></td><td><code>web_apps_vnet_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_vnet_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | Virtual Network information contract. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Gets a virtual network the app (or deployment slot) is connected to by name. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Deletes a connection from an app (or deployment slot to a named virtual network. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
