---
title: edge_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_gateways
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
<tr><td><b>Name</b></td><td><code>edge_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.edge_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | Object which holds information related to edge gateways. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `edgeGateway, location, resourceGroupName, subscriptionId` | Returns the requested edge gateway. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns the list of all edge gateways at a certain location. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns the list of all edge gateways at a certain location. |
