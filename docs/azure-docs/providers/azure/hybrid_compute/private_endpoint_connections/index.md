---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - hybrid_compute
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
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a private endpoint connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId` | Gets a private endpoint connection. |
| `list_by_private_link_scope` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` | Gets all private endpoint connections on a private link scope. |
| `create_or_update` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId` | Deletes a private endpoint connection with a given name. |
| `_list_by_private_link_scope` | `EXEC` | `resourceGroupName, scopeName, subscriptionId` | Gets all private endpoint connections on a private link scope. |
