---
title: watchers_next_hop
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_next_hop
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
<tr><td><b>Name</b></td><td><code>watchers_next_hop</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.watchers_next_hop</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextHopIpAddress` | `string` | Next hop IP Address. |
| `nextHopType` | `string` | Next hop type. |
| `routeTableId` | `string` | The resource identifier for the route table associated with the route being returned. If the route being returned does not correspond to any user created routes then this field will be the string 'System Route'. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId, data__destinationIPAddress, data__sourceIPAddress, data__targetResourceId` |
