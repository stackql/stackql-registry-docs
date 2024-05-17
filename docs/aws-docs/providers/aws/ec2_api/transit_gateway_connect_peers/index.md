---
title: transit_gateway_connect_peers
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connect_peers
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_connect_peers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_connect_peers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectPeerConfiguration" /> | `object` | Describes the Connect peer details. |
| <CopyableCode code="creationTime" /> | `string` | The creation time. |
| <CopyableCode code="state" /> | `string` | The state of the Connect peer. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the Connect peer. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the Connect attachment. |
| <CopyableCode code="transitGatewayConnectPeerId" /> | `string` | The ID of the Connect peer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_connect_peers_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more Connect peers. |
| <CopyableCode code="transit_gateway_connect_peer_Create" /> | `INSERT` | <CopyableCode code="InsideCidrBlocks, PeerAddress, TransitGatewayAttachmentId, region" /> | &lt;p&gt;Creates a Connect peer for a specified transit gateway Connect attachment between a transit gateway and an appliance.&lt;/p&gt; &lt;p&gt;The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html#tgw-connect-peer"&gt;Connect peers&lt;/a&gt; in the &lt;i&gt;Transit Gateways Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_connect_peer_Delete" /> | `DELETE` | <CopyableCode code="TransitGatewayConnectPeerId, region" /> | Deletes the specified Connect peer. |
