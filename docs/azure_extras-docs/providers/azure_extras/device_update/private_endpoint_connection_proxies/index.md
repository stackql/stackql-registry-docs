---
title: private_endpoint_connection_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_proxies
  - device_update
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.device_update.private_endpoint_connection_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Private endpoint connection proxy object property bag. |
| `remotePrivateEndpoint` | `object` | Remote private endpoint details. |
| `status` | `string` | Operation status. |
| `eTag` | `string` | ETag from NRP. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnectionProxies_Get` | `SELECT` | `accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId` | (INTERNAL - DO NOT USE) Get the specified private endpoint connection proxy associated with the device update account. |
| `PrivateEndpointConnectionProxies_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | (INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account. |
| `PrivateEndpointConnectionProxies_CreateOrUpdate` | `INSERT` | `accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId` | (INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account. |
| `PrivateEndpointConnectionProxies_Delete` | `DELETE` | `accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId` | (INTERNAL - DO NOT USE) Deletes the specified private endpoint connection proxy associated with the device update account. |
| `PrivateEndpointConnectionProxies_UpdatePrivateEndpointProperties` | `EXEC` | `accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId` | (INTERNAL - DO NOT USE) Updates a private endpoint inside the private endpoint connection proxy object. |
| `PrivateEndpointConnectionProxies_Validate` | `EXEC` | `accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId` | (INTERNAL - DO NOT USE) Validates a private endpoint connection proxy object. |
