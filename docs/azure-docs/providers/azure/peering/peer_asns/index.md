---
title: peer_asns
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_asns
  - peering
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
<tr><td><b>Name</b></td><td><code>peer_asns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.peer_asns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties that define a peer's ASN. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PeerAsns_Get` | `SELECT` | `peerAsnName, subscriptionId` | Gets the peer ASN with the specified name under the given subscription. |
| `PeerAsns_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the peer ASNs under the given subscription. |
| `PeerAsns_CreateOrUpdate` | `INSERT` | `peerAsnName, subscriptionId` | Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription. |
| `PeerAsns_Delete` | `DELETE` | `peerAsnName, subscriptionId` | Deletes an existing peer ASN with the specified name under the given subscription. |
