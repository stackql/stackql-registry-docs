---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `type` | `string` | The resource type. |
| `properties` | `object` | The properties of a private endpoint connection |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Get private endpoint connection properties |
| `PrivateEndpointConnections_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | List private endpoint connection properties |
| `PrivateEndpointConnections_Delete` | `DELETE` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Delete private endpoint connection with the specified name |
| `PrivateEndpointConnections_Update` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId, data__properties` | Update the status of a private endpoint connection with the specified name |
