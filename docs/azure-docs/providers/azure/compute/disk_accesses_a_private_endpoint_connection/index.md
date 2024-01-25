---
title: disk_accesses_a_private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses_a_private_endpoint_connection
  - compute
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
<tr><td><b>Name</b></td><td><code>disk_accesses_a_private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_accesses_a_private_endpoint_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | private endpoint connection Id |
| `name` | `string` | private endpoint connection name |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `type` | `string` | private endpoint connection type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets information about a private endpoint connection under a disk access resource. |
| `delete` | `DELETE` | `diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection under a disk access resource. |
| `update` | `EXEC` | `diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection under disk access resource, this can't be used to create a new private endpoint connection. |
