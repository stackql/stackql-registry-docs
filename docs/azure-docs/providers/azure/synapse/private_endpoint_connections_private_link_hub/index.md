---
title: private_endpoint_connections_private_link_hub
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_private_link_hub
  - synapse
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_private_link_hub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.private_endpoint_connections_private_link_hub</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | identifier |
| `properties` | `object` | Properties of a private endpoint connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnectionsPrivateLinkHub_Get` | `SELECT` |  | Get all PrivateEndpointConnection in the PrivateLinkHub by name |
| `PrivateEndpointConnectionsPrivateLinkHub_List` | `SELECT` |  | Get all PrivateEndpointConnections in the PrivateLinkHub |
