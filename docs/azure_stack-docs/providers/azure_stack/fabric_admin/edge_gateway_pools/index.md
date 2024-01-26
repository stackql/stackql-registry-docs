---
title: edge_gateway_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_gateway_pools
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>edge_gateway_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.edge_gateway_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | An object that contains the properties of an edge gateway pool. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `edgeGatewayPool, location, resourceGroupName, subscriptionId` | Returns the requested edge gateway pool object. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all edge gateway pool objects at a location. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns a list of all edge gateway pool objects at a location. |
