---
title: transit_gateway_connect_peers
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connect_peers
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_connect_peers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_connect_peers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationTime` | `string` | The creation time. |
| `state` | `string` | The state of the Connect peer. |
| `tagSet` | `array` | The tags for the Connect peer. |
| `transitGatewayAttachmentId` | `string` | The ID of the Connect attachment. |
| `transitGatewayConnectPeerId` | `string` | The ID of the Connect peer. |
| `connectPeerConfiguration` | `object` | Describes the Connect peer details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_connect_peers_Describe` | `SELECT` |  | Describes one or more Connect peers. |
| `transit_gateway_connect_peer_Create` | `INSERT` | `InsideCidrBlocks, PeerAddress, TransitGatewayAttachmentId` | &lt;p&gt;Creates a Connect peer for a specified transit gateway Connect attachment between a transit gateway and an appliance.&lt;/p&gt; &lt;p&gt;The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html#tgw-connect-peer"&gt;Connect peers&lt;/a&gt; in the &lt;i&gt;Transit Gateways Guide&lt;/i&gt;.&lt;/p&gt; |
| `transit_gateway_connect_peer_Delete` | `DELETE` | `TransitGatewayConnectPeerId` | Deletes the specified Connect peer. |
