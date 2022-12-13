---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - key_vault
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
<tr><td><b>Id</b></td><td><code>azure.key_vault.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the key vault resource. |
| `name` | `string` | Name of the key vault resource. |
| `location` | `string` | Azure location of the key vault resource. |
| `properties` | `object` | Properties of the private endpoint connection resource. |
| `tags` | `object` | Tags assigned to the key vault resource. |
| `type` | `string` | Resource type of the key vault resource. |
| `etag` | `string` | Modified whenever there is a change in the state of private endpoint connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName` | Gets the specified private endpoint connection associated with the key vault. |
| `PrivateEndpointConnections_ListByResource` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | The List operation gets information about the private endpoint connections associated with the vault. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName` | Deletes the specified private endpoint connection associated with the key vault. |
| `PrivateEndpointConnections_Put` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName` | Updates the specified private endpoint connection associated with the key vault. |
