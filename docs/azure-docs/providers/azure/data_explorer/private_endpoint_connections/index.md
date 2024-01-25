---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - data_explorer
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
<tr><td><b>Id</b></td><td><code>azure.data_explorer.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a private endpoint connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets a private endpoint connection. |
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of private endpoint connections. |
| `create_or_update` | `INSERT` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `delete` | `DELETE` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection with a given name. |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of private endpoint connections. |
