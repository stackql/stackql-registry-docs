---
title: virtual_hub_bgp_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_bgp_connection
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_hub_bgp_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_hub_bgp_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the connection. |
| `properties` | `object` | Properties of the bgp connection. |
| `type` | `string` | Connection type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualHubBgpConnection_Get` | `SELECT` | `connectionName, resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of a Virtual Hub Bgp Connection. |
| `VirtualHubBgpConnection_CreateOrUpdate` | `INSERT` | `connectionName, resourceGroupName, subscriptionId, virtualHubName` | Creates a VirtualHubBgpConnection resource if it doesn't exist else updates the existing VirtualHubBgpConnection. |
| `VirtualHubBgpConnection_Delete` | `DELETE` | `connectionName, resourceGroupName, subscriptionId, virtualHubName` | Deletes a VirtualHubBgpConnection. |
