---
title: spot_fleet_request_history
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_fleet_request_history
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
<tr><td><b>Name</b></td><td><code>spot_fleet_request_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.spot_fleet_request_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `timestamp` | `string` | The date and time of the event, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). |
| `eventInformation` | `object` | Describes an EC2 Fleet or Spot Fleet event. |
| `eventType` | `string` | &lt;p&gt;The event type.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;error&lt;/code&gt; - An error with the Spot Fleet request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;fleetRequestChange&lt;/code&gt; - A change in the status or configuration of the Spot Fleet request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;instanceChange&lt;/code&gt; - An instance was launched or terminated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Information&lt;/code&gt; - An informational event.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `spot_fleet_request_history_Describe` | `SELECT` | `SpotFleetRequestId, StartTime` |
