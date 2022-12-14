---
title: private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection
  - batch
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.private_endpoint_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Private endpoint connection properties. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnection_Get` | `SELECT` | `accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets information about the specified private endpoint connection. |
| `PrivateEndpointConnection_ListByBatchAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all of the private endpoint connections in the specified account. |
| `PrivateEndpointConnection_Delete` | `DELETE` | `accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint connection. |
| `PrivateEndpointConnection_Update` | `EXEC` | `accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Updates the properties of an existing private endpoint connection. |
