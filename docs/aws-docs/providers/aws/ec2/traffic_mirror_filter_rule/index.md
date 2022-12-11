---
title: traffic_mirror_filter_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_mirror_filter_rule
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
<tr><td><b>Name</b></td><td><code>traffic_mirror_filter_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.traffic_mirror_filter_rule</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `traffic_mirror_filter_rule_Create` | `INSERT` | `DestinationCidrBlock, RuleAction, RuleNumber, SourceCidrBlock, TrafficDirection, TrafficMirrorFilterId` | &lt;p&gt;Creates a Traffic Mirror filter rule.&lt;/p&gt; &lt;p&gt;A Traffic Mirror rule defines the Traffic Mirror source traffic to mirror.&lt;/p&gt; &lt;p&gt;You need the Traffic Mirror filter ID when you create the rule.&lt;/p&gt; |
| `traffic_mirror_filter_rule_Delete` | `DELETE` | `TrafficMirrorFilterRuleId` | Deletes the specified Traffic Mirror rule. |
| `traffic_mirror_filter_rule_Modify` | `EXEC` | `TrafficMirrorFilterRuleId` | &lt;p&gt;Modifies the specified Traffic Mirror rule.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DestinationCidrBlock&lt;/code&gt; and &lt;code&gt;SourceCidrBlock&lt;/code&gt; must both be an IPv4 range or an IPv6 range.&lt;/p&gt; |
