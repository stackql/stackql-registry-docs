---
title: transit_gateway_vpc_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_vpc_attachments
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
<tr><td><b>Name</b></td><td><code>transit_gateway_vpc_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_vpc_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | The creation time. |
| <CopyableCode code="options" /> | `object` | Describes the VPC attachment options. |
| <CopyableCode code="state" /> | `string` | The state of the VPC attachment. Note that the &lt;code&gt;initiating&lt;/code&gt; state has been deprecated. |
| <CopyableCode code="subnetIds" /> | `array` | The IDs of the subnets. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the VPC attachment. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the attachment. |
| <CopyableCode code="transitGatewayId" /> | `string` | The ID of the transit gateway. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC. |
| <CopyableCode code="vpcOwnerId" /> | `string` | The ID of the Amazon Web Services account that owns the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_vpc_attachments_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can filter the results. |
| <CopyableCode code="transit_gateway_vpc_attachment_Create" /> | `INSERT` | <CopyableCode code="SubnetIds, TransitGatewayId, VpcId, region" /> | &lt;p&gt;Attaches the specified VPC to the specified transit gateway.&lt;/p&gt; &lt;p&gt;If you attach a VPC with a CIDR range that overlaps the CIDR range of a VPC that is already attached, the new VPC CIDR range is not propagated to the default propagation route table.&lt;/p&gt; &lt;p&gt;To send VPC traffic to an attached transit gateway, add a route to the VPC route table using &lt;a&gt;CreateRoute&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_vpc_attachment_Delete" /> | `DELETE` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | Deletes the specified VPC attachment. |
| <CopyableCode code="transit_gateway_vpc_attachment_Accept" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | &lt;p&gt;Accepts a request to attach a VPC to a transit gateway.&lt;/p&gt; &lt;p&gt;The VPC attachment must be in the &lt;code&gt;pendingAcceptance&lt;/code&gt; state. Use &lt;a&gt;DescribeTransitGatewayVpcAttachments&lt;/a&gt; to view your pending VPC attachment requests. Use &lt;a&gt;RejectTransitGatewayVpcAttachment&lt;/a&gt; to reject a VPC attachment request.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_vpc_attachment_Modify" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | Modifies the specified VPC attachment. |
| <CopyableCode code="transit_gateway_vpc_attachment_Reject" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | &lt;p&gt;Rejects a request to attach a VPC to a transit gateway.&lt;/p&gt; &lt;p&gt;The VPC attachment must be in the &lt;code&gt;pendingAcceptance&lt;/code&gt; state. Use &lt;a&gt;DescribeTransitGatewayVpcAttachments&lt;/a&gt; to view your pending VPC attachment requests. Use &lt;a&gt;AcceptTransitGatewayVpcAttachment&lt;/a&gt; to accept a VPC attachment request.&lt;/p&gt; |
