---
title: traffic_mirror_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_mirror_sessions
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
<tr><td><b>Name</b></td><td><code>traffic_mirror_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.traffic_mirror_sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the Traffic Mirror session. |
| `trafficMirrorFilterId` | `string` | The ID of the Traffic Mirror filter. |
| `virtualNetworkId` | `integer` | The virtual network ID associated with the Traffic Mirror session. |
| `packetLength` | `integer` | The number of bytes in each packet to mirror. These are the bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet |
| `sessionNumber` | `integer` | &lt;p&gt;The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.&lt;/p&gt; &lt;p&gt;Valid values are 1-32766.&lt;/p&gt; |
| `trafficMirrorTargetId` | `string` | The ID of the Traffic Mirror target. |
| `ownerId` | `string` | The ID of the account that owns the Traffic Mirror session. |
| `networkInterfaceId` | `string` | The ID of the Traffic Mirror session's network interface. |
| `tagSet` | `array` | The tags assigned to the Traffic Mirror session. |
| `trafficMirrorSessionId` | `string` | The ID for the Traffic Mirror session. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `traffic_mirror_sessions_Describe` | `SELECT` |  | Describes one or more Traffic Mirror sessions. By default, all Traffic Mirror sessions are described. Alternatively, you can filter the results. |
| `traffic_mirror_session_Create` | `INSERT` | `NetworkInterfaceId, SessionNumber, TrafficMirrorFilterId, TrafficMirrorTargetId` | &lt;p&gt;Creates a Traffic Mirror session.&lt;/p&gt; &lt;p&gt;A Traffic Mirror session actively copies packets from a Traffic Mirror source to a Traffic Mirror target. Create a filter, and then assign it to the session to define a subset of the traffic to mirror, for example all TCP traffic.&lt;/p&gt; &lt;p&gt;The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can be in the same VPC, or in a different VPC connected via VPC peering or a transit gateway. &lt;/p&gt; &lt;p&gt;By default, no traffic is mirrored. Use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilter.htm"&gt;CreateTrafficMirrorFilter&lt;/a&gt; to create filter rules that specify the traffic to mirror.&lt;/p&gt; |
| `traffic_mirror_session_Delete` | `DELETE` | `TrafficMirrorSessionId` | Deletes the specified Traffic Mirror session. |
| `traffic_mirror_session_Modify` | `EXEC` | `TrafficMirrorSessionId` | Modifies a Traffic Mirror session. |
