---
title: traffic_mirror_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_mirror_targets
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
<tr><td><b>Name</b></td><td><code>traffic_mirror_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.traffic_mirror_targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Information about the Traffic Mirror target. |
| `trafficMirrorTargetId` | `string` | The ID of the Traffic Mirror target. |
| `type` | `string` | The type of Traffic Mirror target. |
| `gatewayLoadBalancerEndpointId` | `string` | The ID of the Gateway Load Balancer endpoint. |
| `networkInterfaceId` | `string` | The network interface ID that is attached to the target. |
| `networkLoadBalancerArn` | `string` | The Amazon Resource Name (ARN) of the Network Load Balancer. |
| `ownerId` | `string` | The ID of the account that owns the Traffic Mirror target. |
| `tagSet` | `array` | The tags assigned to the Traffic Mirror target. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `traffic_mirror_targets_Describe` | `SELECT` |  | Information about one or more Traffic Mirror targets. |
| `traffic_mirror_target_Create` | `INSERT` |  | &lt;p&gt;Creates a target for your Traffic Mirror session.&lt;/p&gt; &lt;p&gt;A Traffic Mirror target is the destination for mirrored traffic. The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can be in the same VPC, or in different VPCs connected via VPC peering or a transit gateway.&lt;/p&gt; &lt;p&gt;A Traffic Mirror target can be a network interface, a Network Load Balancer, or a Gateway Load Balancer endpoint.&lt;/p&gt; &lt;p&gt;To use the target in a Traffic Mirror session, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorSession.htm"&gt;CreateTrafficMirrorSession&lt;/a&gt;.&lt;/p&gt; |
| `traffic_mirror_target_Delete` | `DELETE` | `TrafficMirrorTargetId` | &lt;p&gt;Deletes the specified Traffic Mirror target.&lt;/p&gt; &lt;p&gt;You cannot delete a Traffic Mirror target that is in use by a Traffic Mirror session.&lt;/p&gt; |
