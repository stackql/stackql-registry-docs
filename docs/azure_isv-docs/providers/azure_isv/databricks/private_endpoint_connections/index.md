---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - databricks
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.databricks.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The properties of a private endpoint connection |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Get a private endpoint connection properties for a workspace |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List private endpoint connections of the workspace |
| `create` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Update the status of a private endpoint connection with the specified name |
| `delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Remove private endpoint connection with the specified name |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List private endpoint connections of the workspace |
