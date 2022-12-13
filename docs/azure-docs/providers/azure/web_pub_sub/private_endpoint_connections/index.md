---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - web_pub_sub
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
<tr><td><b>Id</b></td><td><code>azure.web_pub_sub.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Private endpoint connection properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebPubSubPrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Get the specified private endpoint connection |
| `WebPubSubPrivateEndpointConnections_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List private endpoint connections |
| `WebPubSubPrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Delete the specified private endpoint connection |
| `WebPubSubPrivateEndpointConnections_Update` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Update the state of specified private endpoint connection |
