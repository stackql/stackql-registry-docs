---
title: transit_gateway_multicast_group_members
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_members
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
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_multicast_group_members</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_multicast_group_members_Deregister` | `EXEC` |  | Deregisters the specified members (network interfaces) from the transit gateway multicast group. |
| `transit_gateway_multicast_group_members_Register` | `EXEC` |  | &lt;p&gt;Registers members (network interfaces) with the transit gateway multicast group. A member is a network interface associated with a supported EC2 instance that receives multicast traffic. For information about supported instances, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-limits.html#multicast-limits"&gt;Multicast Consideration&lt;/a&gt; in &lt;i&gt;Amazon VPC Transit Gateways&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;After you add the members, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayMulticastGroups.html"&gt;SearchTransitGatewayMulticastGroups&lt;/a&gt; to verify that the members were added to the transit gateway multicast group.&lt;/p&gt; |
