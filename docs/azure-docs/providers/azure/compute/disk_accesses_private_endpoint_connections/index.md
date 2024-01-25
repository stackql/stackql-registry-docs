---
title: disk_accesses_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses_private_endpoint_connections
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
<tr><td><b>Name</b></td><td><code>disk_accesses_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_accesses_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | private endpoint connection Id |
| `name` | `string` | private endpoint connection name |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `type` | `string` | private endpoint connection type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `diskAccessName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `diskAccessName, resourceGroupName, subscriptionId` |
