---
title: transit_gateway_multicast_group_members
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_group_members
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
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_group_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_multicast_group_members" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_multicast_group_members_Deregister" /> | `EXEC` | <CopyableCode code="region" /> | Deregisters the specified members (network interfaces) from the transit gateway multicast group. |
| <CopyableCode code="transit_gateway_multicast_group_members_Register" /> | `EXEC` | <CopyableCode code="region" /> | &lt;p&gt;Registers members (network interfaces) with the transit gateway multicast group. A member is a network interface associated with a supported EC2 instance that receives multicast traffic. For information about supported instances, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-limits.html#multicast-limits"&gt;Multicast Consideration&lt;/a&gt; in &lt;i&gt;Amazon VPC Transit Gateways&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;After you add the members, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayMulticastGroups.html"&gt;SearchTransitGatewayMulticastGroups&lt;/a&gt; to verify that the members were added to the transit gateway multicast group.&lt;/p&gt; |
