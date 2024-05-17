---
title: traffic_mirror_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_mirror_targets
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
<tr><td><b>Name</b></td><td><code>traffic_mirror_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.traffic_mirror_targets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Information about the Traffic Mirror target. |
| <CopyableCode code="gatewayLoadBalancerEndpointId" /> | `string` | The ID of the Gateway Load Balancer endpoint. |
| <CopyableCode code="networkInterfaceId" /> | `string` | The network interface ID that is attached to the target. |
| <CopyableCode code="networkLoadBalancerArn" /> | `string` | The Amazon Resource Name (ARN) of the Network Load Balancer. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the account that owns the Traffic Mirror target. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the Traffic Mirror target. |
| <CopyableCode code="trafficMirrorTargetId" /> | `string` | The ID of the Traffic Mirror target. |
| <CopyableCode code="type" /> | `string` | The type of Traffic Mirror target. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="traffic_mirror_targets_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Information about one or more Traffic Mirror targets. |
| <CopyableCode code="traffic_mirror_target_Create" /> | `INSERT` | <CopyableCode code="region" /> | &lt;p&gt;Creates a target for your Traffic Mirror session.&lt;/p&gt; &lt;p&gt;A Traffic Mirror target is the destination for mirrored traffic. The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can be in the same VPC, or in different VPCs connected via VPC peering or a transit gateway.&lt;/p&gt; &lt;p&gt;A Traffic Mirror target can be a network interface, a Network Load Balancer, or a Gateway Load Balancer endpoint.&lt;/p&gt; &lt;p&gt;To use the target in a Traffic Mirror session, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorSession.htm"&gt;CreateTrafficMirrorSession&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="traffic_mirror_target_Delete" /> | `DELETE` | <CopyableCode code="TrafficMirrorTargetId, region" /> | &lt;p&gt;Deletes the specified Traffic Mirror target.&lt;/p&gt; &lt;p&gt;You cannot delete a Traffic Mirror target that is in use by a Traffic Mirror session.&lt;/p&gt; |
