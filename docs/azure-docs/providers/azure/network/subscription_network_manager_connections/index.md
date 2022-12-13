---
title: subscription_network_manager_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_network_manager_connections
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
<tr><td><b>Name</b></td><td><code>subscription_network_manager_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.subscription_network_manager_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Information about the network manager connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SubscriptionNetworkManagerConnections_Get` | `SELECT` |  | Get a specified connection created by this subscription. |
| `SubscriptionNetworkManagerConnections_List` | `SELECT` | `subscriptionId` | List all network manager connections created by this subscription. |
| `SubscriptionNetworkManagerConnections_CreateOrUpdate` | `INSERT` |  | Create a network manager connection on this subscription. |
| `SubscriptionNetworkManagerConnections_Delete` | `DELETE` |  | Delete specified connection created by this subscription. |
