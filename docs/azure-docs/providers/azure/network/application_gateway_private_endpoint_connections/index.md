---
title: application_gateway_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_private_endpoint_connections
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
<tr><td><b>Name</b></td><td><code>application_gateway_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateway_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the private endpoint connection on an application gateway. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of Private Link Resource of an application gateway. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationGatewayName, connectionName, resourceGroupName, subscriptionId` | Gets the specified private endpoint connection on application gateway. |
| `list` | `SELECT` | `applicationGatewayName, resourceGroupName, subscriptionId` | Lists all private endpoint connections on an application gateway. |
| `delete` | `DELETE` | `applicationGatewayName, connectionName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint connection on application gateway. |
| `_list` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Lists all private endpoint connections on an application gateway. |
| `update` | `EXEC` | `applicationGatewayName, connectionName, resourceGroupName, subscriptionId` | Updates the specified private endpoint connection on application gateway. |
