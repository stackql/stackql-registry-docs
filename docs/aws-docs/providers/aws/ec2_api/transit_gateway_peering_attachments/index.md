---
title: transit_gateway_peering_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_peering_attachments
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
<tr><td><b>Name</b></td><td><code>transit_gateway_peering_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_peering_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accepterTgwInfo" /> | `object` | Information about the transit gateway in the peering attachment. |
| <CopyableCode code="creationTime" /> | `string` | The time the transit gateway peering attachment was created. |
| <CopyableCode code="requesterTgwInfo" /> | `object` | Information about the transit gateway in the peering attachment. |
| <CopyableCode code="state" /> | `string` | The state of the transit gateway peering attachment. Note that the &lt;code&gt;initiating&lt;/code&gt; state has been deprecated. |
| <CopyableCode code="status" /> | `object` | The status of the transit gateway peering attachment. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the transit gateway peering attachment. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the transit gateway peering attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_peering_attachments_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes your transit gateway peering attachments. |
| <CopyableCode code="transit_gateway_peering_attachment_Create" /> | `INSERT` | <CopyableCode code="PeerAccountId, PeerRegion, PeerTransitGatewayId, TransitGatewayId, region" /> | &lt;p&gt;Requests a transit gateway peering attachment between the specified transit gateway (requester) and a peer transit gateway (accepter). The transit gateways must be in different Regions. The peer transit gateway can be in your account or a different Amazon Web Services account.&lt;/p&gt; &lt;p&gt;After you create the peering attachment, the owner of the accepter transit gateway must accept the attachment request.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_peering_attachment_Delete" /> | `DELETE` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | Deletes a transit gateway peering attachment. |
| <CopyableCode code="transit_gateway_peering_attachment_Accept" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | Accepts a transit gateway peering attachment request. The peering attachment must be in the &lt;code&gt;pendingAcceptance&lt;/code&gt; state. |
| <CopyableCode code="transit_gateway_peering_attachment_Reject" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | Rejects a transit gateway peering attachment request. |
