---
title: transit_gateway_vpc_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_vpc_attachments
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
<tr><td><b>Name</b></td><td><code>transit_gateway_vpc_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_vpc_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | The state of the VPC attachment. Note that the &lt;code&gt;initiating&lt;/code&gt; state has been deprecated. |
| `subnetIds` | `array` | The IDs of the subnets. |
| `tagSet` | `array` | The tags for the VPC attachment. |
| `creationTime` | `string` | The creation time. |
| `options` | `object` | Describes the VPC attachment options. |
| `vpcOwnerId` | `string` | The ID of the Amazon Web Services account that owns the VPC. |
| `vpcId` | `string` | The ID of the VPC. |
| `transitGatewayAttachmentId` | `string` | The ID of the attachment. |
| `transitGatewayId` | `string` | The ID of the transit gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_vpc_attachments_Describe` | `SELECT` |  | Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can filter the results. |
| `transit_gateway_vpc_attachment_Create` | `INSERT` | `SubnetIds, TransitGatewayId, VpcId` | &lt;p&gt;Attaches the specified VPC to the specified transit gateway.&lt;/p&gt; &lt;p&gt;If you attach a VPC with a CIDR range that overlaps the CIDR range of a VPC that is already attached, the new VPC CIDR range is not propagated to the default propagation route table.&lt;/p&gt; &lt;p&gt;To send VPC traffic to an attached transit gateway, add a route to the VPC route table using &lt;a&gt;CreateRoute&lt;/a&gt;.&lt;/p&gt; |
| `transit_gateway_vpc_attachment_Delete` | `DELETE` | `TransitGatewayAttachmentId` | Deletes the specified VPC attachment. |
| `transit_gateway_vpc_attachment_Accept` | `EXEC` | `TransitGatewayAttachmentId` | &lt;p&gt;Accepts a request to attach a VPC to a transit gateway.&lt;/p&gt; &lt;p&gt;The VPC attachment must be in the &lt;code&gt;pendingAcceptance&lt;/code&gt; state. Use &lt;a&gt;DescribeTransitGatewayVpcAttachments&lt;/a&gt; to view your pending VPC attachment requests. Use &lt;a&gt;RejectTransitGatewayVpcAttachment&lt;/a&gt; to reject a VPC attachment request.&lt;/p&gt; |
| `transit_gateway_vpc_attachment_Modify` | `EXEC` | `TransitGatewayAttachmentId` | Modifies the specified VPC attachment. |
| `transit_gateway_vpc_attachment_Reject` | `EXEC` | `TransitGatewayAttachmentId` | &lt;p&gt;Rejects a request to attach a VPC to a transit gateway.&lt;/p&gt; &lt;p&gt;The VPC attachment must be in the &lt;code&gt;pendingAcceptance&lt;/code&gt; state. Use &lt;a&gt;DescribeTransitGatewayVpcAttachments&lt;/a&gt; to view your pending VPC attachment requests. Use &lt;a&gt;AcceptTransitGatewayVpcAttachment&lt;/a&gt; to accept a VPC attachment request.&lt;/p&gt; |
