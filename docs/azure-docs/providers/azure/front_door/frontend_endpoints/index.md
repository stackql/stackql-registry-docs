---
title: frontend_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - frontend_endpoints
  - front_door
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
<tr><td><b>Name</b></td><td><code>frontend_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.front_door.frontend_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The JSON object that contains the properties required to create a frontend endpoint. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId` | Gets a Frontend endpoint with the specified name within the specified Front Door. |
| `list_by_front_door` | `SELECT` | `frontDoorName, resourceGroupName, subscriptionId` | Lists all of the frontend endpoints within a Front Door. |
| `_list_by_front_door` | `EXEC` | `frontDoorName, resourceGroupName, subscriptionId` | Lists all of the frontend endpoints within a Front Door. |
| `disable_https` | `EXEC` | `frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId` | Disables a frontendEndpoint for HTTPS traffic |
| `enable_https` | `EXEC` | `frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId, data__certificateSource, data__minimumTlsVersion, data__protocolType` | Enables a frontendEndpoint for HTTPS traffic |
