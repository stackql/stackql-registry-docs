---
title: fleet_history
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_history
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
<tr><td><b>Name</b></td><td><code>fleet_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.fleet_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `historyRecordSet` | `array` | Information about the events in the history of the EC2 Fleet. |
| `lastEvaluatedTime` | `string` | &lt;p&gt;The last date and time for the events, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). All records up to this time were retrieved.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; indicates that there are more results, this value is not present.&lt;/p&gt; |
| `nextToken` | `string` | The token for the next set of results. |
| `startTime` | `string` | The start date and time for the events, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). |
| `fleetId` | `string` | The ID of the EC Fleet. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `fleet_history_Describe` | `SELECT` | `FleetId, StartTime` |
