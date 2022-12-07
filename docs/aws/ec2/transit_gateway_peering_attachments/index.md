---
title: transit_gateway_peering_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peering_attachments
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
<tr><td><b>Name</b></td><td><code>transit_gateway_peering_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_peering_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accepterTgwInfo` | `object` | Information about the transit gateway in the peering attachment. |
| `creationTime` | `string` | The time the transit gateway peering attachment was created. |
| `requesterTgwInfo` | `object` | Information about the transit gateway in the peering attachment. |
| `state` | `string` | The state of the transit gateway peering attachment. Note that the &lt;code&gt;initiating&lt;/code&gt; state has been deprecated. |
| `status` | `object` | The status of the transit gateway peering attachment. |
| `tagSet` | `array` | The tags for the transit gateway peering attachment. |
| `transitGatewayAttachmentId` | `string` | The ID of the transit gateway peering attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_peering_attachments_Describe` | `SELECT` |  | Describes your transit gateway peering attachments. |
| `transit_gateway_peering_attachment_Create` | `INSERT` | `PeerAccountId, PeerRegion, PeerTransitGatewayId, TransitGatewayId` | &lt;p&gt;Requests a transit gateway peering attachment between the specified transit gateway (requester) and a peer transit gateway (accepter). The transit gateways must be in different Regions. The peer transit gateway can be in your account or a different Amazon Web Services account.&lt;/p&gt; &lt;p&gt;After you create the peering attachment, the owner of the accepter transit gateway must accept the attachment request.&lt;/p&gt; |
| `transit_gateway_peering_attachment_Delete` | `DELETE` | `TransitGatewayAttachmentId` | Deletes a transit gateway peering attachment. |
| `transit_gateway_peering_attachment_Accept` | `EXEC` | `TransitGatewayAttachmentId` | Accepts a transit gateway peering attachment request. The peering attachment must be in the &lt;code&gt;pendingAcceptance&lt;/code&gt; state. |
| `transit_gateway_peering_attachment_Reject` | `EXEC` | `TransitGatewayAttachmentId` | Rejects a transit gateway peering attachment request. |
