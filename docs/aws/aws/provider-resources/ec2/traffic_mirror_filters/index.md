---
title: traffic_mirror_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_mirror_filters
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
<tr><td><b>Name</b></td><td><code>traffic_mirror_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.traffic_mirror_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the Traffic Mirror filter. |
| `egressFilterRuleSet` | `array` | Information about the egress rules that are associated with the Traffic Mirror filter. |
| `ingressFilterRuleSet` | `array` | Information about the ingress rules that are associated with the Traffic Mirror filter. |
| `networkServiceSet` | `array` | The network service traffic that is associated with the Traffic Mirror filter. |
| `tagSet` | `array` | The tags assigned to the Traffic Mirror filter. |
| `trafficMirrorFilterId` | `string` | The ID of the Traffic Mirror filter. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `traffic_mirror_filters_Describe` | `SELECT` |  | Describes one or more Traffic Mirror filters. |
| `traffic_mirror_filter_Create` | `INSERT` |  | &lt;p&gt;Creates a Traffic Mirror filter.&lt;/p&gt; &lt;p&gt;A Traffic Mirror filter is a set of rules that defines the traffic to mirror.&lt;/p&gt; &lt;p&gt;By default, no traffic is mirrored. To mirror traffic, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilterRule.htm"&gt;CreateTrafficMirrorFilterRule&lt;/a&gt; to add Traffic Mirror rules to the filter. The rules you add define what traffic gets mirrored. You can also use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterNetworkServices.html"&gt;ModifyTrafficMirrorFilterNetworkServices&lt;/a&gt; to mirror supported network services.&lt;/p&gt; |
| `traffic_mirror_filter_Delete` | `DELETE` | `TrafficMirrorFilterId` | &lt;p&gt;Deletes the specified Traffic Mirror filter.&lt;/p&gt; &lt;p&gt;You cannot delete a Traffic Mirror filter that is in use by a Traffic Mirror session.&lt;/p&gt; |
