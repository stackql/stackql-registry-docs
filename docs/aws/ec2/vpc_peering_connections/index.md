---
title: vpc_peering_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_peering_connections
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
<tr><td><b>Name</b></td><td><code>vpc_peering_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_peering_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `vpcPeeringConnectionId` | `string` | The ID of the VPC peering connection. |
| `accepterVpcInfo` | `object` | Describes a VPC in a VPC peering connection. |
| `expirationTime` | `string` | The time that an unaccepted VPC peering connection will expire. |
| `requesterVpcInfo` | `object` | Describes a VPC in a VPC peering connection. |
| `status` | `object` | Describes the status of a VPC peering connection. |
| `tagSet` | `array` | Any tags assigned to the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_peering_connections_Describe` | `SELECT` |  | Describes one or more of your VPC peering connections. |
| `vpc_peering_connection_Create` | `INSERT` |  | &lt;p&gt;Requests a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection. The accepter VPC can belong to another Amazon Web Services account and can be in a different Region to the requester VPC. The requester VPC and accepter VPC cannot have overlapping CIDR blocks.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Limitations and rules apply to a VPC peering connection. For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations"&gt;limitations&lt;/a&gt; section in the &lt;i&gt;VPC Peering Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The owner of the accepter VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected.&lt;/p&gt; &lt;p&gt;If you create a VPC peering connection request between VPCs with overlapping CIDR blocks, the VPC peering connection has a status of &lt;code&gt;failed&lt;/code&gt;.&lt;/p&gt; |
| `vpc_peering_connection_Delete` | `DELETE` | `VpcPeeringConnectionId` | Deletes a VPC peering connection. Either the owner of the requester VPC or the owner of the accepter VPC can delete the VPC peering connection if it's in the &lt;code&gt;active&lt;/code&gt; state. The owner of the requester VPC can delete a VPC peering connection in the &lt;code&gt;pending-acceptance&lt;/code&gt; state. You cannot delete a VPC peering connection that's in the &lt;code&gt;failed&lt;/code&gt; state. |
| `vpc_peering_connection_Accept` | `EXEC` |  | &lt;p&gt;Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the &lt;code&gt;pending-acceptance&lt;/code&gt; state, and you must be the owner of the peer VPC. Use &lt;a&gt;DescribeVpcPeeringConnections&lt;/a&gt; to view your outstanding VPC peering connection requests.&lt;/p&gt; &lt;p&gt;For an inter-Region VPC peering connection request, you must accept the VPC peering connection in the Region of the accepter VPC.&lt;/p&gt; |
| `vpc_peering_connection_Reject` | `EXEC` | `VpcPeeringConnectionId` | Rejects a VPC peering connection request. The VPC peering connection must be in the &lt;code&gt;pending-acceptance&lt;/code&gt; state. Use the &lt;a&gt;DescribeVpcPeeringConnections&lt;/a&gt; request to view your outstanding VPC peering connection requests. To delete an active VPC peering connection, or to delete a VPC peering connection request that you initiated, use &lt;a&gt;DeleteVpcPeeringConnection&lt;/a&gt;. |
