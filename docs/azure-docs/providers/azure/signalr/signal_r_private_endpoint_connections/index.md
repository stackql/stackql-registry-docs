---
title: signal_r_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_private_endpoint_connections
  - signalr
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
<tr><td><b>Name</b></td><td><code>signal_r_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.signalr.signal_r_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Get the specified private endpoint connection |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List private endpoint connections |
| `delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Delete the specified private endpoint connection |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List private endpoint connections |
| `update` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Update the state of specified private endpoint connection |
